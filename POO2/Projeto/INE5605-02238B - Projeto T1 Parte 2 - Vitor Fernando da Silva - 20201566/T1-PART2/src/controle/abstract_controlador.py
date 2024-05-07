from abc import ABC, abstractmethod
from src.controle.tipo_pagina import TipoPagina
from src.limite.abstract_tela import AbstractTela, TipoMensagem
from pathlib import Path
from time import sleep
import json


class AbstractControlador(ABC):

    @abstractmethod
    def __init__(
        self, 
        controlador_sistema,
        opcoes: dict = {}, 
        nome_controlador: str = ""
    ) -> None:
        super().__init__()
        self.__controlador_sistema = controlador_sistema
        self.__nome_controlador = nome_controlador
        self.__opcoes = opcoes
        
        # Adiciona opção de voltar para a página Home
        if nome_controlador not in ("Home", "Acesso", "Login", "Cadastro de usuários"):
            self.__opcoes[str(len(self.__opcoes)+1)] = {
                "desc": "Abrir página Home",
                "metodo": self.__abrir_pagina_home
            }
        
        # Adiciona opção de voltar para a página anterior
        self.__opcoes[str(len(self.__opcoes)+1)] = {
            "desc": "Voltar",
            "metodo": self.controlador_sistema.voltar
        }
        self.__opcoes[str(len(self.__opcoes)+1)] = {
            "desc": "Logout",
            "metodo": self.controlador_sistema.logout
        }
        # Adicona opção de sair do programa
        self.__opcoes[str(len(self.__opcoes)+1)] = {
            "desc": "Sair",
            "metodo": self.controlador_sistema.sair
        }
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def nome_controlador(self) -> str:
        return self.__nome_controlador
    
    @property
    @abstractmethod
    def tela(self) -> AbstractTela:
        return self.__tela
    
    def __abrir_pagina_home(self) -> None:
        """Troca página atual para a Home"""
        self.controlador_sistema.troca_pagina(TipoPagina.HOME)
    
    def le_json(self, path: str | Path) -> object:
        with open(path, "r") as file:
            return json.load(file)
        
    def salva_json(self, obj: object, path: str | Path) -> None:
        with open(path, "w") as file:
            json.dump(obj, file, indent=2)
        
    def wait(self, time: int = 4):
        sleep(time)

    def main(self) -> None:
        while True:
            # Identifica a página atual e pede para o usuário
            # escolher uma opção válida
            self.tela.limpa_terminal()
            self.tela.mostra_msg(
                f"Você está na página {self.__nome_controlador}", 
                tipo_msg=TipoMensagem.TITULO
                )
            try:
                # Opção = metódo do controlador que deve ser executado
                opcoes = {n: opcao["desc"] for n, opcao in self.__opcoes.items()}
                opcao_para_executar = self.tela.pega_resposta(opcoes)
                self.__opcoes[opcao_para_executar]["metodo"]()
            except Exception as e:
                self.tela.mostra_msg(e)
                self.wait()
            else:
                break
            