from src.limite.abstract_tela import TipoMensagem
from src.controle.tipo_pagina import TipoPagina
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_cadastro_novo_usuario import CepNaoEncontradoException, TelaCadastroNovoUsuario
from requests import request


class EmailJaCadastradoException(Exception):

    def __init__(self, email: str) -> None:
        super().__init__(f"Email {email} já está cadastrado.")


class ControladorCadastroNovoUsuario(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema, 
            opcoes={
            "1": {"desc": "Cadastro", "metodo": self.__opcao_cadastro}
            }, 
            nome_controlador="Cadastro de usuários"
        )
        self.__tela = TelaCadastroNovoUsuario()
    
    @property
    def tela(self) -> TelaCadastroNovoUsuario:
        return self.__tela 
    
    def __pega_info_endereco_pelo_cep(self, cep: str) -> tuple:
        """Procura pela informação completo do endereço do usuário
        através do cep"""
        r = request("GET", url=f"https://cep.awesomeapi.com.br/json/{cep}")
        
        if r.status_code != 200:
            raise CepNaoEncontradoException(cep)
        
        r = r.json()
        return r["state"], r["city"], r["district"], r["address"]
        
    
    def __opcao_cadastro(self) -> None:
        """Faz o cadastro completo do usuário"""
        
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Faça seu cadastro", tipo_msg=TipoMensagem.TITULO)
        
        nome = self.tela.pega_info_usuario("Nome completo: ")
        primeiro_nome = nome if len(nome.split()) == 0 else nome.split()[0]
        email = self.tela.pega_email()
        senha = self.tela.pega_senha()
        
        # Verifica se o usuário já está cadastrado
        if self.controlador_sistema.controlador_usuario.pega_usuario(lambda usuario: usuario.email == email):
            raise EmailJaCadastradoException(email)

        # Pega informações sobre o endereço
        cep = self.tela.pega_cep()
        estado, cidade, bairro, logradouro = self.__pega_info_endereco_pelo_cep(cep)
        numero_residencia = self.tela.pega_numero_residencia()
        complemento = self.tela.pega_info_usuario("Complemento: ")

        # Adiciona o usuário no sistema e salva o arquivo de usuários
        self.controlador_sistema.controlador_usuario.add_usuario(
            {
                "id": str(len(self.controlador_sistema.controlador_usuario.usuarios) + 1),
                "nome": nome,
                "primeiro_nome": primeiro_nome,
                "email": email.lower(),
                "senha": senha,
                "estado": estado,
                "cidade": cidade,
                "bairro": bairro,
                "cep": cep,
                "logradouro": logradouro,
                "numero_residencia": numero_residencia,
                "complemento": complemento,
                "acervo": {},
                "vendas": {},
                "compras": {}
            },
            salvar=True
        )

        self.tela.mostra_msg(f"Usuário {nome} cadastrado com sucesso!")

        # Troca para a página acesso para que o usuário faça login
        self.controlador_sistema.troca_pagina(TipoPagina.ACESSO)
        self.wait()



