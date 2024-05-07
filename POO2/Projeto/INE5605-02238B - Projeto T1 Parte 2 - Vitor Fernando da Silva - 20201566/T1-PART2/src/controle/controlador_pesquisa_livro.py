from src.controle.tipo_pagina import TipoPagina
from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_pesquisa_livro import TelaPesquisaLivro
from src.entidade.livro import Livro


class LivroNaoEncontradoException(Exception):

    def __init__(self, livro: str) -> None:
        super().__init__(f"Livro {livro} não encontrado.")


class ControladorPesquisaLivro(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={
                "1": {"desc": "Pesquisar", "metodo": self.__opcao_pesquisa}
            },
            nome_controlador="Pesquisa"
        )
        self.__tela = TelaPesquisaLivro()

    @property
    def tela(self) -> TelaPesquisaLivro:
        return self.__tela 
    
    def __retorna_resultado_pesquisa(self, titulo_pesquisa) -> dict:
        resultados = {}

        for livro in self.controlador_sistema.controlador_livro.livros:
            if livro.vendedores: # Mostra apenas os livros que possuem vendedores
                c = 0  # Conta as diferenças entre os titulos
                for l1, l2 in zip(livro.titulo, titulo_pesquisa):
                    if l1 != " " and l2 != " " and l1.lower() != l2.lower():
                        c += 1
                    if c == 4:
                        break 
                
                if c < 4:
                    resultados[str(len(resultados)+1)] = livro
        
        if not resultados:
            raise LivroNaoEncontradoException(titulo_pesquisa)
        return resultados


    def __opcao_pesquisa(self) -> None:
        self.tela.limpa_terminal()
        
        # Titulo do livro que o usuário deseja pesquisar
        livro_pesquisar = self.tela.pega_info_usuario("Livro: ")
        
        # Guarda os resultados da pesquisa
        resultado_pesquisa = self.__retorna_resultado_pesquisa(livro_pesquisar)

        # Pede para o usuário escolher um livro dentre os resultados encontrados
        
        livro_escolhido: Livro = resultado_pesquisa[self.tela.pega_resposta(resultado_pesquisa)]
        # Adiciona uma visualização a página do livro
        self.controlador_sistema.controlador_relatorio.add_view_livro(livro_escolhido.isbn)
        
        self.controlador_sistema.troca_pagina(TipoPagina.PAGINA_LIVRO)
        self.controlador_sistema.pagina.livro = livro_escolhido

        
        



