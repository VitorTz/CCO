from src.controle.tipo_pagina import TipoPagina
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_minha_conta import TelaMinhaConta


class ControladorMinhaConta(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema, 
            opcoes={
                "1": {"desc": "Acessar meu acervo", "metodo": self.__opcao_acessa_acervo},
                "2": {"desc": "Acessar carrinho", "metodo": self.__opcao_carrinho}
            }, 
            nome_controlador="Minha Conta"
        )
        self.__tela = TelaMinhaConta()
        
    @property
    def tela(self) -> TelaMinhaConta:
        return self.__tela
    
    def __opcao_acessa_acervo(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.ACERVO) 
    
    def __opcao_carrinho(self) -> None:
        self.controlador_sistema.pagina = self.controlador_sistema.controlador_carrinho