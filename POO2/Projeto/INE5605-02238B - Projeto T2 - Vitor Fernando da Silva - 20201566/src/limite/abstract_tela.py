from abc import ABC, abstractmethod
from typing import Callable, List, Tuple, Dict
import PySimpleGUI as sg 


class NumeroInvalidoException(Exception):

    def __init__(self, numero: str) -> None:
        super().__init__(f"Número {numero} inválido.")


class CampoNaoPreenchidoException(Exception):

    def __init__(self, campo: str) -> None:
        super().__init__(f"Preencha o campo {campo}, por favor.")


class AbstractTela(ABC):

    sg.theme("DarkGrey13")

    @abstractmethod
    def __init__(self, titulo: str = "") -> None:
        """A tela possui duas janelas que podem ser manipuladas separadamente"""
        super().__init__()
        self.__titulo = titulo
        self.__janela_principal: sg.Window or None = None 
        self.__janela_secundaria: sg.Window or None = None 
    
    @property
    def janela_principal(self) -> sg.Window or None:
        return self.__janela_principal

    @property
    def janela_secundaria(self) -> sg.Window or None:
        return self.__janela_secundaria 
    
    def log(self, msg: str or Exception, indent: int = 2) -> None:
        if isinstance(msg, Exception):
            msg = f"Erro ==> {msg}"
            indent = 1
        print(f"{' ' * indent} -> {msg}")

    def __mostra_valores_lidos(self, event, values) -> None:
        """Mostra os valores lidos da tela no terminal"""
        self.log(f"Event -> {event} | Values -> {values}", indent=1)

    def __read_janela(self, janela: sg.Window) -> Tuple:
        if isinstance(janela, sg.Window):
            event, values = janela.read()
            self.__mostra_valores_lidos(event, values)
            return event, values

    def read_janela_principal(self) -> Tuple:
        return self.__read_janela(self.__janela_principal)
    
    def read_janela_secundaria(self) -> Tuple:
        return self.__read_janela(self.__janela_secundaria)
    
    def verifica_valores_tela(self, values: Dict) -> None:
        """Verifica se todos os campos foram preenchidos, levanta
        uma exceção caso ache um campo não preenchido"""
        for k, v in values.items():
            if not v:
                raise CampoNaoPreenchidoException(k)

    def __close_janela(self, janela: sg.Window) -> None:
        try:
            janela.close()
        except: pass 
    
    def close_janela_principal(self) -> None:
        self.__close_janela(self.__janela_principal)

    def close_janela_secundaria(self) -> None:
        self.__close_janela(self.__janela_secundaria)

    def set_layout_janela_principal(self, layout: List[List]) -> None:
        self.__janela_principal = sg.Window(self.__titulo, layout)
    
    def set_layout_janela_secundaria(self, layout: List[List]) -> None:
        self.__janela_secundaria = sg.Window(self.__titulo, layout)

    def get_layout_listagem(
        self,
        list_box_values: List[str],
        btns: List[str],
        size_list_box: Tuple[int, int] = (30, 20),
        key_list_box: str = "-LISTBOX-",
        default_text_desc_box: str = "Selecione um item para mostrar suas inforamções.",
        size_desc_box: Tuple[int, int] = (31, 20),
        key_desc_box: str = "-DESC-",
        multiline_text_box: bool = False
    ) -> None:
        """
        Retorna um layout de listagem e modifição de entidades
        Na primeira linha a tela contem uma listbox e um espaço 
        para mostrar as informações da entidade selecionada
        e na segunda linha possui botões para interagir com as 
        entidades listadas
        :param list_box_values: Valores a serem mostrados na listbox
        :param btns: Botões disponíveis na tela
        :param size_list_box: Tamanho da listbox
        :param key_list_box: Key da listbox
        :param default_text_desc_box: Texto exibido por padrão na caixa de texto ao lado da listbox
        :param size_desc_box: Tamanha da caixa de texto ao lado da listbox
        """
        text_box = sg.Text if multiline_text_box is False else sg.Multiline
        box = text_box(
                    default_text_desc_box, 
                    size=size_desc_box, 
                    background_color="#272a31", 
                    key=key_desc_box,
                    border_width=10 if multiline_text_box is False else 0
                )
        if multiline_text_box:
            box.Disabled = True
        return [
            [
                sg.Listbox(list_box_values, size=size_list_box, key=key_list_box),
                box
            ],
            [sg.Button(btn) for btn in btns]
        ]
    
    def reset_desc_box(self, msg: str = "Selecione um item para mostrar suas informações.") -> None:
        """Altera a mensagem da caixa de texto da tela principal para o valor default"""
        if self.__janela_principal:
            try:
                self.__janela_principal["-DESC-"].Update(msg)
            except Exception as e:
                self.log(e)
    
    def set_layout_main_window(
        self,
        list_box_values: List[str],
        btns: List[str],
        size_list_box: Tuple[int, int] = (30, 20),
        key_list_box: str = "-LISTBOX-",
        default_text_desc_box: str = "Selecione um item para mostrar suas informações.",
        size_desc_box: Tuple[int, int] = (31, 20),
        key_desc_box: str = "-DESC-"
    ) -> None:
        """Define a janela principal dos controladores"""
        layout = self.get_layout_listagem(
            list_box_values,
            btns,
            size_list_box,
            key_list_box,
            default_text_desc_box,
            size_desc_box,
            key_desc_box
        )
        self.set_layout_janela_principal(layout)
    
    def update_list_box(self, info: List[str], janela = None) -> None:
        """
        Atualiza as informações mostradas em alguma listbox, por padrão
        atualiza a listbox da janela principal
        """
        janela = self.__janela_principal if janela is None else janela
        try:
            self.__janela_principal["-LISTBOX-"].Update(info)
        except Exception as e:
            self.log(e)
    
    def get_dados_tela(self, layout: List[List]) -> Tuple:
        """Cria uma janela secundária com o layout recebido e retorna os dados inseridos pelo usuário"""
        self.set_layout_janela_secundaria(layout)
        event, values = self.read_janela_secundaria()
        self.close_janela_secundaria()
        return event, values

    def get_item_list_box(self, listbox_values: List[str]) -> str:
        """Mostra uma listbox para o usuário e retorna o valor escolhido"""
        self.set_layout_janela_secundaria(
            [
                [sg.Text("Escolha um item a baixo:")],
                [sg.Listbox(listbox_values, key="-LISTBOX-", size=(60, 10))],
                [sg.Button("Escolher"), sg.Button("Cancelar")]
            ]
        )
        _, values = self.read_janela_secundaria()
        self.close_janela_secundaria()
        try:
            return values["-LISTBOX-"][0]
        except:
            pass 
    
    def get_termo_pesquisa(self) -> str:
        """Pede para o usuário inserir um valor para pesquisa"""
        _, values = self.get_dados_tela([
            [sg.Text("Pesquise:"), sg.InputText(key="pesquisa")],
            [sg.Button("Ok"), sg.Button("Cancelar")]
        ])
        return values["pesquisa"]
    
    def popup(self, msg: str or Exception) -> None:
        """Mostra uma janela de aviso"""
        sg.popup(f'Aviso -> {msg}')
    
    def valida_numero(self, numero: str, _int: bool = False, _float: bool = False, outra_validacao: Callable = None) -> None:
        """Valida o número recibido, levanta uma exceçao caso seja um número inválido."""
        try:
            if _int:
                int(numero)
            elif _float:
                float(numero)
            if callable(outra_validacao):
                # Precisa ser uma validação que retorna um boolean
                if not outra_validacao(numero):
                    raise ValueError()
        except ValueError:
            raise NumeroInvalidoException(numero)