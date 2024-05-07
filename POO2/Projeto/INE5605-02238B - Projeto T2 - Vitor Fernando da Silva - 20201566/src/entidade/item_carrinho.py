from src.entidade.usuario import Usuario
from src.entidade.abstract_entidade import AbstractEntidade
from src.entidade.item_acervo_usuario import ItemAcervoUsuario
from typing import Dict


class QuantidadeInvalidaException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__("Quantidade inválida")


class ItemCarrinho(AbstractEntidade):

    def __init__(
        self,
        item_acervo_usuario: ItemAcervoUsuario,
        comprador: Usuario,
        quantidade: int = 0
    ) -> None:
        super().__init__()
        self.__item_acervo_usuario = item_acervo_usuario
        self.__quantidade = quantidade
        self.__comprador = comprador
    
    @property
    def key(self) -> object:
        return self.item_acervo_usuario.key

    @property
    def info_entidade(self) -> str:
        return {
            "Item": self.item_acervo_usuario.livro.titulo,
            "Quantidade": self.quantidade,
            "Valor total": self.valor_total
        }
    
    @property
    def item_acervo_usuario(self) -> ItemAcervoUsuario:
        return self.__item_acervo_usuario
    
    @property
    def comprador(self) -> Usuario:
        return self.__comprador
    
    @property
    def vendedor(self) -> Usuario:
        return self.__item_acervo_usuario.vendedor

    @property
    def quantidade(self) -> int:
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade: int):
        if isinstance(quantidade, int):
            if quantidade >= 0 and quantidade <= self.item_acervo_usuario.exemplares:
                self.__quantidade = quantidade
            else:
                raise QuantidadeInvalidaException()
        
    @property
    def valor_total(self) -> None:
        return self.quantidade * self.item_acervo_usuario.valor
    
    