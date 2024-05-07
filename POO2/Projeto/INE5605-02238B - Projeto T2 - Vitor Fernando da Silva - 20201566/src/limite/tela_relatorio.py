from src.limite.abstract_tela import AbstractTela
from typing import Dict, List
import PySimpleGUI as sg


class TelaRelatorio(AbstractTela):

    def __init__(self) -> None:
        super().__init__(titulo="Relatorio")
    
    def __mostra_ordem(self, info: List[str] or float) -> str:
        """Retorna uma string para mostrar a ordem da lista"""
        if isinstance(info, float ):
            return str(info)
        elif isinstance(info, List):
            msg = ""
            for item in info:
                msg += f"{item}\n"
            return msg
    
    def set_layout_relatorio_para_mostrar(self, opcoes: List[str]) -> None:
        op = [[sg.Radio(opcao, "opcao", key=opcao)] for opcao in opcoes]
        layout = [
            [sg.Text("Escolha uma opção")]
        ]
        layout.extend(op)
        layout.append([sg.Button("Escolher"), sg.Button("Cancelar")])      
        self.set_layout_janela_principal(layout)
    
    def mostra_relatorio(self, nome_relatorio: str, info: Dict[str, List[str]]) -> None:
        layout: List[List] = [
            [sg.Text(nome_relatorio)]
        ]
        layout.extend(self.get_layout_listagem(
            list(info.keys()),
            ["Selecionar", "Cancelar"],
            size_desc_box=(70, 20),
            multiline_text_box=True
        ))
        self.set_layout_janela_secundaria(layout)
        while True:
            event, values = self.read_janela_secundaria()
            if event in ("Cancelar", None):
                self.close_janela_secundaria()
                break
            elif event == "Selecionar":
                if values["-LISTBOX-"]:
                    lista_selecionada = info.get(values["-LISTBOX-"][0])
                    self.janela_secundaria["-DESC-"].Update(
                        self.__mostra_ordem(lista_selecionada)
                    )