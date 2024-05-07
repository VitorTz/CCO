from src.limite.abstract_tela import AbstractTela


class IsbnInvalidoException(Exception):

    def __init__(self, isbn: str) -> None:
        super().__init__(f"Isbn {isbn} inválida")


class PrecoInvalidoException(Exception):

    def __init__(self, preco: str) -> None:
        super().__init__(f"Preco {preco} inválido.")


class TelaCadastraLivro(AbstractTela):

    def __init__(self) -> None:
        super().__init__()
    
    def __valida_isbn(self, isbn: str):
        if not len(isbn) == 10:
            raise IsbnInvalidoException(isbn)
    
    def __valida_preco(self, preco: str):
        try:
            float(preco)
        except ValueError:
            raise PrecoInvalidoException(preco)
    
    def pega_isbn(self) -> str:
        return self.pega_info_usuario(
            "Isbn: ",
            self.__valida_isbn
        )
    
    def pega_exemplares(self) -> str:
        return self.pega_info_usuario(
            "Exemplares: ",
            self.valida_numero
        )
    
    def pega_preco_livro(self) -> str:
        return self.pega_info_usuario(
            "Preço: ",
            self.__valida_preco
        )