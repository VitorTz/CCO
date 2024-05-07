from re import search
from src.limite.abstract_tela import AbstractTela


class EmailInvalidoException(Exception):

    def __init__(self, email: str) -> None:
        super().__init__(f"O email {email} é inválido.")


class SenhaInvalidaException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__("Senha inválida.")


class CepInvalidoException(Exception):

    def __init__(self, cep: str) -> None:
        super().__init__(f"Cep {cep} inválido.")


class CepNaoEncontradoException(Exception):

    def __init__(self, cep: str) -> None:
        super().__init__(f"Cep {cep} não encontrado.")


class NumeroResidenciaInvalidoException(Exception):

    def __init__(self, numero: str) -> None:
        super().__init__(f"Número de residencia {numero} inválido.")


class TelaCadastroNovoUsuario(AbstractTela):

    def __init__(self) -> None:
        super().__init__()
    
    def __valida_senha(self, senha: str):
        if not (senha.isdigit() and len(senha) >= 8):
            raise SenhaInvalidaException()

    def __valida_cep(self, cep: str):
        if not (cep.isdigit() and len(cep) == 8):
            raise CepInvalidoException(cep)

    def __valida_numero_residencia(self, numero: str):
        if not numero.isdigit():
            raise NumeroResidenciaInvalidoException(numero)

    def pega_email(self) -> str:
        return self.pega_info_usuario("Email: ")
        
    def pega_senha(self) -> str:
        return self.pega_info_usuario(
            "Senha (apenas digitos e no mínimo 8 digitos): ",
            self.__valida_senha
        )
    
    def pega_cep(self) -> str:
        return self.pega_info_usuario(
            "Cep (apenas números, precisa ser um cep existente): ",
            self.__valida_cep
        )
    
    def pega_numero_residencia(self) -> str:
        return self.pega_info_usuario(
            "Número residência: ",
            self.__valida_numero_residencia
        )
