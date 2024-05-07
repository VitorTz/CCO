from __future__ import annotations
from typing import TYPE_CHECKING, Callable, Dict, List
if TYPE_CHECKING:
    from src.controle.controlador_sistema import ControladorSistema

from time import sleep
from src.limite.abstract_tela import AbstractTela
from src.dao.abstract_dao import AbstractDAO
from abc import ABC, abstractmethod


class ErroGraveException(Exception):

    def __init__(self, e) -> None:
        super().__init__(f"ERRO GRAVE -> {e}")


class AbstractControlador(ABC):

    @abstractmethod
    def __init__(self, controlador_sistema: ControladorSistema) -> None:
        super().__init__()
        self.__controlador_sistema = controlador_sistema
    
    @property
    @abstractmethod
    def dao(self) -> AbstractDAO:
        pass 

    @property
    @abstractmethod
    def tela(self) -> AbstractTela:
        pass 

    @property
    def controlador_sistema(self) -> ControladorSistema:
        return self.__controlador_sistema
    
    @property
    def dict_entidades(self) -> Dict:
        """Retorna um dicionário com as entidades do controlador"""
        return self.dao.cache
    
    @property
    def btns(self) -> Dict[str, Callable]:
        """Retorna um dicionário com os botões que a tela do controlador deve
        apresentar e os métodos relacionados a eles"""
        return {
            "Novo": self.novo,
            "Editar": self.editar,
            "Deletar": self.deletar,
            "Selecionar": self.selecionar,
            "Pesquisar": self.pesquisar,
            "Cancelar": None
        }

    def wait(self, time: float = 3) -> None:
        sleep(time)
    
    # Deve ser implementado para cada controlador
    @abstractmethod
    def novo(self, retornar_entidade_criada: bool = False) -> None:
        """Cria e adiciona uma nova entidade ao controlador"""
        pass 
    
    # Deve ser implementado para cada controlador
    @abstractmethod
    def editar(self, entidade_selecionada: object) -> None:
        if entidade_selecionada:
            # Salva as entidades, atualiza a descrição da entidade
            # caixa de texto ao lado da listbox da janela principal
            # e abre um popup pra avisar o sucesso da alteração
            self.dao.dump()
            self.tela.reset_desc_box(entidade_selecionada.info) 
            self.tela.popup(f"Entidade {entidade_selecionada.key} alterada com sucesso!")

    def deletar(self, entidade_selecionada: object) -> None:
        """Deleta uma entidade pertencente ao controlador"""
        if entidade_selecionada:
            self.tela.log(f"Removendo entidade {entidade_selecionada.key}")
            self.dao.remove(entidade_selecionada)
            self.tela.log(f"Entidade {entidade_selecionada.key} removida com sucesso!")
            self.tela.reset_desc_box()  # Reseta a descrição da entidade selecionada para o texto padrão
            self.tela.update_list_box(list(self.dict_entidades.keys()))  # Atualiza a listbox da janela principal
            self.tela.popup(f"Entidade {entidade_selecionada.key} removida com sucesso!")
        else:
            self.tela.popup("Selecione uma entidade para deletar, por favor.")
    
    def selecionar(self, entidade_selecionada: object) -> None:
        """Mostra as informações da entidade na caixa de texto da janela principal"""
        if entidade_selecionada:
            # Mostra as informações da entidade na caixa de texto ao lado da listbox da janela principal
            self.tela.reset_desc_box(entidade_selecionada.info)
        else:
            self.tela.popup("Selecione uma entidade, por favor.")

    def pesquisar(self, *args) -> None:
        """Pede para o usuário pesquisar uma entidade e ordena a list box
        com base no termo pesquisado"""
        def check(key_entidade: str, termpo_pesquisado: str) -> int:
            """Retorna o número de semelhanças entre as duas strings recebidas"""
            key_entidade = str(key_entidade)
            semelhancas: int = 0
            comparar: bool = False
            for l1, l2 in zip(key_entidade.lower().replace(" ", ""), termpo_pesquisado.lower().replace(" ", "")):
                if not comparar and l1 == l2:
                    comparar = True
                if comparar and l1 == l2:
                    semelhancas += 1
            return semelhancas

        termo_pesquisa: str = self.tela.get_termo_pesquisa()
        
        if termo_pesquisa:
            self.tela.log(f"Termo pesquisado = {termo_pesquisa}")
            lista_keys: List[str or int] = list(self.dict_entidades.keys())            
            # Ordena a lista de entidades mostradas na tela com base nas semelhanças 
            # com o termo pesquisado
            lista_keys.sort(key=lambda entidade: check(termo_pesquisa, entidade), reverse=True)
            self.tela.update_list_box(lista_keys)
            self.tela.log("Ordem da Listbox alterada")

    def __get_entidade_escolhida(self, list_box_values: List) -> str:
        """Retorna a entidade selecionada pelo usuário na listbox"""
        try:
            return self.dict_entidades.get(list_box_values[0])
        except Exception as e:
            self.tela.log(f"Erro ao pegar entidade escolhida pelo usuário. {e}")

    def __open_main_window(self) -> None:
        self.tela.set_layout_main_window(
            list(self.dict_entidades.keys()),
            list(self.btns.keys())
        )

    def main(self) -> None:
        self.__open_main_window()

        while True:
            event, values = self.tela.read_janela_principal()
            if event in ("Cancelar", None):
                self.tela.close_janela_principal()
                break
            else:
                entidade_escolhida = self.__get_entidade_escolhida(values["-LISTBOX-"])
                try:
                    self.tela.log(f"Executando método relacionado ao botão {event}")
                    self.btns.get(event)(entidade_escolhida)
                except ErroGraveException as e:
                    self.tela.close_janela_principal()
                    self.tela.close_janela_secundaria()
                    self.tela.popup(e)
                    break
                except Exception as e:
                    self.tela.log(e)


