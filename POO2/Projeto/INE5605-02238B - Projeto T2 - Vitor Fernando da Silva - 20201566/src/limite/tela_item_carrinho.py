from src.limite.abstract_tela import AbstractTela
from typing import List
import PySimpleGUI as sg 


class TelaItemCarrinho(AbstractTela):

    def __init__(self) -> None:
        super().__init__(titulo="Carrinho")
    
    def get_vendedor_escolhido(self, info_livro: str, lista_vendedores: List[str]) -> str:
        layout = [
            [sg.Text("Escolha um vendedor")]
        ]
        layout.extend(self.get_layout_listagem(
            lista_vendedores,
            default_text_desc_box=info_livro,
            btns=["Escolher", "Cancelar"],
            size_list_box=(20, 5),
            size_desc_box=(30, 10)
        ))
        event, values = self.get_dados_tela(layout)
        if event == "Escolher":
            try:
                return values["-LISTBOX-"][0]
            except:
                pass 
        
    def get_quantidade_item_carrinho(self) -> int:
        """Retorna a quantidade de um item no carrinho"""
        event, values = self.get_dados_tela(
            [
                [sg.Text("Quantidade:"), sg.InputText(key="quantidade")],
                [sg.Button("Ok"), sg.Button("Cancelar")]
            ]
        )
        if event == "Ok":
            try:
                return int(values["quantidade"])
            except:
                pass 
