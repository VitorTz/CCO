

class Livro:

    def __init__(
        self,
        isbn: str,
        titulo: str,
        autor: str,
        editora: str,
        edicao: str,
        genero: str,
        vendedores: dict
    ) -> None:
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__edicao = edicao
        self.__genero = genero
        self.__vendedores = vendedores
    
    @property
    def info_completa(self) -> dict:
        """Retorna as informações completas do livro em forma de dicionário"""
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "editora": self.editora,
            "edicao": self.edicao,
            "genero": self.genero,
            "vendedores": self.vendedores
        }
    
    @property
    def isbn(self) -> str:
        return self.__isbn 
    
    @property
    def titulo(self) -> str:
        return self.__titulo
    
    @property
    def editora(self) -> str:
        return self.__editora 

    @property
    def autor(self) -> str:
        return self.__autor
    
    @property
    def edicao(self) -> str:
        return self.__edicao 
    
    @property
    def genero(self) -> str:
        return self.__genero
    
    @property
    def vendedores(self) -> str:
        return self.__vendedores
    
    def __str__(self) -> str:
        return self.titulo