from __future__ import annotations
from asyncio import events
from typing import TYPE_CHECKING, Dict, List
if TYPE_CHECKING:
    from src.controle.controlador_sistema import ControladorSistema
from src.entidade.usuario import Usuario
from src.entidade.livro import Livro
from src.controle.controlador_compra import ControladorCompra
from src.entidade.compra import Compra
from src.limite.tela_relatorio import TelaRelatorio


class ControladorRelatorio:

    def __init__(self, controlador_sistema: ControladorSistema) -> None:
        self.__tela = TelaRelatorio()
        self.__controlador_sistema = controlador_sistema
    
    def __get_livros_separados_por_genero(self) -> Dict[str, List[Livro]]:
        livros: List[Livro] = self.__controlador_sistema.controlador_livro.dao.get_all()
        livros_separados_por_genero: Dict[str, List[Livro]] = {}
        for livro in livros:
            if livro.genero not in livros_separados_por_genero:
                livros_separados_por_genero[livro.genero] = []
            livros_separados_por_genero[livro.genero].append(livro)
        return livros_separados_por_genero    
    
    def __total_vendido_por_usuario(self, lista_compras: List[Compra], usuario: Usuario) -> float:
        total: float = 0.0
        for compra in lista_compras:
            for item in compra.itens_carrinho:
                if item.vendedor.key == usuario.key:
                    total += item.valor_total
        return total
    
    def __get_vendedores_que_mais_venderam(self) -> Dict[str, float]:
        vendedores: List[Usuario] = self.__controlador_sistema.controlador_usuario.dao.get_all()
        todas_compras: List[Compra] = self.__controlador_sistema.controlador_compra.dao.get_todas_compras()
        vendedores.sort(
            key=lambda usuario: self.__total_vendido_por_usuario(todas_compras, usuario),
            reverse=True
        )
        return {
            usuario.email: self.__total_vendido_por_usuario(todas_compras, usuario) for usuario in vendedores
        }

    def __total_vendido_por_livro(self, compras: List[Compra], livro: Livro) -> float:
        """Retorna o o valor total das vendas do livro"""
        total_vendido: float = 0.0
        for compra in compras:
            for item in compra.itens_carrinho:
                if livro.key == item.item_acervo_usuario.livro.key:
                    total_vendido += item.valor_total
        return total_vendido

    def __get_livros_mais_vendidos_por_genero(self) -> Dict[str, List[str]]:
        """Retorna um dicionário com os livros mais vendidos por genero"""
        controlador_compra: ControladorCompra = self.__controlador_sistema.controlador_compra
        todas_compras: List[Compra] = controlador_compra.dao.get_todas_compras()
        livros_separados_por_genero: Dict[str, List[Livro]] = self.__get_livros_separados_por_genero()
        for genero, livros in livros_separados_por_genero.items():
            livros.sort(
                key=lambda livro: self.__total_vendido_por_livro(todas_compras, livro),
                reverse=True
            )
            for i, livro in enumerate(livros):
                livros[i] = f"{livro.titulo} | Total vendido = {self.__total_vendido_por_livro(todas_compras, livro)}"
        return livros_separados_por_genero
    
    def __get_livros_mais_visualizados_por_genero(self) -> Dict[str, List[str]]:
        """Retorna um dicionário com os livros mais visualizados por genero"""
        livros_separados_por_genero: Dict[str, List[Livro]] = self.__get_livros_separados_por_genero()
        for genero, livros in livros_separados_por_genero.items():
            livros.sort(key=lambda livro: livro.views, reverse=True)
            for i, livro in enumerate(livros):
                livros[i] = f"{livro.titulo} | Views = {livro.views}"
        return livros_separados_por_genero
    

    def __mostra_livros_mais_visualizados_por_genero(self) -> None:
        livros_mais_visualizados_por_genero: Dict[str, List[Livro]] = self.__get_livros_mais_visualizados_por_genero()
        self.__tela.mostra_relatorio(
            "Livros mais visualizados por genero",
            livros_mais_visualizados_por_genero
        )
    
    def __mostra_livros_mais_vendidos_por_genero(self) -> None:
        livros_mais_vendidos_por_genero: Dict[str, List[str]] = self.__get_livros_mais_vendidos_por_genero()
        self.__tela.mostra_relatorio(
            "Livros mais vendidos por genero",
            livros_mais_vendidos_por_genero
        )

    def __mostra_vendedores_que_mais_venderam(self) -> None:
        vendedores_que_mais_venderam: Dict[str, float] = self.__get_vendedores_que_mais_venderam()
        self.__tela.mostra_relatorio(
            "Vendedores que mais venderam",
            vendedores_que_mais_venderam
        )

    def main(self) -> None:
        opcoes = {
            "Livros mais vendidos por genero": self.__mostra_livros_mais_vendidos_por_genero,
            "Livros mais visualizados por genero": self.__mostra_livros_mais_visualizados_por_genero,
            "Vendedores que mais venderam": self.__mostra_vendedores_que_mais_venderam
        }
        self.__tela.set_layout_relatorio_para_mostrar(list(opcoes.keys()))
        while True:
            event, values = self.__tela.read_janela_principal()
            if event in ("Cancelar", None):
                self.__tela.close_janela_principal()
                break 
            opcao_escolhida = [k for k, v in values.items() if v is True]
            if opcao_escolhida:
                self.__tela.log(f"Executando {opcao_escolhida[0]}")
                opcoes.get(opcao_escolhida[0])()