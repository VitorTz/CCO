from abc import ABC, abstractmethod
from enum import Enum, auto


class TipoMensagem(Enum):

    TITULO = auto()
    OPCAO = auto()
    PERGUNTA = auto()
    AVISO = auto()


class NumeroInvalidoException(Exception):

    def __init__(self, numero: str) -> None:
        super().__init__(f"O valor {numero} deve ser um número inteiro e positivo")


class RespostaInvalidaException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(f"Digite uma resposta válida, por favor.")


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.__tipo_msg = {
            TipoMensagem.TITULO: {"symbol": "\u058D", "indent": ' ' * 4},
            TipoMensagem.OPCAO: {"symbol": "\u0F1A", "indent": ' ' * 6},
            TipoMensagem.PERGUNTA: {"symbol": "\u2BC0", "indent": ' ' * 4},
            TipoMensagem.AVISO: {"symbol": "\u26A0", "indent": ' ' * 4}
        }

    def limpa_terminal(self) -> None:
        print("\x1b[2J\x1b[1;1H", end="\n\n")

    def valida_numero(self, numero: str):
        if not numero.isdigit():
            raise NumeroInvalidoException()
    
    def mostra_msg(self, msg: str | Exception, tipo_msg: TipoMensagem = TipoMensagem.OPCAO, end="\n") -> None:
        if isinstance(msg, Exception):
            tipo_msg = TipoMensagem.AVISO
        
        indent = self.__tipo_msg[tipo_msg]['indent']
        symbol = self.__tipo_msg[tipo_msg]['symbol']
        
        print(f"{indent}{symbol} {msg}", end=end)
    
    def mostra_msg_dict(self, msg: dict, tipo_msg: TipoMensagem = TipoMensagem.OPCAO):
        for k, v in msg.items():
            self.mostra_msg(f"{k} - {v}", tipo_msg=tipo_msg)
        
    def mostra_msg_lista(self, msg: list, tipo_msg: TipoMensagem = TipoMensagem.OPCAO):
        for i in msg:
            self.mostra_msg(i, tipo_msg=tipo_msg)

    def mostra_info_livro(self, *info_livro: dict):
        for livro in info_livro:            
            for k, v in livro.items():
                if k != "vendedores":
                    self.mostra_msg(f"{k} - {v}")

    def pega_resposta(self, opcoes: dict, msg: str = "Escolha um número válido: "):
        self.mostra_msg(msg, tipo_msg=TipoMensagem.TITULO)
        self.mostra_msg_dict(opcoes)
        
        resposta = self.pega_info_usuario("Digite sua resposta: ")
        if resposta not in opcoes.keys():
            raise RespostaInvalidaException()
        
        return resposta
    
    def pega_info_usuario(self, msg: str, *validacoes) -> str:
        """
        Pega alguma informação do usuário, também faz algumas validações com a resposta
        Validações podem levantar alguma exceção caso a resposta não seja a esperada 
        pelo sistema
        """
        self.mostra_msg(msg, tipo_msg=TipoMensagem.PERGUNTA ,end="")
        resposta = input().strip()
        [validacao(resposta) for validacao in validacoes]
        
        return resposta 