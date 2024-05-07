from src.entidade.usuario import Usuario
from src.entidade.usuario import Usuario
from src.dao.abstract_dao import AbstractDAO
from src.entidade.item_carrinho import ItemCarrinho
from typing import Dict
from pathlib import Path


class ItemCarrinhoDao(AbstractDAO):

    def __init__(self) -> None:
        super().__init__(datasource=Path("db/item_carrinho.pkl"))
    
    @property
    def entidade(self) -> ItemCarrinho:
        return ItemCarrinho

    def get_carrinho_usuario(self, usuario: Usuario) -> Dict[str, ItemCarrinho]:
        return self.cache.get(usuario.key, {})
    
    def limpa_carrinho_usuario(self, usuario: Usuario) -> None:
        self.get_carrinho_usuario(usuario).clear()
        self.dump()

    def add(self, item: ItemCarrinho, usuario: Usuario) -> None:
        """Adiciona o item ao carrinho do usuário"""
        itens_usuario: Dict[str, ItemCarrinho] = self.get_carrinho_usuario(usuario)
        itens_usuario[item.key] = item 
        self.cache[usuario.key] = itens_usuario
        self.dump()
    
    def remove(self, item: ItemCarrinho) -> None:
        try:
            del self.get_carrinho_usuario(item.comprador)[item.key]
        except:
            pass 
        else:
            self.dump()
    
        