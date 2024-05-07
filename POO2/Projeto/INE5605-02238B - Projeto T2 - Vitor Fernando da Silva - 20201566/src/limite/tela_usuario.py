from src.limite.abstract_tela import AbstractTela
from typing import Dict, Tuple
import PySimpleGUI as sg 


class ErroCadastroUsuarioException(Exception):

    def __init__(self, e: str) -> None:
        super().__init__(f"Houve um erro em seu cadastro. {e}")


class TelaUsuario(AbstractTela):

    def __init__(self) -> None:
        super().__init__(titulo="Tela do usuário")
    
    def pega_valores_cadastro(self) -> Dict[str, str]:
        """Retorna os valores necessários para o cadastro do usuário"""
        event, values = self.get_dados_tela(
            [
                [sg.Text("Casdastro de novo usuário")],
                [sg.Text("Nome:", size=(24, 1)), sg.InputText(key="nome")],
                [sg.Text("Email:", size=(24, 1)), sg.InputText(key="email")],
                [sg.Text("Senha:", size=(24, 1)), sg.InputText(key="senha")],
                [sg.Text("Cep (apenas números):", size=(24, 1)), sg.InputText(key="cep")],
                [sg.Text("Número residência:", size=(24, 1)), sg.InputText(key="numero_residencia")],
                [sg.Button("Cadastrar"), sg.Button("Cancelar")]
            ]
        )
        if event not in ("Cancelar", None):
            try:
                self.verifica_valores_tela(values)
                if not (values["cep"].isdigit() and len(values["cep"]) == 8):
                    raise ErroCadastroUsuarioException(f"Cep {values['cep']} inválido, o cep precisa existir e conter apenas números")
                
                self.valida_numero(values["numero_residencia"], _int=True)

            except Exception as e:
                self.popup(e)
            else:
                return values
            
    def pega_valores_acesso_sistema(self) -> Tuple:
        return self.get_dados_tela(
            [
                [sg.Text("Email:", size=(13, 1)), sg.InputText(key="email")],
                [sg.Text("Senha:", size=(13, 1)), sg.InputText(key="senha")],
                [sg.Button("Login"), sg.Button("Cadastrar")]
            ]
        )
    