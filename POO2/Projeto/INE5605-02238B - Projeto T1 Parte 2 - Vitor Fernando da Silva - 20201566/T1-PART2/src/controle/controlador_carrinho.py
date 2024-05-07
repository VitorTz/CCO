from src.controle.tipo_pagina import TipoPagina
from src.limite.abstract_tela import TipoMensagem
from src.entidade.item_carrinho import ItemCarrinho
from src.controle.abstract_controlador import AbstractControlador
from src.entidade.livro import Livro
from src.limite.tela_carrinho import TelaCarrinho


class LivroNaoAdicionadoAoCarrinhoException(Exception):

    def __init__(self) -> None:
        super().__init__("Não foi possível adicionar o livro ao carrinho.")


class CarrinhoVazioException(Exception):

    def __init__(self) -> None:
        super().__init__("Não é possível acessar a página de compra, seu carrinho está vazio")


class LivroInvalidoParaCompraException(Exception):
    """Usado quando o usuário tenta comprar um livro que o pertence"""

    def __init__(self, livro: str) -> None:
        super().__init__(f"Você não pode comprar um livro que já te pertence.")


class LivroJaNoCarrinhoException(Exception):

    def __init__(self) -> None:
        super().__init__("O livro já se encontra no carrinho.")


class ControladorCarrinho(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Efetivar Compra", "metodo": self.__opcao_compra},
                "2": {"desc": "Ver carrinho", "metodo": self.__opcao_mostra_carrinho},
                "3": {"desc": "Remove item carrinho", "metodo": self.__opcao_remover_item}
            },
            nome_controlador="Carrinho"
        )
        self.__tela = TelaCarrinho()
        self.__itens_carrinho: list[ItemCarrinho] = []

    @property
    def tela(self) -> TelaCarrinho:
        return self.__tela 
    
    @property
    def valor_total_carrinho(self) -> int:
        return sum(float(item.preco) for item in self.__itens_carrinho)
    
    @property
    def itens_carrinho(self) -> list[ItemCarrinho]:
        return self.__itens_carrinho
    
    @property
    def id_vendedores_carrinho(self) -> list:
        """Retorna o id e o livro que cada item no carrinho"""
        return {item.id_vendedor: item.livro.isbn for item in self.itens_carrinho}
    
    def limpa_carrinho(self) -> None:
        self.__itens_carrinho.clear()

    def add_livro_carrinho(self, livro: Livro, id_vendedor: str, preco: str):
        if id_vendedor == self.controlador_sistema.controlador_usuario.usuario_logado.id:
            raise LivroInvalidoParaCompraException(livro.titulo)
        
        for item in self.__itens_carrinho:
            if item.livro.isbn == livro.isbn:
                raise LivroJaNoCarrinhoException()

        self.__itens_carrinho.append(ItemCarrinho(livro, id_vendedor, preco))
        self.tela.mostra_msg(f"Livro {livro.titulo} adidionado ao carrinho pelo valor de {preco} reais.")
        self.wait()
    
    def remove_item_carrinho(self, *livro: Livro):
        for l in livro:
            self.__itens_carrinho.remove(l)

    def __opcao_compra(self) -> None:
        """Troca para a página de compra"""
        if not self.__itens_carrinho:
            raise CarrinhoVazioException()
            
        self.controlador_sistema.troca_pagina(TipoPagina.COMPRA)

    def __opcao_mostra_carrinho(self) -> None:
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Itens do carrinho", tipo_msg=TipoMensagem.TITULO)
        self.tela.mostra_msg_lista(self.__itens_carrinho)
        self.tela.pega_info_usuario("Digite qualquer tecla e enter para parar a visualização: ")

    def __opcao_remover_item(self) -> None:
        """Remove um item do carrinho"""
        self.tela.limpa_terminal()

        info_itens = {
            str(n+1): item_carrinho for n, item_carrinho in enumerate(self.__itens_carrinho)
        }
        item_escolhido = self.tela.pega_resposta(
            opcoes=info_itens
        )

        item_escolhido = info_itens[item_escolhido]
        self.__itens_carrinho.remove(item_escolhido)

        self.tela.mostra_msg(f"Item {item_escolhido.livro.titulo} removido do carrinho.")
        self.wait()