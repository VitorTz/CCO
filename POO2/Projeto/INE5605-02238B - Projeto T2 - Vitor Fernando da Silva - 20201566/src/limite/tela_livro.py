from src.limite.abstract_tela import AbstractTela
from typing import List
import PySimpleGUI as sg 


class IsbnInvalidaException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__("Digite ums isbn válida, por favor.")


class TelaLivro(AbstractTela):

    def __init__(self) -> None:
        super().__init__(titulo="Acervo geral de livros")
    
    def __valida_isbn(self, isbn: str) -> None:
        if not (len(isbn) == 10):
            raise IsbnInvalidaException()
        
    def pega_isbn(self) -> str:
        _, values = self.get_dados_tela(
            [
                [sg.Text("ISBN10:"), sg.InputText(key="isbn")],
                [sg.Button("Ok"), sg.Button("Cancelar")]
            ]
        )

        try:
            isbn: str = values["isbn"].strip()
            self.__valida_isbn(isbn)
        except Exception as e:
            self.log(e) 
        else:
            return isbn
        
        