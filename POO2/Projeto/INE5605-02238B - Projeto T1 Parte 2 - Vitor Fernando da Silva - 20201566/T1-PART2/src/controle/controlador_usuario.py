from src.entidade.livro import Livro
from src.controle.abstract_controlador import AbstractControlador
from src.entidade.usuario import Usuario
from src.limite.tela_usuario import TelaUsuario
from pathlib import Path


class ControladorUsuario(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema, 
            opcoes={},
            nome_controlador="Usuario"
        )
        self.__path_arquivo_usuarios = Path("db/usuarios.json")
        self.__tela = TelaUsuario()
        self.__usuarios: list[Usuario] = []
        self.__usuario_logado: Usuario | None = None
        # Carrega os usuários
        for info_usuario in self.le_json(self.__path_arquivo_usuarios):
                self.add_usuario(info_usuario)
        
    @property
    def tela(self) -> TelaUsuario:
        return self.__tela
    
    @property
    def usuarios(self) -> list[Usuario]:
        return self.__usuarios
    
    @property
    def usuario_logado(self) -> Usuario:
        return self.__usuario_logado
    
    @usuario_logado.setter
    def usuario_logado(self, usuario: Usuario):
        self.__usuario_logado = usuario
    
    def add_usuario(self, info_usuario: dict, salvar: bool = False):
        self.__usuarios.append(
            Usuario(
                info_usuario["id"],
                info_usuario["nome"],
                info_usuario["primeiro_nome"],
                info_usuario["email"],
                info_usuario["senha"],
                info_usuario["estado"],
                info_usuario["cidade"],
                info_usuario["bairro"],
                info_usuario["cep"],
                info_usuario["logradouro"],
                info_usuario["numero_residencia"],
                info_usuario["complemento"],
                info_usuario["acervo"]
            )
        )
    
        if salvar:
            self.salvar()
    
    def salvar(self):
        """Salva os usuário no arquivo da 'base de dados'"""
        self.salva_json(
                obj=[
                    usuario.info_completa for usuario in self.__usuarios
                ],
                path=self.__path_arquivo_usuarios
            )
    
    def pega_usuario(self, validacao) -> Usuario | None:
        for usuario in self.__usuarios:
            if validacao(usuario):
                return usuario
    
    def pega_acervo(self, usuario: Usuario | None = None) -> list[Livro]:
        """Retorna uma lista com todos os livros no acervo do usuário"""
        if usuario is None:
            usuario = self.__usuario_logado
        pega_livro = self.controlador_sistema.controlador_livro.pega_livro
        return [
            pega_livro(lambda livro: livro.isbn == isbn) for isbn in usuario.acervo.keys()
        ]

