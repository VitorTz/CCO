from src.controle.controlador_usuario import ControladorUsuario
from src.controle.controlador_item_acervo_usuario import ControladorItemAcervoUsuario
from src.controle.controlador_livro import ControladorLivro
from src.controle.controlador_item_carrinho import ControladorItemCarrinho
from src.controle.controlador_compra import ControladorCompra
from src.controle.controlador_relatorio import ControladorRelatorio
from src.limite.tela_sistema import TelaSistema
from typing import Dict 


class ControladorSistema:

    def __init__(self) -> None:
        self.__tela = TelaSistema()
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_livro = ControladorLivro(self)
        self.__controlador_item_acervo_usuario = ControladorItemAcervoUsuario(self)
        self.__controlador_item_carrinho = ControladorItemCarrinho(self)
        self.__controlador_compra = ControladorCompra(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__esta_executando: bool = True 
    
    @property
    def esta_executando(self) -> bool:
        return self.__esta_executando
    
    @esta_executando.setter
    def esta_executando(self, esta_executando: bool):
        self.__esta_executando = esta_executando

    @property
    def controlador_usuario(self) -> ControladorUsuario:
        return self.__controlador_usuario
    
    @property
    def controlador_livro(self) -> ControladorLivro:
        return self.__controlador_livro
    
    @property
    def controlador_item_acervo_usuario(self) -> ControladorItemAcervoUsuario:
        return self.__controlador_item_acervo_usuario
    
    @property
    def controlador_item_carrinho(self) -> ControladorItemCarrinho:
        return self.__controlador_item_carrinho
    
    @property
    def controlador_compra(self) -> ControladorCompra:
        return self.__controlador_compra
    
    @property
    def __opcoes(self) -> Dict[str, str]:
        return {
            "Gerenciar livros": self.controlador_livro.main,
            "Gerenciar meus livros": self.controlador_item_acervo_usuario.main,
            "Gerenciar usuários": self.controlador_usuario.main,
            "Gerenciar minhas compras": self.controlador_compra.main,
            "Carrinho": self.controlador_item_carrinho.main,
            "Relatorio": self.__controlador_relatorio.main
        }

    def __main(self) -> None:
        event, values = self.__tela.pega_opcao(
            list(self.__opcoes.keys()),
            self.controlador_usuario.usuario_logado.email
        )
        if event in ("Cancelar", None):
            self.__encerra_programa()
        elif event == "Escolher":
            opcao_escolhida = [k for k, v in values.items() if v is True]
            if opcao_escolhida:
                self.__opcoes[opcao_escolhida[0]]()

    def __encerra_programa(self) -> None:
        self.esta_executando = False

    def run(self) -> None:
        while self.esta_executando:
            if self.controlador_usuario.usuario_logado is None:
                self.controlador_usuario.acesso_sistema()
            else:
                try:
                    self.__main() 
                except Exception as e:
                    self.__tela.log(e)
            
            