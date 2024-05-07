from src.dao.abstract_dao import AbstractDAO
from src.entidade.usuario import Usuario
from typing import List
from pathlib import Path


class UsuarioDAO(AbstractDAO):

    def __init__(self) -> None:
        super().__init__(datasource=Path("db/usuario.pkl"))
    
    @property
    def entidade(self) -> object:
        return Usuario
    
    def get_list_keys(self) -> List:
        return super().get_list_keys(key=lambda usuario: usuario.email)