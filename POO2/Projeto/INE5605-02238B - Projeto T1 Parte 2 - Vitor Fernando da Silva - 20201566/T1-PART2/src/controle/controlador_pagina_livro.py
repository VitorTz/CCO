from src.controle.tipo_pagina import TipoPagina
from src.limite.abstract_tela import TipoMensagem
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_pagina_livro import TelaPaginaLivro
from src.entidade.livro import Livro


class ControladorPaginaLivro(AbstractControlador):
    """
    Mostra uma página com informações sobre um livro especifico e permite
    adiciona-lo ao carrinho
    """
    
    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Ver informações do livro", "metodo": self.__opcao_mostra_info_livro},
                "2": {"desc": "Adicionar ao carrinho pelo menor preço", "metodo": self.__opcao_add_carrinho_menor_preco},
                "3": {"desc": "Escolher vendedor", "metodo": self.__opcao_escolher_vendedor}
            },
            nome_controlador="Pagina livro"
        )
        self.__livro: Livro | None = None
        self.__tela = TelaPaginaLivro()

    @property
    def tela(self) -> TelaPaginaLivro:
        return self.__tela 

    @property
    def livro(self) -> Livro:
        return self.__livro
    
    @livro.setter
    def livro(self, livro: Livro):
        self.__livro = livro
    
    def __opcao_mostra_info_livro(self) -> None:
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Informações sobre o livro", tipo_msg=TipoMensagem.TITULO)
        self.tela.mostra_info_livro(self.livro.info_completa)
        self.tela.pega_info_usuario("Aperte qualquer tecla e enter para parar de visualizar as informações: ")

    def __opcao_add_carrinho_menor_preco(self) -> None:
        """Adiciona o livro ao carrinho pelo menor preço encontrado"""
        vendedor_menor_preco = {}
        
        for id_vendedor, info_venda in self.livro.vendedores.items():
            if not vendedor_menor_preco or float(info_venda["preco"]) < float(vendedor_menor_preco["preco"]):
                vendedor_menor_preco = {
                    "id_vendedor": id_vendedor,
                    "preco": float(info_venda["preco"])
                }

        self.controlador_sistema.controlador_carrinho.add_livro_carrinho(
            self.livro, 
            vendedor_menor_preco["id_vendedor"],
            str(vendedor_menor_preco["preco"])
            )
        
        self.controlador_sistema.troca_pagina(TipoPagina.PESQUISA, nova_pagina = False)
        self.wait()

    def __opcao_escolher_vendedor(self) -> None:
        vendedores = {
            id: f"{info['preco']}R$" for id, info in self.livro.vendedores.items()
        }
        self.tela.limpa_terminal()
        # Mostra os vendedores disponíveis e pede para o usuário escolher algum
        id_vendedor_escolhido = self.tela.pega_resposta(vendedores, msg="Escolha um vendedor válido.")

        # Adiciona o livro ao carriho
        self.controlador_sistema.controlador_carrinho.add_livro_carrinho(
            self.livro,
            id_vendedor_escolhido,
            self.livro.vendedores[id_vendedor_escolhido]["preco"]
        )



