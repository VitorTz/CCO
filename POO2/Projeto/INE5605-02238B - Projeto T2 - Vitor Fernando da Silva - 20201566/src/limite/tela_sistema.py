from src.limite.abstract_tela import AbstractTela
from typing import List, Tuple
import PySimpleGUI as sg 


class TelaSistema(AbstractTela):


    def __init__(self) -> None:
        super().__init__(titulo="Tela Sistema")

    def pega_opcao(self, opcoes: List[str], usuario_logado: str) -> Tuple:
        radios_btns: List = [[sg.Radio(opcao, "opcao", key=opcao)] for opcao in opcoes]
        layout = [
            [sg.Text(f"Usuário: {usuario_logado}")],
            [sg.Text("Escolha uma das opções")]
        ]
        layout.extend(radios_btns)
        layout.append([sg.Button("Escolher"), sg.Button("Cancelar")])
        return self.get_dados_tela(layout) 