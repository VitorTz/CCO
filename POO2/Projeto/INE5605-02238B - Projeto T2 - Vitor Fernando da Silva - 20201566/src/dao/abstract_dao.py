import pickle
from abc import ABC, abstractmethod
from typing import Callable, Dict, List
from pathlib import Path
from src.entidade.abstract_entidade import AbstractEntidade


class AbstractDAO(ABC):

    @abstractmethod
    def __init__(self, datasource: Path) -> None:
        super().__init__()
        self.__datasource: Path = datasource
        self.__cache: Dict = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.dump()
            
    @property
    @abstractmethod
    def entidade(self) -> AbstractEntidade:
        """Identifica a entidade que deve compor o self.__cache"""
        pass

    def dump(self) -> None:
        with open(self.__datasource, "wb") as file:
            pickle.dump(self.__cache, file)
    
    def __load(self) -> None:
        with open(self.__datasource, "rb") as file:
            self.__cache = pickle.load(file)
        
    @property
    def cache(self) -> Dict:
        return self.__cache
    
    def get_by_key(self, key) -> object:
        return self.cache.get(key)
    
    def get(self, validacao: Callable) -> object:
        """Retorna um objeto que corresponda a uma validação específica"""
        for obj in self.__cache.values():
            try:
                if validacao(obj):
                    return obj  
            except:
                pass 
    
    def add(self, obj: object):
        if isinstance(obj, self.entidade): # Verifica se a entidade está correta
            self.cache[obj.key] = obj 
            self.dump()
    
    def remove(self, entidade = None, key = None):
        if isinstance(entidade, self.entidade):
            key = entidade.key
        try:
            del self.__cache[key]
        except KeyError:
            pass
        else:
            self.dump()
    
    def get_all(self) -> List:
        return [obj for obj in self.__cache.values()]
