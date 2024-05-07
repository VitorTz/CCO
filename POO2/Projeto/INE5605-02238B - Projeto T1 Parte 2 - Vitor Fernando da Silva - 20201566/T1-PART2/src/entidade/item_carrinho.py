from src.entidade.livro import Livro


class ItemCarrinho:

    def __init__(
        self, 
        livro: Livro,
        id_vendedor: str,
        preco: str
    ) -> None:
        self.__livro = livro 
        self.__id_vendedor = id_vendedor
        self.__preco = preco
    
    @property
    def livro(self) -> Livro:
        return self.__livro
    
    @property
    def id_vendedor(self) -> str:
        return self.__id_vendedor
    
    @property
    def preco(self) -> str:
        return self.__preco
    
    @property
    def info_completa(self) -> dict:
        return {
            self.livro.isbn: {
                "id_vendedor": self.id_vendedor,
                "valor": self.preco
            }
        }

    def __str__(self) -> str:
        return f"Titulo - {self.__livro.titulo} | Preço - {self.__preco}"
