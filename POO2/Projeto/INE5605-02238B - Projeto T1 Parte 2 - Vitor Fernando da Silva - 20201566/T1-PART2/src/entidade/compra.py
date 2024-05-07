from ast import For
from src.entidade.usuario import Usuario
from src.entidade.item_carrinho import ItemCarrinho
from enum import Enum, auto 


class Compra:

    def __init__(
        self,
        id_compra: str,
        id_comprador: str, 
        valor_total: str,
        metodo_pagamento: str,
        itens: dict
    ) -> None:
        self.__id_compra = id_compra
        self.__id_comprador = id_comprador
        self.__valor_total = valor_total
        self.__metodo_pagamento = metodo_pagamento
        self.__itens = itens
    
    @property
    def id_compra(self) -> str:
        return self.__id_compra 
    
    @property
    def id_comprador(self) -> str:
        return self.__id_comprador 
    
    @property
    def valor_total(self) -> str:
        return self.__valor_total
    
    @property
    def metodo_pagamento(self) -> str:
        return self.__metodo_pagamento
    
    @property
    def itens(self) -> dict:
        return self.__itens

    @property
    def info_completa(self) -> dict:
        return {
            "id_compra": self.id_compra,
            "id_comprador": self.id_comprador,
            "valor_total": self.valor_total,
            "metodo_pagamento": self.metodo_pagamento,
            "itens": self.itens
        }