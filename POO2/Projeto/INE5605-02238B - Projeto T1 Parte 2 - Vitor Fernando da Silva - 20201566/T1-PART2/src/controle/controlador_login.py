from src.controle.tipo_pagina import TipoPagina
from src.limite.abstract_tela import TipoMensagem
from src.limite.tela_login import TelaLogin
from src.controle.abstract_controlador import AbstractControlador


class LoginInvalidoException(Exception):

    def __init__(self, email: str) -> None:
        super().__init__(f"Email ou senha inválidos, login não efetivado.")


class ControladorLogin(AbstractControlador):
    """Realiza o login de um usuário cadastrado no sistema"""

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema, 
            opcoes={
            "1": {"desc": "Fazer Login", "metodo": self.__opcao_login},
            "2": {"desc": "Abrir tela Acesso", "metodo": self.__acesso}
            }, 
            nome_controlador="Login"
        )
        self.__tela = TelaLogin()

    @property
    def tela(self) -> TelaLogin:
        return self.__tela
    
    def __acesso(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.ACESSO)
        
    def __opcao_login(self) -> None:
        
        # Desloga o usuário ativo e limpa o carrinho
        self.controlador_sistema.controlador_usuario.usuario_logado = None
        self.controlador_sistema.controlador_carrinho.limpa_carrinho()
        
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Faça seu login", tipo_msg=TipoMensagem.TITULO)

        email = self.tela.pega_info_usuario("Email: ")
        senha = self.tela.pega_info_usuario("Senha: ")
        
        # Verifica se o usuário existe
        usuario = self.controlador_sistema.controlador_usuario.pega_usuario(lambda usuario: usuario.email == email)
        if not (usuario and usuario.senha == senha):
            raise LoginInvalidoException(email)
        
        # Efetua o login
        self.controlador_sistema.controlador_usuario.usuario_logado = usuario
        self.tela.mostra_msg(f"Bem vindo(a), {usuario.nome}", tipo_msg=TipoMensagem.TITULO)
        
        # Troca para a página HOME
        self.controlador_sistema.troca_pagina(TipoPagina.HOME)
        # Espera por dois segundos antes de mudar de página
        self.wait()

        

