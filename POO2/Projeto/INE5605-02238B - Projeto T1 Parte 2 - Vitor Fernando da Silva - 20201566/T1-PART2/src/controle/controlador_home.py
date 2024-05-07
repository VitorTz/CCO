from src.controle.abstract_controlador import AbstractControlador
from src.controle.tipo_pagina import TipoPagina
from src.limite.tela_home import TelaHome


class ControladorHome(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema, 
            opcoes={
                "1": {"desc": "Minha Conta", "metodo": self.__opcao_minha_conta},
                "2": {"desc": "Pesquisar Livros", "metodo": self.__opcao_pesquisar}
            }, 
            nome_controlador="Home"
            )
        self.__tela = TelaHome()

    @property
    def tela(self) -> TelaHome:
        return self.__tela

    def __opcao_minha_conta(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.MINHA_CONTA)

    def __opcao_pesquisar(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.PESQUISA)