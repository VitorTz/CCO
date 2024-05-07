from src.limite.abstract_tela import TipoMensagem
from src.entidade.usuario import Usuario
from src.entidade.livro import Livro
from src.controle.tipo_pagina import TipoPagina
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_acervo_usuario import TelaAcervoUsuario


class ControladorAcervoUsuario(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Ver acervo", "metodo": self.__opcao_mostra_acervo},
                "2": {"desc": "Cadastrar livro", "metodo": self.__opcao_cadastra},
                "3": {"desc": "Remover livro", "metodo": self.__opcao_remover_livro}
            },
            nome_controlador="Acervo"
        )
        self.__tela = TelaAcervoUsuario()
    
    @property
    def tela(self) -> TelaAcervoUsuario:
        return self.__tela 
    
    @property
    def lista_livros_acervo(self) -> list[Livro]:
        """Retorna uma lista com todos os livros no acervo do usuário"""
        return self.controlador_sistema.controlador_usuario.pega_acervo()

    def __opcao_mostra_acervo(self) -> None:
        """Mostra os titulos de cada livro no acervo do usuário"""
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Seu acervo", tipo_msg=TipoMensagem.TITULO)
        self.tela.mostra_msg_lista(self.lista_livros_acervo)
        self.tela.pega_info_usuario("Pressione qualquer tecla para parar a visualização")

    def __opcao_cadastra(self) -> None:
        self.controlador_sistema.troca_pagina(TipoPagina.CADASTRO_LIVRO)
    
    def __opcao_remover_livro(self) -> None:
        self.tela.limpa_terminal()
        self.tela.mostra_msg("Escolha um livro para remover", tipo_msg=TipoMensagem.TITULO)
    
        usuario = self.controlador_sistema.controlador_usuario.usuario_logado

        # Cria um dicionário com uma identificação para cada livro
        # Serve para facilitar a seleção pelo usuário
        livros: dict[str, Livro] = {
            str(n+1): livro for n, livro in enumerate(self.lista_livros_acervo)
            }
        
        # Mostra os livros no acervo e pede para o usuário escolher um 
        livro_escolhido = self.tela.pega_resposta(livros)
        
        # Pega o livro escolhido 
        livro_escolhido = livros[livro_escolhido]
        
        # Deleta as informações necessárias
        del livro_escolhido.vendedores[usuario.id]
        del usuario.acervo[livro_escolhido.isbn]

        # Salva os arquivos
        self.controlador_sistema.controlador_usuario.salvar()
        self.controlador_sistema.controlador_livro.salvar()

        self.tela.mostra_msg(
            f"Livro {livro_escolhido.titulo} removido do seu acervo com sucesso!", tipo_msg=TipoMensagem.TITULO
            )
        self.wait()