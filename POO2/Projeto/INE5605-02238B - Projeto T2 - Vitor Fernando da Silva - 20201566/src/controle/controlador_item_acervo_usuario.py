from src.entidade.usuario import Usuario
from src.controle.abstract_controlador import AbstractControlador
from src.entidade.item_acervo_usuario import ItemAcervoUsuario
from src.entidade.livro import Livro
from src.dao.item_acervo_usuario_dao import ItemAcervoUsuarioDao
from src.limite.tela_item_acervo_usuario import TelaItemAcervoUsuario
from typing import Dict 


class ControladorItemAcervoUsuario(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__tela = TelaItemAcervoUsuario()
        self.__dao = ItemAcervoUsuarioDao()
    
    @property
    def tela(self) -> TelaItemAcervoUsuario:
        return self.__tela

    @property
    def dao(self) -> ItemAcervoUsuarioDao:
        return self.__dao 

    @property
    def dict_entidades(self) -> Dict:
        """Retorna um dicionário com os itens do acervo do usuário identificados
        pelo titulo do livro"""
        itens: Dict[str, ItemAcervoUsuario] = self.dao.get_itens_vendedor(
            self.controlador_sistema.controlador_usuario.usuario_logado.key
        )
        return {
            item.livro.titulo: item for item in itens.values()
        }

    def deleta_itens_acervo_usuario(self, usuario: Usuario) -> None:
        """Deleta todos os itens do acervo do usuário"""
        self.dao.deleta_itens_usuario(usuario)

    def __pega_livro_para_adicionar(self) -> Livro or None:
        # Escolhe se quer adicionar um livro que já existe no acervo geral
        # ou um novo livro
        # Se escolher um novo livro o sistema vai adicionar o livro no acervo geral
        # antes de retornar o livro criado
        forma_cadastro: str = self.tela.pega_forma_cadastro()
        if forma_cadastro == "Escolher livro acervo geral":
            return self.controlador_sistema.controlador_livro.get_livro_escolhido_na_listbox()
        elif forma_cadastro == "Novo livro":
            return self.controlador_sistema.controlador_livro.novo(retornar_entidade_criada=True)

    def novo(self, retornar_entidade_criada: bool = False) -> None:
        """Adiciona um novo item ao acervo do usuário logado"""
        # Pega um livro do acervo geral para compor o item no acervo do usuário
        livro: Livro or None = self.__pega_livro_para_adicionar()
        if livro:
            # Verifica se o livro já faz parte do acervo do usuário
            item_acervo: ItemAcervoUsuario or None = self.dao.get_by_key(
                self.controlador_sistema.controlador_usuario.usuario_logado.key,
                livro.key
            )
            if item_acervo:
                self.tela.popup(f"Item {item_acervo.livro.titulo} já cadastrado em seu acervo!")
            else:
                self.tela.log(f"Livro a ser adicionado ao acervo do usuário = {livro.titulo}")
                info_cadastro: Dict[str, str] or None = self.tela.pega_valores_cadastro()
                if info_cadastro:
                    item_acervo = ItemAcervoUsuario(
                        livro,
                        self.controlador_sistema.controlador_usuario.usuario_logado,
                        info_cadastro["exemplares"],
                        info_cadastro["valor"]
                    )
                    self.dao.add(item_acervo)
                    self.tela.update_list_box(list(self.dict_entidades.keys()))
                    self.tela.log(f"Item {item_acervo.livro.titulo} criado com sucesso!")
                    self.tela.popup(f"Item {item_acervo.livro.titulo} adicionado a seu acervo com sucesso!")

            if retornar_entidade_criada:
                return item_acervo
            
    def editar(self, entidade_selecionada: ItemAcervoUsuario) -> None:
        if entidade_selecionada:
            # Pega e valida os dados necesários para alterar a entidade
            info_cadastro: Dict[str, str] = self.tela.pega_valores_cadastro()
            if info_cadastro:
                # Se os dados foram retornados então são válidos
                self.tela.log(f"Alterando valores de {entidade_selecionada.livro.titulo}")
                entidade_selecionada.exemplares = info_cadastro["exemplares"] 
                entidade_selecionada.valor = info_cadastro["valor"]
                super().editar(entidade_selecionada)
        else:
            self.tela.popup("Selecione um item para editar.")