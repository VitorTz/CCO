from src.entidade.usuario import Usuario
from src.dao.abstract_dao import AbstractDAO
from src.entidade.livro import Livro
from src.entidade.item_acervo_usuario import ItemAcervoUsuario
from typing import Dict, List, Set
from pathlib import Path


class ItemAcervoUsuarioDao(AbstractDAO):

    def __init__(self) -> None:
        super().__init__(datasource=Path("db/item_acervo.pkl"))
    
    @property
    def entidade(self) -> ItemAcervoUsuario:
        return ItemAcervoUsuario

    def get_titulos_disponiveis(self, usuario_logado: Usuario) -> List[str]:
        """Retorna os titulos dos itens validos para compra"""
        titulos: Set[str] = set()
        self.cache: Dict[str, Dict[str, ItemAcervoUsuario]]
        for key, itens in self.cache.items():
            itens: Dict[str, ItemAcervoUsuario]
            if key != usuario_logado.key:
                for item in itens.values():
                    if item.exemplares > 0:
                        titulos.add(item.livro.titulo)
        return list(titulos)

    def get_itens_vendedor(self, key_vendedor) -> Dict[str, ItemAcervoUsuario]:
        return self.cache.get(key_vendedor, {})

    def get_by_key(self, key_vendedor, key_item) -> object:
        return self.get_itens_vendedor(key_vendedor).get(key_item)
    
    def add(self, item: ItemAcervoUsuario) -> None:
        itens_vendedor: Dict[str, ItemAcervoUsuario] = self.get_itens_vendedor(item.vendedor.key)
        itens_vendedor[item.key] = item 
        self.cache[item.vendedor.key] = itens_vendedor
        self.dump()
    
    def remove(self, item: ItemAcervoUsuario) -> None:
        try:
            del self.get_itens_vendedor(item.vendedor.key)[item.key]
        except:
            pass 
        else:
            self.dump()
        
    def deleta_itens_usuario(self, usuario: Usuario) -> None:
        """Deleta todos os itens de um usuario"""
        try:
            del self.cache[usuario.key]
        except:
            pass 
        else:
            self.dump()
    
    def get_itens_by_livro(self, livro: Livro) -> List[ItemAcervoUsuario]:
        """Retorna todos os itens que possuem determinado livro"""
        itens: List[ItemAcervoUsuario] = []
        for itens_vendedor in self.cache.values():
            itens_vendedor: Dict[str, ItemAcervoUsuario]
            for item in itens_vendedor.values():
                if item.livro.key == livro.key:
                    itens.append(item)
        return itens
