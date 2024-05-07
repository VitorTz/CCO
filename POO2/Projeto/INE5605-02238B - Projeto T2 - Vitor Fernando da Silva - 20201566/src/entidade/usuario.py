from src.entidade.abstract_entidade import AbstractEntidade
from typing import Dict


class Usuario(AbstractEntidade):

    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        senha: str,
        estado: str,
        cidade: str,
        bairro: str,
        rua: str,
        cep: str,
        numero_residencia: str
    ) -> None:
        self.id = id 
        self.nome = nome 
        self.email = email 
        self.senha = senha 
        self.estado = estado 
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua 
        self.cep = cep 
        self.numero_residencia = numero_residencia
        super().__init__()

    @property
    def info_entidade(self) -> Dict[str, str]:
        return {
                "id": self.id,
                "nome": self.nome,
                "email": self.email,
                "senha": self.senha,
                "estado": self.estado,
                "cidade": self.cidade,
                "bairro": self.bairro,
                "rua": self.rua,
                "cep": self.cep,
                "numero_residencia": self.numero_residencia
            }

    @property
    def key(self) -> str:
        return self.email
    
    @property
    def id(self) -> int:
        return self.__id 
    
    @id.setter
    def id(self, id: int):
        self.__id = id 
    
    @property
    def nome(self) -> str:
        return self.__nome 
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.title().strip()
    
    @property
    def email(self) -> str:
        return self.__email 
    
    @email.setter
    def email(self, email: str):
        self.__email = email.strip().lower()
    
    @property
    def senha(self) -> str:
        return self.__senha 
    
    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha.strip()
    
    @property
    def estado(self) -> str:
        return self.__estado 
    
    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado
    
    @property
    def cidade(self) -> str:
        return self.__cidade 
    
    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def bairro(self) -> str:
        return self.__bairro 
    
    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro
    
    @property
    def rua(self) -> str:
        return self.__rua 
    
    @rua.setter
    def rua(self, rua: str):
        self.__rua = rua 
    
    @property
    def cep(self) -> str:
        return self.__cep 
    
    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep 
    
    @property
    def numero_residencia(self) -> str:
        return self.__numero_residencia
    
    @numero_residencia.setter
    def numero_residencia(self, numero_residencia: str):
        self.__numero_residencia = numero_residencia
        