from src.controle.abstract_controlador import AbstractControlador
from src.limite.tela_relatorio import TelaRelatorio
from pathlib import Path


class ControladorRelatorio(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        super().__init__(
            controlador_sistema,
            opcoes={},
            nome_controlador="Relatorio"
        )
        self.__tela = TelaRelatorio()
        self.__path_relatorio_views = Path("db/relatorio/views.json")
        self.__path_relatorio_vendas = Path("db/relatorio/vendas.json")
        self.__relatorio_views = self.le_json(self.__path_relatorio_views)
        self.__relatorio_vendas = self.le_json(self.__path_relatorio_vendas)
        
    @property
    def tela(self) -> TelaRelatorio:
        return self.__tela
    
    def add_view_livro(self, isbn: str):
        """Conta o número de vezes que um usuário abriu a página de certo livro"""
        views = self.__relatorio_views.get(isbn, 0)
        self.__relatorio_views[isbn] = views + 1

    def add_venda(self, id_vendedor: str, valor_venda: str) -> None:
        valor_total_vendas = self.__relatorio_vendas.get(id_vendedor, 0.0)
        self.__relatorio_vendas[id_vendedor] = valor_total_vendas + float(valor_venda)
    
    def fecha_relatorio(self) -> None:
        # Ordena o dicionário em ordem descrecente
        self.__relatorio_views = dict(
            sorted(self.__relatorio_views.items(),key = lambda x:x[1], reverse=True)
            )
        
        self.__relatorio_vendas = dict(
            sorted(self.__relatorio_vendas.items(),key = lambda x:x[1], reverse=True)
            )

        self.salva_json(self.__relatorio_views, self.__path_relatorio_views)
        self.salva_json(self.__relatorio_vendas, self.__path_relatorio_vendas)

        