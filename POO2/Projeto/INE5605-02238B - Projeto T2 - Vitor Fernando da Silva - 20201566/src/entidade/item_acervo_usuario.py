from src.entidade.abstract_entidade import AbstractEntidade
from src.entidade.usuario import Usuario
from src.entidade.livro import Livro
from typing import Dict


class ItemAcervoUsuario(AbstractEntidade):

    def __init__(
        self,
        livro: Livro,
        vendedor: Usuario,
        exemplares: int,
        valor: float
    ) -> None:
        self.__livro = livro 
        self.__vendedor = vendedor
        self.exemplares = exemplares
        self.valor = valor 
        super().__init__()
    
    @property
    def info_entidade(self) -> Dict[str, str]:
        return {
            "Livro": self.livro.titulo,
            "Vendedor": self.vendedor.email,
            "Exemplares": self.exemplares,
            "Valor": self.valor
        }

    @property
    def key(self) -> str:
        return self.livro.key
    
    @property
    def livro(self) -> Livro:
        return self.__livro 
    
    @property
    def vendedor(self) -> Usuario:
        return self.__vendedor 
    
    @property
    def exemplares(self) -> int:
        return self.__exemplares
    
    @exemplares.setter
    def exemplares(self, exemplares: int):
        self.__exemplares = int(exemplares)
    
    @property
    def valor(self) -> float:
        return self.__valor 
    
    @valor.setter
    def valor(self, valor: float):
        self.__valor = float(valor)

