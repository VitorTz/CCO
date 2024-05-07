from src.entidade.usuario import Usuario
from src.entidade.item_acervo_usuario import ItemAcervoUsuario
from src.entidade.livro import Livro
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_item_carrinho import TelaItemCarrinho
from src.entidade.item_carrinho import ItemCarrinho
from src.dao.item_carrinho_dao import ItemCarrinhoDao
from typing import Dict, List, Callable, Set


class ControladorItemCarrinho(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__tela = TelaItemCarrinho()
        self.__dao = ItemCarrinhoDao()
    
    @property
    def tela(self) -> TelaItemCarrinho:
        return self.__tela 
    
    @property
    def dao(self) -> ItemCarrinhoDao:
        return self.__dao
    
    def limpa_carrinho(self, usuario: Usuario or None = None) -> None:
        """Limpa o carrinho do usuário"""
        usuario = self.controlador_sistema.controlador_usuario.usuario_logado if usuario is None else usuario
        self.dao.limpa_carrinho_usuario(usuario)
        self.tela.update_list_box(list(self.dict_entidades.keys()))
        self.tela.reset_desc_box()

    def get_carrinho_usuario(self, usuario: Usuario or None = None) -> Dict[str, ItemCarrinho]:
        """Retorna um dicionário contendo o carrinho do usuário"""
        usuario = self.controlador_sistema.controlador_usuario.usuario_logado if usuario is None else usuario
        return self.dao.get_carrinho_usuario(usuario)

    @property
    def dict_entidades(self) -> Dict:
        """Retorna o carrinho do usuário com cada item sendo identificado pelo titulo do livro"""
        carrinho: Dict[str, ItemCarrinho] = self.get_carrinho_usuario()
        return {
            item.item_acervo_usuario.livro.titulo: item for item in carrinho.values()
        }
    
    @property
    def btns(self) -> Dict[str, Callable]:
        """Retorna os botões que o controlador implementa"""
        b = {"Comprar": self.comprar} # Adiciona a opção de comprar ao controlador
        b.update(super().btns)
        return b
    
    def open_main_window(self) -> None:
        """Abre a janela principal do controlador"""
        self.tela.set_layout_main_window(
            list(self.dict_entidades.keys()),
            list(self.btns.keys()),
            size_list_box=(38, 20),
            size_desc_box=(35, 20)
        )

    def __escolhe_item_vendedor(self, livro: Livro) -> ItemAcervoUsuario:
        """Apresenta os vendedores disponíveis para o livro e retorna o item escolhido pelo usuário"""
        # Procura no acervo de cada usuário por itens que contenham o livro escolhido
        itens_acervo: List[ItemAcervoUsuario] = self.controlador_sistema.controlador_item_acervo_usuario.dao.get_itens_by_livro(livro)
        if itens_acervo:
            usuario_logado: Usuario = self.controlador_sistema.controlador_usuario.usuario_logado
            
            # A partir dos itens encontrados de cada vendedor que correspondem ao livro escolhido para compra
            # cria um dicionário com a identificação de cada vendedor e seu item
            # Não adiciona itens com 0 exemplares e que possuam ao usuário logado
            itens_disponiveis: Dict[str, ItemAcervoUsuario] = {
                f"Vendedor {n+1} - {item.valor} reais": item for n, item in enumerate(itens_acervo) if (item.vendedor.key != usuario_logado.key) and (item.exemplares > 0)
            }
            if itens_disponiveis:
                # Mostra os vendedores na tela e pede para o usuário escolher um
                item_escolhido: str = self.tela.get_vendedor_escolhido(livro.info, list(itens_disponiveis.keys()))
                if item_escolhido:
                    # Retorna o item do vendedor escolhido pelo usuário
                    return itens_disponiveis.get(item_escolhido)
            else:
                self.tela.popup("Nenhum vendedor encontrado!")    
        else:
            self.tela.popup("Nenhum vendedor encontrado!")

    def novo(self, retornar_entidade_criada: bool = False) -> None:
        """Adiciona um item ao carrinho do usuário"""
        #lista_titulos: List[str] = self.controlador_sistema.controlador_livro.dao.get_titulos()
        lista_titulos: Set[str] = self.controlador_sistema.controlador_item_acervo_usuario.dao.get_titulos_disponiveis(
            self.controlador_sistema.controlador_usuario.usuario_logado
        )
        # Apresenta os titulos e pede para o usuário escolher algum
        titulo_escolhido: str = self.tela.get_item_list_box(lista_titulos)
        
        if titulo_escolhido:
            # Pega a entidade Livro que corresponde ao titulo escolhido
            livro: Livro = self.controlador_sistema.controlador_livro.dao.get(lambda livro: livro.titulo == titulo_escolhido)
            self.tela.log(f"Livro {livro.titulo} escolhido!")
            # Conta uma view para o livro
            livro.views += 1
            # Mostra os vendedores que possuem o livro escolhido e pede para o usuário escolher um
            item_acervo_escolhido: ItemAcervoUsuario or None = self.__escolhe_item_vendedor(livro)
            if item_acervo_escolhido:
                # Continua o cadastro com o item de um vendedor especifico escolhido 
                item_carrinho: ItemCarrinho = ItemCarrinho(
                    item_acervo_escolhido,
                    comprador=self.controlador_sistema.controlador_usuario.usuario_logado,
                    quantidade=1
                )
                # Adiciona o item escolhido ao carrinho do usuário logado
                self.dao.add(item_carrinho, self.controlador_sistema.controlador_usuario.usuario_logado)
                self.tela.update_list_box(list(self.dict_entidades.keys()))
                self.tela.popup(f"Item {item_carrinho.item_acervo_usuario.livro.titulo} adicionado com sucesso ao carrinho!")

    def editar(self, entidade_selecionada: ItemCarrinho) -> None:
        """Altera a quantidade de um item no carrinho"""
        if entidade_selecionada:
            quantidade = self.tela.get_quantidade_item_carrinho()
            if quantidade:
                try:
                    entidade_selecionada.quantidade = quantidade
                except Exception as e:
                    self.tela.popup(e)
                else:
                    super().editar(entidade_selecionada)

    def comprar(self, *args) -> None:
        """Realiza a compra dos itens do carrinho"""
        self.controlador_sistema.controlador_compra.novo()
