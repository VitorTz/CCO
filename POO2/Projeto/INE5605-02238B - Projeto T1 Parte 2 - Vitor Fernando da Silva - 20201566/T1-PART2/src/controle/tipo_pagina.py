from enum import Enum, auto


class TipoPagina(Enum):

    ACESSO = auto()
    LOGIN = auto()
    CADASTRO_USUARIO = auto()
    HOME = auto()
    MINHA_CONTA = auto()
    CADASTRO_LIVRO = auto()
    PESQUISA = auto()
    ACERVO = auto()
    PAGINA_LIVRO = auto()
    CARRINHO = auto()
    COMPRA = auto()