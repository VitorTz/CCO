

class Usuario:

    def __init__(
        self, 
        id: str,
        nome: str,
        primeiro_nome: str,
        email: str,
        senha: str,
        estado: str,
        cidade: str,
        bairro: str,
        cep: str,
        logradouro: str,
        numero_residencia: str,
        complemento: str,
        acervo: dict
    ) -> None:
        self.__id = id 
        self.__nome = nome 
        self.__primeiro_nome = primeiro_nome 
        self.__email = email 
        self.__senha = senha 
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__cep = cep
        self.__logradouro = logradouro
        self.__numero_residencia = numero_residencia
        self.__complemento = complemento
        self.__acervo = acervo
    
    @property
    def info_completa(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "primeiro_nome": self.primeiro_nome,
            "email": self.email,
            "senha": self.senha,
            "estado": self.estado,
            "cidade": self.cidade,
            "bairro": self.bairro,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "numero_residencia": self.numero_residencia,
            "complemento": self.complemento,
            "acervo": self.acervo
        }
    
    @property
    def info_endereco(self) -> dict:
        return {
            "estado": self.estado,
            "cidade": self.cidade,
            "bairro": self.bairro,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "numero_residencia": self.numero_residencia,
            "complemento": self.complemento
        }
    
    @property
    def id(self) -> str:
        return self.__id 
    
    @property
    def nome(self) -> str:
        return self.__nome 
    
    @property
    def primeiro_nome(self) -> str:
        return self.__primeiro_nome
    
    @property
    def email(self) -> str:
        return self.__email 

    @property
    def senha(self) -> str:
        return self.__senha
    
    @property
    def estado(self) -> str:
        return self.__estado
    
    @property
    def cidade(self) -> str:
        return self.__cidade
    
    @property
    def bairro(self) -> str:
        return self.__bairro
    
    @property
    def cep(self) -> str:
        return self.__cep 
    
    @property
    def logradouro(self) -> str:
        return self.__logradouro
    
    @property
    def numero_residencia(self) -> str:
        return self.__numero_residencia
    
    @property
    def complemento(self) -> str:
        return self.__complemento
    
    @property
    def acervo(self) -> dict:
        return self.__acervo