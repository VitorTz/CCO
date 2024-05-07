from src.entidade.usuario import Usuario
from src.entidade.abstract_entidade import AbstractEntidade
from src.entidade.item_carrinho import ItemCarrinho
from datetime import date
from typing import List


class Compra(AbstractEntidade):

    def __init__(
        self,
        id: int,
        itens_carrinho: List[ItemCarrinho],
        comprador: Usuario
    ) -> None:
        super().__init__()
        self.__id = id 
        self.__itens_carrinho = itens_carrinho
        self.__valor_total = sum([item.valor_total for item in self.__itens_carrinho])
        self.__comprador = comprador
        self.__data_compra = date.today()
    
    @property
    def key(self) -> int:
        return self.id 
    
    @property
    def id(self) -> int:
        return self.__id 
    
    @id.setter
    def id(self, id: int):
        self.__id = id 
    
    @property
    def valor_total(self) -> float:
        return self.__valor_total
    
    @property
    def comprador(self) -> Usuario:
        return self.__comprador
    
    @property
    def itens_carrinho(self) -> List[ItemCarrinho]:
        return self.__itens_carrinho
    
    @property
    def data_compra(self) -> str:
        return self.__data_compra

    @property
    def info_entidade(self) -> None:
        pass 

    @property
    def info(self) -> str:
        """Retorna uma string com cada item e seu valor"""
        msg = f"Compra do usuário {self.comprador.email}\n"
        msg += f"Realizada no dia {self.data_compra}\n"
        msg += f"Valor total = {self.valor_total}\n"
        msg += f"Itens:\n"
        for item in self.itens_carrinho:
            msg += "======Inicio Item======\n"
            msg += f"Item Comprado = {item.item_acervo_usuario.livro.titulo}\n"
            msg += f"Quantidade = {item.quantidade}\n"
            msg += f"Valor Total = {item.valor_total}\n"
            msg += f"Vendedor = {item.vendedor.email}\n"
            msg += "======Fim Item======\n"
        return msg  