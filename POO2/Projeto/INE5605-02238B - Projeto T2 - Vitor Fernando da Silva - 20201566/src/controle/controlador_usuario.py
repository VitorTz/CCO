from src.controle.abstract_controlador import AbstractControlador, ErroGraveException
from src.entidade.usuario import Usuario
from src.dao.usuario_dao import UsuarioDAO
from src.limite.tela_usuario import TelaUsuario
from random import randint
from typing import Dict
import requests
import PySimpleGUI as sg 



class CepNaoEncontradoException(Exception):

    def __init__(self, cep: str) -> None:
        super().__init__(f"Cep {cep} não encontrado.")


class UsuarioNaoEncontradoException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__("Credenciais inválidas.")

class ControladorUsuario(AbstractControlador):


    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__tela = TelaUsuario()
        self.__dao = UsuarioDAO()
        self.__usuario_logado: Usuario or None = None
    
    @property
    def usuario_logado(self) -> Usuario or None:
        return self.__usuario_logado

    @property
    def tela(self) -> TelaUsuario:
        return self.__tela 

    @property
    def dao(self) -> UsuarioDAO:
        return self.__dao
    
    @property
    def __novo_id(self) -> int:
        """Retorna um novo id de usuário"""
        while True:
            id = randint(1, 66666666666)
            if not self.dao.get(lambda usuario: usuario.id == id):
                return id 
 
    def __pega_dados_endereco(self, cep: str) -> Dict[str, str]:
        """Retorna o endereço do usuário a partir do cep"""
        info_endereco: requests.Response = requests.request(
            "GET",
            url=f"https://cep.awesomeapi.com.br/json/{cep}"
        )
        if info_endereco.status_code != 200:
            raise CepNaoEncontradoException(cep)
        return info_endereco.json()
    
    def __pega_todos_dados_cadastro(self) -> Dict[str, str]:
        """Pega os dados necesários para realizar o cadastro do usuário"""
        info_conta: Dict[str, str] or None = self.tela.pega_valores_cadastro()
        if info_conta:
            try:
                info_endereco: Dict[str, str] or None = self.__pega_dados_endereco(info_conta["cep"])   
            except Exception as e:
                self.tela.popup(e)
            else:
                return {
                    "nome": info_conta["nome"],
                    "email": info_conta["email"],
                    "senha": info_conta["senha"],
                    "estado": info_endereco["state"],
                    "cidade": info_endereco["city"],
                    "bairro": info_endereco["district"],
                    "rua": info_endereco["address"],
                    "cep": info_endereco["cep"],
                    "numero_residencia": info_conta["numero_residencia"]
                }
        
    def novo(self, retornar_entidade_criada: bool = False) -> Usuario or None:
        info_cadastro: Dict[str, str] = self.__pega_todos_dados_cadastro()
        if info_cadastro:
            usuario: Usuario or None = self.dao.get(lambda usuario: usuario.email == info_cadastro["email"].strip().lower())
            if isinstance(usuario, Usuario):
                self.tela.popup(f"Usuário de email {info_cadastro['email']} já existe!")
            else:
                usuario = Usuario(
                    self.__novo_id,
                    info_cadastro["nome"],
                    info_cadastro["email"],
                    info_cadastro["senha"],
                    info_cadastro["estado"],
                    info_cadastro["cidade"],
                    info_cadastro["bairro"],
                    info_cadastro["rua"],
                    info_cadastro["cep"],
                    info_cadastro["numero_residencia"]
                )
                self.dao.add(usuario)
                self.tela.log(f"Novo usuário {usuario.email} criado!")
                self.tela.update_list_box(list(self.dict_entidades.keys()))
            
            if retornar_entidade_criada:
                return usuario

    def editar(self, entidade_selecionada: Usuario) -> None:
        if entidade_selecionada:
            info_cadastro: Dict[str, str] = self.__pega_todos_dados_cadastro()
            if info_cadastro:
                if self.dao.get(lambda usuario: usuario.email == info_cadastro["email"].strip().lower()):
                    self.tela.popup(f"Já existe um usuário com o email {info_cadastro['email']}")
                else:
                    entidade_selecionada.nome = info_cadastro["nome"]
                    entidade_selecionada.email = info_cadastro["email"]
                    entidade_selecionada.senha = info_cadastro["senha"]
                    entidade_selecionada.estado = info_cadastro["estado"]
                    entidade_selecionada.cidade = info_cadastro["cidade"]
                    entidade_selecionada.bairro = info_cadastro["bairro"]
                    entidade_selecionada.rua = info_cadastro["rua"]
                    entidade_selecionada.cep = info_cadastro["cep"]
                    entidade_selecionada.numero_residencia = info_cadastro["numero_residencia"]
                    super().editar(entidade_selecionada)
        else:
            self.tela.popup(f"Selecione uma entidade para editar, por favor.")
    
    def deletar(self, entidade_selecionada: Usuario) -> None:
        super().deletar(entidade_selecionada)
        # Deleta os itens do acervo do usuário
        self.controlador_sistema.controlador_item_acervo_usuario.deleta_itens_acervo_usuario(entidade_selecionada)
        if entidade_selecionada == self.__usuario_logado:
            self.__usuario_logado = None
            raise ErroGraveException("Você deletou o usuário logado, saindo do sistema")

    def __login(self, values: Dict[str, str]) -> None:
        """Efetiva o login do usuário"""
        try:
            self.tela.verifica_valores_tela(values)
            usuario: Usuario or None = self.dao.get(lambda usuario: usuario.email == values["email"].strip().lower())
            if isinstance(usuario, Usuario):
                self.__usuario_logado = usuario
            else:
                raise UsuarioNaoEncontradoException()
        except Exception as e:
            self.tela.popup(e)

    def acesso_sistema(self) -> None:
        """Permite ao usuário se logar/cadastrar para acessar o sistema"""
        event, values = self.tela.pega_valores_acesso_sistema()
        if event == "Login":
            self.__login(values)
        elif event == "Cadastrar":
            self.controlador_sistema.controlador_usuario.novo()
        else:
            self.controlador_sistema.esta_executando = False
    
            
