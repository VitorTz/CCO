from src.entidade.item_acervo_usuario import ItemAcervoUsuario
from src.entidade.item_carrinho import ItemCarrinho
from src.entidade.compra import Compra
from src.dao.compra_dao import CompraDAO
from src.limite.tela_compra import TelaCompra
from src.controle.abstract_controlador import AbstractControlador
from random import randint
from typing import Dict


class ControladorCompra(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__tela = TelaCompra()
        self.__dao = CompraDAO()
    
    @property
    def tela(self) -> TelaCompra:
        return self.__tela 
    
    @property
    def dao(self) -> CompraDAO:
        return self.__dao 
    
    @property
    def dict_entidades(self) -> Dict[int, Compra]:
        return self.dao.get_compras_usuario(
            self.controlador_sistema.controlador_usuario.usuario_logado
        )

    def __get_id_compra(self) -> int:
        """Retorna um id único para uma nova compra"""
        while True:
            id = randint(1, 6666666666)
            if not self.dao.get(lambda compra: compra.id == id):
                return id
        
    def __retira_itens_comprados_acervo_vendedores(self, compra: Compra) -> None:
        """Retira os itens comprados do acervo de cada vendedor contido na compra"""
        self.tela.log("Alterando acervo dos usuários contidos na compra")
        for item_carrinho in compra.itens_carrinho:
            self.tela.log(f"Item carrinho = {item_carrinho.key}")
            self.tela.log(f"Item acervo = {item_carrinho.item_acervo_usuario.livro.titulo}")
            self.tela.log(f"Exemplares antes da compra = {item_carrinho.item_acervo_usuario.exemplares}")
            item_carrinho.item_acervo_usuario.exemplares -= item_carrinho.quantidade
            self.tela.log(f"Exemplares após a compra = {item_carrinho.item_acervo_usuario.exemplares}")
        # Salva as alterações
        self.controlador_sistema.controlador_item_acervo_usuario.dao.dump()

    def novo(self, *args) -> None:
        # Pega o carrinho do usuário
        itens_carrinho: Dict[str, ItemCarrinho] = self.controlador_sistema.controlador_item_carrinho.get_carrinho_usuario()
        if itens_carrinho:
            self.tela.log(f"Processando a compra...")
            compra = Compra(
                self.__get_id_compra(),
                itens_carrinho=list(itens_carrinho.values()),  
                comprador=self.controlador_sistema.controlador_usuario.usuario_logado  
            )
            # Retira os itens comprados do acervo de cada vendedor contido na compra
            self.__retira_itens_comprados_acervo_vendedores(compra)
            self.dao.add(compra)
            self.controlador_sistema.controlador_item_carrinho.limpa_carrinho()
            self.tela.update_list_box(list(self.dict_entidades.keys()))
            self.tela.popup("Compra concluida!")
        else:
            self.tela.popup("Seu carrinho está vazio!")
    
    def editar(self, entidade_selecionada: Compra) -> None:
        self.tela.popup("Não é possível editar uma compra fechada")
