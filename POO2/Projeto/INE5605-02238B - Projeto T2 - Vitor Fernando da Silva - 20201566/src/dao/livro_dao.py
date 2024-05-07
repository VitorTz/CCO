from src.dao.abstract_dao import AbstractDAO
from src.entidade.livro import Livro
from pathlib import Path
from typing import List, Dict


class LivroDAO(AbstractDAO):

    def __init__(self) -> None:
        super().__init__(datasource=Path("db/livro.pkl"))
    
    @property
    def entidade(self) -> Livro:
        return Livro 
    
    def get_titulos(self) -> List[str]:
        """Retorna uma lista com os titulos de cada livro no acervo"""
        return [livro.titulo for livro in self.get_all()]
    
    def get_dict_titulo_livro(self) -> Dict[str, Livro]:
        """Retorna um dicionário com o par <titulo, Livro>"""
        return {
            livro.titulo: livro for livro in self.get_all()
        }

    def get_all(self) -> List[Livro]:
        return super().get_all()
    