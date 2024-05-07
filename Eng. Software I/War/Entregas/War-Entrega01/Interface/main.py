from tkinter import *
from typing import Literal
from pathlib import Path
from json import load
from glob import glob


# Cada jogador será identificado pela sua cor
Jogador = Literal[
    'vermelho',
    'amarelo',
    'verde',
    'azul'
]

# Ações que podem ser tomadas durante o turno de um jogador
# A interface deve mudar para cada tipo de ação
Acao = Literal[
    'esperar',
    'fortificar'
    'atacar1',
    'atacar2',
    'deslocar1',
    'deslocar2',
    'passar_turno'
]


class InterfaceConfig:

    """
    Permite o acesso as configurações/definições/arquivos utilizados na interface
    """

    def __init__(self, player: Jogador) -> None:
        self.__config = {}
        # Carrega todos os arquivos de configurações em um único dicionário
        config_files = glob("config/*.json")
        for file in config_files:
            with open(file, "r") as f:
                self.__config.update(load(f))
        self.__player = player

    def load_imagens(self) -> None:
        """
        Cria e armazena uma instância de PhotoImage para cada imagem
        que será utilizada na interface.
        """
        self.imagens["mapa"] = PhotoImage(file=Path(self.imagens["mapa"]))

        interface = self.imagens["interface"][self.__player]
        tropas = self.imagens["label_tropas"]
        for d in (interface, tropas):
            for nome, path in d.items():
                img = PhotoImage(file=Path(path))
                d[nome] = img

    @property
    def player(self) -> Jogador:
        """Retorna a cor que identifica o jogador"""
        return self.__player

    @property
    def imagem_mapa(self) -> PhotoImage:
        """Retorna um objeto PhotoImage que representa o mapa do jogo"""
        return self.__config["imagens"]["mapa"]

    @property
    def imagens(self) -> dict:
        """Retorna o dicionário que guarda todas as imagens"""
        return self.__config["imagens"]

    @property
    def imagens_jogador(self) -> dict:
        """
        Retorna o dicionário que guarda as imagens especificas do
        jogador. A ideia é que cada jogador tenha a sua interface
        customizada para cor que o representa.
        No momento só o jogador vermelho possui a interface
        nas cores vermelho.
        """
        return self.__config["imagens"]["interface"][self.player]

    @property
    def window(self) -> dict:
        """Retorna as configurações básicas da janela"""
        return self.__config.get("window")

    @property
    def cores(self) -> dict[str, str]:
        """
        Retorna um dicionário com as cores e seus valores
        hexadecimais
        """
        return self.__config.get("cores")

    @property
    def texto_descricao_acao(self) -> dict[str, str]:
        """
        Retorna o dicionário que guarda a descrição das ações
        """
        return self.__config.get("texto_descricao_acao")

    @property
    def fonte(self) -> dict[str, str]:
        """Retorna um dicionário com as fontes utilizadas no jogo"""
        return self.__config.get("fonte")

    @property
    def territorios(self) -> dict:
        """
        Retorna um dicionário com as informações necessárias
        para exibir os exercitos ocupantes na tela.
        """
        return self.__config["territorios"]

    @property
    def cores_jogadores(self) -> list[str]:
        """
        Retorna uma lista com o nome das cores que representam
        os jogadores.
        """
        return self.__config["cores_jogadores"]

    @property
    def player_color(self) -> str:
        """
        Retorna o hex value da cor que representa o jogador.
        """
        return self.cores.get(self.__player)

    @property
    def window_bg_color(self) -> str:
        """
        Retorna o hex value da cor de fundo da tela.
        """
        return self.window.get("bg-color")


def init_window(config: InterfaceConfig) -> Tk:
    """Inicia a janela com algumas configurações iniciais"""
    window = Tk()
    window.title(config.window.get("title"))
    window["bg"] = config.window.get("bg-color")
    window.geometry(config.window.get("geometry"))
    window.resizable(False, False)
    return window


def init_labels(window: Tk, config: InterfaceConfig) -> dict[str, Label]:
    """
    Cria e retorna um dicionário com os principais Labels da interface inicial
    """
    # Labels que não mudam durante o jogo
    Label(
        window,
        image=config.imagens["mapa"],
        bg=config.window_bg_color
    ).place(x=0, y=81)
    Label(
        window,
        image=config.imagens_jogador["caixa-descricao-jogada"],
        bg=config.window_bg_color
    ).place(x=200, y=0)
    Label(
        window,
        text=f"JOGADOR {config.player.upper()}",
        fg=config.player_color,
        bg=config.cores["cinza"],
        font=config.fonte["grande"]
    ).place(x=220, y=30)

    # Label que tem seu conteudo alterado durante o jogo
    label_descricao_jogada = Label(
        window,
        text=config.texto_descricao_acao["esperar"],
        fg=config.player_color,
        bg=config.cores["cinza"],
        font=config.fonte["regular"]
    )
    label_descricao_jogada.place(x=475, y=30)

    label_botao_acao = Label(
        window,
        image=config.imagens_jogador["esperar"],
        bg=config.window_bg_color
    )
    label_botao_acao.place(x=400, y=583)

    # Botões

    # Botão Ação
    # Botão ação permite ao jogador passar para a próxima ação a ser realizda no turno
    btn_acao = Button(
        window,
        image=config.imagens_jogador[f"btn-esperar"],
        fg=config.cores["cinza"],
        bg=config.cores["cinza"],
        activebackground=config.cores["cinza"],
        activeforeground=config.cores["cinza"],
        highlightthickness=0,
        bd=0
    )

    btn_acao.place(x=788, y=612)
    # Fim Botão Ação

    # Botão ver exercitos
    # Permite ao jogador ver informações sobre os territorios e exercitos
    # de todos os jogadores
    btn_ver_exercitos = Button(
        window,
        image=config.imagens_jogador["btn-ver-exercitos"],
        fg=config.window_bg_color,
        bg=config.window_bg_color,
        activebackground=config.window_bg_color,
        activeforeground=config.window_bg_color,
        highlightthickness=0,
        bd=0
    )
    btn_ver_exercitos.place(x=30, y=600)
    # Fim botão ver exercitos

    # Botão ver objetivos
    # Permite ao jogador ver o seu objetivo
    btn_ver_objetivos = Button(
        window,
        image=config.imagens_jogador["btn-ver-objetivo"],
        fg=config.window_bg_color,
        bg=config.window_bg_color,
        activebackground=config.window_bg_color,
        activeforeground=config.window_bg_color,
        highlightthickness=0,
        bd=0
    )
    btn_ver_objetivos.place(x=1150, y=600)

    # Fim botão ver objetivos

    return {
        "label_descricao_jogada": label_descricao_jogada,
        "label_botao_acao": label_botao_acao,
        "btn_acao": btn_acao,
        "btn_ver_objetivo": btn_ver_objetivos,
        "btn_ver_exercitos": btn_ver_exercitos
    }


def init_territorios(window: Tk, config: InterfaceConfig) -> dict:
    """
    Inicia os labels e textos de cada territorio.
    """
    for value in config.territorios.values():
        # value = dicionário que contem as informações necessárias
        # para exibir as informações sobre o dono do territorio
        # e a qtd de tropas no territorio.

        # Jogador pode ser 'verde', 'vermelho', 'azul', 'amarelo'
        jogador = value["jogador"]
        # Circulo que fica atrás da qtd de tropas no territorio
        value["label"] = Label(
            window,
            image=config.imagens["label_tropas"][jogador],
            bg=value["cor"]
        )
        # Texto que indica a qtd de tropas no territorio
        value["text"] = Label(
            window,
            text=value["qtd_exercitos"],
            font=config.fonte["pequena"],
            fg="black",
            bg=config.cores[jogador]
        )
        # Posiciona corretamente os labels em cima do territorio
        value["label"].place(x=value["x"], y=value["y"])
        value["text"].place(x=value["x"]+10, y=value["y"]+8)


class ActorPlayer:

    def __init__(
        self,
        config: InterfaceConfig,
        player: Jogador,
        objetivo: str,
        acao: Acao = "fortificar"  # Ação inicial a ser tomada pelo jogador
    ) -> None:
        self.__config = config
        self.__player = player
        self.__objetivo = objetivo
        self.__meu_turno = True

        self.__acao = acao
        self.__window = init_window(self.__config)
        # Instancia um objeto de PhotoImage para as imagens necessárias
        self.__config.load_imagens()
        # Inicia os labels da interface
        self.__labels = init_labels(self.__window, self.__config)
        # Inicia os labels dos territorios
        init_territorios(self.__window, self.__config)
        # Configura os métodos bind dos botões e atualiza a interface para
        # representar a ação inicial.
        self.__bind_buttons()
        self.__bind_territorios()
        self.__atualiza_interface()
        self.__window.mainloop()

    def __bind_buttons(self) -> None:
        """Configura o o método bind dos botões"""
        self.__labels["btn_acao"].bind(
            "<Button-1>", lambda e: self.__proxima_acao()
        )
        self.__labels["btn_ver_objetivo"].bind(
            "<Button-1>", lambda e: self.__ver_objetivo()
        )
        self.__labels["btn_ver_exercitos"].bind(
            "<Button-1>", lambda e: self.__ver_exercitos()
        )

    def __bind_territorios(self) -> None:
        """
        Configura o método bind dos territórios.
        """
        for name, value in self.__config.territorios.items():
            value["label"].bind(
                "<Button-1>",
                lambda e, k=name, v=value: self.__click_territorio(k, v)
            )
            value["text"].bind(
                "<Button-1>",
                lambda e, k=name, v=value: self.__click_territorio(k, v)
            )

    def __click_territorio(self, nome: str, info: dict[str, str | Label]) -> None:
        """Representa o clique em algum territorio do mapa"""
        b = "="*20
        print(b)
        print(f"{nome}")
        for k, v in info.items():
            print(f"{k} -> {v}")
        print(b)

    def __atualiza_interface(self) -> None:
        """Atualiza a interface conforme a ação a ser realizada pelo jogador"""
        botao_acao = self.__labels["btn_acao"]
        label_botao_acao = self.__labels["label_botao_acao"]
        label_descricao = self.__labels["label_descricao_jogada"]

        botao_acao.config(
            image=self.__config.imagens_jogador[f"btn-{self.__acao}"]
        )
        label_botao_acao.config(
            image=self.__config.imagens_jogador[self.__acao]
        )
        label_descricao.config(
            text=self.__config.texto_descricao_acao[self.__acao]
        )

    def __proxima_acao(self) -> None:
        """
        Existem uma ordem a ser seguida no turno de cada jogador.
        Ações:
        1 -> Fortificar
        2 -> Atacar, se dese1ar
        3 -> Deslocar exercitos, se desejar
        4 -> Passar turno
        Define a próxima ação a ser realizda. É executado quando
        o jogador aperta o botão para passar para a próxima ação.
        """
        # Só um exemplo para ver a interface mudando conforme a ação
        # a ser realizada
        if self.__meu_turno:
            if self.__acao == "passar_turno":
                self.__passar_turno()
            else:
                ordem = [
                    'esperar',
                    'fortificar',
                    'atacar1',
                    'atacar2',
                    'deslocar1',
                    'deslocar2',
                    'passar_turno'
                ]
                prox_acao = (ordem.index(self.__acao) + 1) % len(ordem)
                self.__acao = ordem[prox_acao]
                # Atualiza a interface para permitir a execução da próxima ação
                self.__atualiza_interface()
        else:
            print("Espere seu turno")

    def __passar_turno(self) -> None:
        """Passa o turno é atualiza a interface para a ação 'esperar'"""
        self.__meu_turno = False
        self.__acao = 'esperar'
        self.__atualiza_interface()

    def __ver_objetivo(self) -> None:
        """Abre uma segunda tela com o objetivo do jogador"""
        window = Toplevel(
            padx=30,
            pady=20,
            bg=self.__config.window_bg_color
        )
        window.title("Seu objetivo")
        titulo = Label(
            window,
            text="Objetivo",
            font=self.__config.fonte["grande"],
            fg=self.__config.player_color,
            bg=self.__config.window_bg_color
        )
        texto_descricao_acao = Label(
            window,
            text=self.__objetivo,
            fg=self.__config.player_color,
            bg=self.__config.window_bg_color,
            font=self.__config.fonte["regular"]
        )
        titulo.pack()
        texto_descricao_acao.pack()

    def __conta_exercitos_e_territorios(self) -> dict:
        """
        Retorna um dicionário com o número de territorios e exercitos
        de cada jogador
        """
        res = {
            jogador: {
                "Territorios": 0,
                "Exercitos": 0
            } for jogador in self.__config.cores_jogadores
        }
        for value in self.__config.territorios.values():
            res[value["jogador"]]["Territorios"] += 1
            res[value["jogador"]]["Exercitos"] += value["qtd_exercitos"]
        return res

    def __ver_exercitos(self) -> None:
        """
        Abre uma segunda tela para mostrar a quantidade de territorios e
        exercitos de cada jogador.
        """
        window = Toplevel(padx=40, pady=20, bg=self.__config.window_bg_color)
        window.title("Exercitos")
        res: dict[str, str] = self.__conta_exercitos_e_territorios()

        # Cria um frame para cada jogador e os posiciona na mesma linha
        coluna = 0  # Identifica a coluna de cada frame
        for jogador, info in res.items():
            frame = Frame(
                window,
                padx=20,
                pady=40,
                bg=self.__config.window_bg_color,
                width=200,
                height=400
            )
            frame.grid(row=0, column=coluna)
            coluna += 1
            # Nome do jogador
            Label(
                frame,
                text=jogador.title(),
                font=self.__config.fonte["grande"],
                fg=self.__config.cores[jogador],
                bg=self.__config.window_bg_color
            ).pack()
            # Quantidade de territorios
            Label(
                frame,
                text=f"Territorio: {info['Territorios']}",
                font=self.__config.fonte["regular"],
                fg=self.__config.cores[jogador],
                bg=self.__config.window_bg_color
            ).pack()
            # Quantidade de exercitos
            Label(
                frame,
                text=f"Exercitos: {info['Exercitos']}",
                font=self.__config.fonte["regular"],
                fg=self.__config.cores[jogador],
                bg=self.__config.window_bg_color
            ).pack()


def main() -> None:
    player = "vermelho"
    objetivo = "Conquistar a totalidade da America do Norte e Europa"
    config = InterfaceConfig(player)
    ActorPlayer(config, player, objetivo)


if __name__ == "__main__":
    main()
