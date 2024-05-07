from src.controle.controlador_compra import ControladorCompra
from src.controle.abstract_controlador import AbstractControlador
from src.controle.controlador_relatorio import ControladorRelatorio
from src.controle.controlador_carrinho import ControladorCarrinho
from src.controle.controlador_acervo_usuario import ControladorAcervoUsuario
from src.controle.controlador_pesquisa_livro import ControladorPesquisaLivro
from src.controle.controlador_cadastra_livro import ControladorCadastraLivro
from src.controle.controlador_minha_conta import ControladorMinhaConta
from src.controle.tipo_pagina import TipoPagina
from src.controle.controlador_usuario import ControladorUsuario
from src.controle.controlador_acesso import ControladorAcesso
from src.controle.controlador_login import ControladorLogin
from src.controle.controlador_home import ControladorHome
from src.controle.controlador_cadastro_novo_usuario import ControladorCadastroNovoUsuario
from src.controle.controlador_livro import ControladorLivro
from src.controle.controlador_pagina_livro import ControladorPaginaLivro

from sys import exit

class PaginaInvalidaException(Exception):

    def __init__(self, pagina: object) -> None:
        super().__init__(f"Erro ao setar nova página. Página {pagina} não é uma página válida.")


class VoltarPaginaException(Exception):


    def __init__(self, *args: object) -> None:
        super().__init__(f"Tentando voltar para uma página que não existe.")

class ControladorSistema:

    def __init__(self) -> None:
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_livro = ControladorLivro(self)
        self.__controlador_carrinho = ControladorCarrinho(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__paginas_acessadas: list[TipoPagina] = []
        self.troca_pagina(TipoPagina.ACESSO)
        
    
    @property
    def pagina(self):
        return self.__pagina
    
    @pagina.setter
    def pagina(self, pagina: AbstractControlador):
        if not isinstance(pagina, AbstractControlador):
            raise PaginaInvalidaException(pagina)
        
        self.__pagina = pagina

    @property
    def controlador_usuario(self) -> ControladorUsuario:
        return self.__controlador_usuario

    @property
    def controlador_livro(self) -> ControladorLivro:
        return self.__controlador_livro

    @property
    def controlador_carrinho(self) -> ControladorCarrinho:
        return self.__controlador_carrinho

    @property
    def controlador_relatorio(self) -> ControladorRelatorio:
        return self.__controlador_relatorio

    @property
    def paginas_acessadas(self) -> list[TipoPagina]:
        return self.__paginas_acessadas
    
    def troca_pagina(self, pagina: TipoPagina, nova_pagina: bool = True):
        self.pagina = {
            TipoPagina.ACESSO: ControladorAcesso,
            TipoPagina.CADASTRO_USUARIO: ControladorCadastroNovoUsuario,
            TipoPagina.CADASTRO_LIVRO: ControladorCadastraLivro,
            TipoPagina.LOGIN: ControladorLogin,
            TipoPagina.HOME: ControladorHome,
            TipoPagina.MINHA_CONTA: ControladorMinhaConta,
            TipoPagina.PESQUISA: ControladorPesquisaLivro,
            TipoPagina.ACERVO: ControladorAcervoUsuario,
            TipoPagina.PAGINA_LIVRO: ControladorPaginaLivro,
            TipoPagina.COMPRA: ControladorCompra
        }.get(pagina)(self)

        if nova_pagina:
            self.__paginas_acessadas.append(pagina)
        else:
            del self.__paginas_acessadas[-1]
    
    def voltar(self) -> None:
        if len(self.__paginas_acessadas) == 1:
            raise VoltarPaginaException()
        self.troca_pagina(self.__paginas_acessadas[-2], nova_pagina=False)
    
    def logout(self) -> None:
        self.__paginas_acessadas.clear()
        self.troca_pagina(TipoPagina.LOGIN)
    
    def sair(self) -> None:
        self.controlador_relatorio.fecha_relatorio()
        exit()
    
    def run(self) -> None:
        while True:
            self.pagina.main()
        