from src.limite.abstract_tela import AbstractTela


class TelaLivro(AbstractTela):

    def __init__(self) -> None:
        super().__init__()

    def mostra_info_livro(self, info_livro: dict):
        for k, v in info_livro.items():
            if k != "vendedores":
                self.mostra_msg(f"{k} - {v}")