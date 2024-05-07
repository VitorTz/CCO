from src.limite.abstract_tela import TipoMensagem
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_livro import TelaLivro
from src.entidade.livro import Livro
from pathlib import Path



class ControladorLivro(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema, 
            opcoes={}, 
            nome_controlador="Livro"
            )
        self.__tela = TelaLivro()
        self.__livros: list[Livro] = []
        self.__path_acervo = Path("db/acervo.json")
        for info_livro in self.le_json(self.__path_acervo):
                self.add_livro(info_livro)
    
    @property
    def livros(self) -> list[Livro]:
        return self.__livros
    
    @property
    def tela(self) -> TelaLivro:
        return self.__tela 
    
    def add_livro(self, info_livro: dict, salvar: bool = False, retorna_livro: bool = False) -> Livro | None:
        livro = Livro(
                isbn=info_livro["isbn"],
                titulo=info_livro["titulo"],
                autor=info_livro["autor"],
                editora=info_livro["editora"],
                edicao=info_livro["edicao"],
                genero=info_livro["genero"],
                vendedores=info_livro["vendedores"],
            )
        self.__livros.append(livro)
        
        if salvar:
            self.salvar()
        
        if retorna_livro:
            return livro
    
    def salvar(self):
        self.salva_json(
                obj=[
                    livro.info_completa for livro in self.__livros
                ],
                path=self.__path_acervo
            )
    
    def pega_livro(self, filtro) -> Livro | None:    
        for livro in self.__livros:
            if filtro(livro):
                return livro 
