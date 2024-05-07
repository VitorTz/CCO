from src.limite.abstract_tela import AbstractTela


class TelaCompra(AbstractTela):

    def __init__(self) -> None:
        super().__init__(titulo="Compras")