from calendar import c
from src.entidade.usuario import Usuario
from src.dao.abstract_dao import AbstractDAO
from src.entidade.compra import Compra
from typing import Dict, List
from pathlib import Path


class CompraDAO(AbstractDAO):

    def __init__(self) -> None:
        super().__init__(datasource=Path("db/compra.pkl"))
    
    @property
    def entidade(self) -> Compra:
        return Compra
    
    def get_compras_usuario(self, usuario: Usuario) -> Dict[int, Compra]:
        return self.cache.get(usuario.key, {})

    def add(self, compra: Compra) -> None:
        self.cache: Dict[str, Dict[int, Compra]]
        itens_usuario: Dict[int, Compra] = self.get_compras_usuario(compra.comprador)   
        itens_usuario[compra.key] = compra
        self.cache[compra.comprador.key] = itens_usuario
        self.dump()
    
    def remove(self, compra: Compra) -> None:
        try:
            del self.get_compras_usuario(compra.comprador)[compra.key]
        except:
            pass 
        else:
            self.dump()
        
    def get_todas_compras(self) -> List[Compra]:
        """Retorna uma lista com todas as compras"""
        todas_compras: List[Compra] = []
        for _, compras in self.cache.items():
            compras: Dict[str, Compra]
            for compra in compras.values():
                todas_compras.append(compra)
        return todas_compras