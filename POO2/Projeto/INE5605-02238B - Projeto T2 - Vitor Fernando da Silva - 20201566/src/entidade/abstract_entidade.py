from abc import ABC, abstractmethod
from typing import Dict


class AbstractEntidade(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
    
    @property
    @abstractmethod
    def key(self) -> object:
        """Deve setar a key que identifica a entidade no cache da entidade DAO"""
        pass 

    @property
    @abstractmethod
    def info_entidade(self) -> Dict[str, str]:
        pass 

    @property
    def info(self) -> str:
        """Retorna as informações da entidade em forma de string"""
        msg = ""
        for k, v in self.info_entidade.items():
            msg += f"{k} -> {v}\n"
        return msg 

