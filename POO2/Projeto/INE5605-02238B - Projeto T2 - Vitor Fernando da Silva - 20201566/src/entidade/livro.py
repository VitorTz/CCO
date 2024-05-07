from src.entidade.abstract_entidade import AbstractEntidade
from typing import Dict


class Livro(AbstractEntidade):

    def __init__(
        self,
        isbn: str,
        titulo: str,
        autor: str,
        editora: str,
        edicao: str,
        genero: str
    ) -> None:
        super().__init__()
        self.isbn = isbn 
        self.titulo = titulo
        self.autor = autor 
        self.editora = editora
        self.edicao = edicao
        self.genero = genero
        self.__views = 0
    
    @property
    def info_entidade(self) -> Dict[str, str]:
        return {
            "Ibsn": self.isbn,
            "Titulo": self.titulo,
            "Autor": self.autor,
            "Editora": self.editora,
            "Edição": self.edicao,
            "Genero": self.genero
        }
    
    @property
    def key(self) -> str:
        return self.isbn
    
    @property
    def isbn(self) -> str:
        return self.__isbn 
    
    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn 
    
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
    
    @property
    def autor(self) -> str:
        return self.__autor 

    @autor.setter
    def autor(self, autor: str):
        self.__autor = autor
    
    @property
    def editora(self) -> str:
        return self.__editora 
    
    @editora.setter
    def editora(self, editora: str):
        self.__editora = editora
    
    @property
    def edicao(self) -> str:
        return self.__edicao 

    @edicao.setter
    def edicao(self, edicao: str):
        self.__edicao = edicao
    
    @property
    def genero(self) -> str:
        return self.__genero
    
    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def views(self) -> int:
        return self.__views 
    
    @views.setter
    def views(self, views: int) -> None:
        self.__views = views

    def __str__(self) -> str:
        return self.titulo
