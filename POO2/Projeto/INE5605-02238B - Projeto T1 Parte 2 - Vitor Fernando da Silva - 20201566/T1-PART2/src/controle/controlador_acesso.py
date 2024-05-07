from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_acesso import TelaAcesso
from src.controle.tipo_pagina import TipoPagina


class ControladorAcesso(AbstractControlador):
    """Permite ao usuário acessar a tela de login ou de cadastro"""

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Login", "metodo": self.__opcao_login},
                "2": {"desc": "Cadastro", "metodo": self.__opcao_cadastro}
            },
            nome_controlador="Acesso"
        )
        self.__tela = TelaAcesso()
    
    @property
    def tela(self) -> TelaAcesso:
        return self.__tela

    def __opcao_login(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.LOGIN)

    def __opcao_cadastro(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.CADASTRO_USUARIO)
    