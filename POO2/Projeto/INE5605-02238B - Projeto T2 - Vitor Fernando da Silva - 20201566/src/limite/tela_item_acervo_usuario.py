from src.limite.abstract_tela import AbstractTela
from typing import Dict 
import PySimpleGUI as sg 


class TelaItemAcervoUsuario(AbstractTela):

    def __init__(self) -> None:
        super().__init__(titulo="Acervo do usuário")
    
    def __valida_valores_tela(self, valores: Dict[str, str]) -> None:
        self.valida_numero(valores["exemplares"], _int=True)
        self.valida_numero(valores["valor"], _float=True)   
    
    def pega_valores_cadastro(self) -> Dict[str, str]:
        event, values = self.get_dados_tela(
            [
                [sg.Text("Exemplares:", size=(16, 1)), sg.InputText(key="exemplares")],
                [sg.Text("Valor:", size=(16, 1)), sg.InputText(key="valor")],
                [sg.Button("Ok"), sg.Button("Cancelar")]
            ]
        )
        if event == "Ok":
            try:
                self.__valida_valores_tela(values)
            except Exception as e:
                self.popup(e)
            else:
                return values

    def pega_forma_cadastro(self) -> str:
        event, _ = self.get_dados_tela(
            [
                [sg.Text("Escolha como quer adicionar um livro em seu acervo")],
                [sg.Button("Escolher livro acervo geral"), sg.Button("Novo livro"), sg.Button("Cancelar")]
            ]
        )
        return event