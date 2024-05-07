from time import sleep
import globals
from typing import Union, List, Dict
from queue import Queue
from threading import Semaphore, Thread, Lock
from mines.oil import Pipeline
from mines.uranium import StoreHouse
from space.rocket import Rocket
from stars.planet import Planet
from random import choice


class Viagem(Thread):

    """
    Representa uma viagem/lançamento de uma base
    Uma viagem pode carregar um foguete explosivo de uma base até
    um planeta ou um foguete de carga de uma base na terra até a lua
    """
    def __init__(
        self,
        foguete: Rocket | None = None,
        partida: Union['SpaceBase', None] = None,
        destino: Union['SpaceBase', Planet, None] = None
    ) -> None:
        super().__init__()
        self.__foguete = foguete
        self.__partida = partida
        self.__destino = destino
        
        # Se algum parametro for None escolhe aleatoriamente
        if foguete is None:
            self.__foguete = self.__get_foguete_aleatorio()
        if destino is None:
            self.__destino = self.__get_destino_aleatorio()
        if partida is None:
            self.__partida = self.__get_partida_aleatoria()
        
        if self.__foguete.name == "LION":
            self.__foguete.fuel_cargo = 120
            self.__foguete.uranium_cargo = 75
        
        # Coloca na fila de lançamento da base de partida
        self.__coloca_viagem_na_fila()
        # Status da viagem
        self.__viagem_completa = False
        self.__sucesso_viagem = False
    
    @property
    def viagem_completa(self) -> bool:
        return self.__viagem_completa
    
    @property
    def sucesso_viagem(self) -> bool:
        return self.__sucesso_viagem
    
    @property
    def foguete(self) -> Rocket:
        return self.__foguete

    @property
    def partida(self) -> 'SpaceBase':
        return self.__partida
    
    @property
    def destino(self) -> Union[Planet, 'SpaceBase']:
        return self.__destino

    def __get_partida_aleatoria(self) -> 'SpaceBase':
        """
        Retorna uma base aleatoria.
        @return SpaceBase
        """
        bases: Dict[str, 'SpaceBase'] = globals.get_bases_ref()
        nome_bases: List[str] = bases.keys()
        nome_base_partida = ""
        if self.foguete.name == "LION":
            nome_base_partida = choice(
                [n for n in nome_bases if n != "moon"]
            )
        else:
            nome_base_partida = choice(nome_bases)
        return bases.get(nome_base_partida)
    
    def __get_foguete_aleatorio(self) -> Rocket:
        """
        Retorna um foguete explosivo aleatorio
        @return Rocket
        """
        return Rocket(
            choice(
                globals.get_nome_foguetes_explosivos()
            )
        )

    def __get_destino_aleatorio(self) -> Union[Planet, None]:
        """
        Retorna um planeta aleatorio
        @return Planet caso exista um planeta ainda não habitavel
        """
        planetas_habitaveis: List[Planet] = []
        for planeta in globals.get_planets_ref().values():
            with planeta.mutex:
                if planeta.terraform > 0.0:
                    planetas_habitaveis.append(planeta)
        if planetas_habitaveis:
            return choice(planetas_habitaveis)
    
    def __coloca_viagem_na_fila(self) -> None:
        """
        Coloca a viagem na fila de viagens da base de partida
        Respeita o número máximo de foguetes a serem
        armazenas na base de partida da viagem.
        """
        if self.destino:
            # Adquire o semaforo que limita os foguetes armazenados na base
            self.partida.sema_foguetes.acquire()
            # Caso a terraformação ainda não esteja completa
            if not globals.terraformacao_esta_completa():
                # Reabastece caso necessário e consome o fuel e uranium da base
                self.partida.base_rocket_resources(self.__partida, self.__foguete)
                # Coloca na fila de lançamentos
                self.partida.fila_viagens.put(self)
            else:
                # Caso a viagem tenha sido criada porem na hora
                # de produzir o foguete a terraformação já esteja completa
                # Neste caso apenas chama o método de conclusão de viagem
                # e define o sucesso como False já que o a viagem não aconteceu
                self.conclui_viagem()
                self.__sucesso_viagem = False
    
    def conclui_viagem(self) -> None:
        self.__viagem_completa = True

    def aguarda_conclusao(self) -> None:
        """
        É chamado apenas na situação onde a lua está 
        esperando pelo combustivel vindo da terra.
        Apenas a thread de produção da base da lua fica em espera ocupada
        """
        while not self.__viagem_completa:
            pass
        
    def run(self) -> None:
        """Inicia a viagem"""
        if self.foguete.successfull_launch(self.__partida):
            print(f"[{self.foguete.name} - {self.foguete.name}] launched in {self.partida.name} com destino em {self.destino.name}.")
            
            self.__sucesso_viagem = not self.foguete.voyage(self.destino)
            if self.__sucesso_viagem:
                if self.destino.name != "MOON":
                    # Viagem de detonação
                    self.foguete.nuke(self.destino)
                    globals.verifica_terraform() 
                else:
                    # Viagem de reabastecimento
                    self.destino.refuel_oil(self.foguete.fuel_cargo, usar_minas=False)
                    self.destino.refuel_uranium(self.foguete.uranium_cargo, usar_minas=False)
        else:
            self.__sucesso_viagem = False
        self.conclui_viagem()


class SpaceBase(Thread):

    ################################################
    # O CONSTRUTOR DA CLASSE NÃO PODE SER ALTERADO #
    ################################################
    def __init__(self, name, fuel, uranium, rockets):
        Thread.__init__(self)
        self.name = name
        self.uranium = 0
        self.fuel = 0
        self.rockets = 0
        self.constraints = [uranium, fuel, rockets]
    
    @property
    def fila_viagens(self) -> Queue[Viagem]:
        """Fila de lançamentos da base"""
        return globals.get_fila_viagens(self.name)

    @property
    def sema_foguetes(self) -> Semaphore:
        """Semaforo que limita o número de foguetes armazenados na base"""
        return globals.get_sema_foguetes(self.name)
    
    @property
    def mutex_oil(self) -> Lock:
        """Mutex que protege as alterações no atributo fuel"""
        return globals.get_mutex_recurso_base(self.name, "oil")
    
    @property
    def mutex_uranium(self) -> Lock:
        """Mutex que protege as alterações no atributo uranium"""
        return globals.get_mutex_recurso_base(self.name, "uranium")

    def print_space_base_info(self):
        print(f"🔭 - [{self.name}] → 🪨  {self.uranium}/{self.constraints[0]} URANIUM  ⛽ {self.fuel}/{self.constraints[1]}  🚀 {self.rockets}/{self.constraints[2]}")
    
    def base_rocket_resources(self, base: 'SpaceBase', foguete: Rocket):
        """Reabastece a base caso necessário e consome as unidades
        de uranium e fuel para produzir o foguete requisitado
        """
        fuel = foguete.get_fuel_necessario(base.name)
        uranium = foguete.get_uranium_necessario(base.name)
        self.__refuel(fuel, uranium)  # Reabastece apenas caso necessário

        with self.mutex_oil:
            self.fuel -= fuel

        with self.mutex_uranium:
            self.uranium -= uranium
        
    def __refuel_mina(self, qtd: int, nome_mina: str) -> None:
        """Usado para reabastecer uma base usando uma mina terrestre"""
        mina: Pipeline | StoreHouse = globals.get_mines_ref().get(nome_mina)
        # Sai do laço quando foi possível obter a quantidade de recurso
        # necessária da mina ou a terraformação está completa
        while True and not globals.terraformacao_esta_completa():
            mina.mutex.acquire()
            if mina.unities - qtd >= 0:
                mina.unities -= qtd
                mina.mutex.release()
                break
            mina.mutex.release()
        
    def refuel_oil(self, fuel: int, usar_minas: bool = True) -> None:
        """
        @param fuel: int
                Quantidade necessária para reabastecer.
        @param usar_minas: bool
                Se deve usar uma mina terrestre para realizar
                o reabastecimento. Se está fazendo um reabastecimento
                usando o foguete LION então usar_minas deve ser False
        """
        if fuel > 0:
            if usar_minas:
                self.__refuel_mina(fuel, "oil_earth")
        
            with self.mutex_oil:
                self.fuel += fuel

    def refuel_uranium(self, uranium: int, usar_minas: bool = True) -> None:
        """
        @param fuel: int
                Quantidade necessária para reabastecer.
        @param usar_minas: bool
                Se deve usar uma mina terrestre para realizar
                o reabastecimento. Se está fazendo um reabastecimento
                usando o foguete LION então usar_minas deve ser False
        """
        if uranium > 0:
            if usar_minas:
                self.__refuel_mina(uranium, "uranium_earth")

            with self.mutex_uranium:
                self.uranium += uranium

    def __refuel(self, fuel: int, uranium: int) -> None:
        # Verifica se é necessário reabastecer
        if self.fuel < fuel or self.uranium < uranium:
            if self.name == "MOON":
                """
                Caso esteja na base da Lua então
                deve criar uma nova viagem usando o foguete LION
                com destino a Lua e partida em alguma base terrestre 
                escolhida de forma aleatoria
                """
                while True:
                    # Cria a viagem e coloca na fila de lançamento de alguma base terrestre
                    viagem = Viagem(
                        foguete=Rocket("LION"),
                        partida=None, # Passar None faz com que uma base aleatoria seja escolhida
                        destino=self # self = Base da Lua neste caso
                    )
                    # Aguarda que a viagem seja iniciada e concluida
                    viagem.aguarda_conclusao()
                    # Após o termino verifica se a viagem foi um sucesso
                    # Caso seja um sucesso então o reabastecimento foi concluido
                    # Caso não então deve repetir o processo
                    # Tambem sai do laço caso a terraformação esteja completa
                    if viagem.sucesso_viagem or globals.terraformacao_esta_completa():
                        break
            else:
                # Usado para reabastecer uma base terrestre
                self.refuel_oil(fuel - self.fuel)
                self.refuel_uranium(uranium - self.uranium)

    def __cria_viagem(self) -> None:
        """
        Cria nova viagens com partida na base self e foguete explosivos
        e destino aleatorios.
        O método __cria_viagem será executado por uma Thread
        O número de threads que executar __cria_viagem é igual
        ao número de foguetes que a base pode produzir ou manter
        armazenados ao mesmo tempo
        """
        while not globals.terraformacao_esta_completa():
            # Faz um acquire em self.sema_foguetes para 
            # criar uma nova viagem
            Viagem(partida=self)
    
    def __inicia_viagem(self) -> None:
        """
        Também é executado por threads porem apenas uma thread
        é criada para executar este método
        """
        while not globals.terraformacao_esta_completa():
            if not self.fila_viagens.empty():
                # Inicia a primeira viagem da fila
                # e libera o semaforo para que novas viagens
                # possam ser criadas
                viagem: Viagem = self.fila_viagens.get()
                viagem.start()
                self.sema_foguetes.release()
        # Após o fim do laço finaliza viagens esperando 
        # para serem criadas ou criadas e não iniciadas
        self.__finaliza_viagens_na_fila()

    def __finaliza_viagens_na_fila(self) -> None:
        # Só é chamado após a thead __inicia_viagem sair do laço
        # controlado por globals.terraformacao_esta_completa
        while not self.fila_viagens.empty():
            viagem = self.fila_viagens.get()
            # Libera as viagens esperando para serem criadas
            # As viagens são liberas mas não são iniciadas
            # As viagens são iniciadas dentro do laço em __inicia_viagem
            # self.__finaliza_viagens_na_fila() é sempre chamado após
            # o laço em __inicia_viagem
            viagem.partida.sema_foguetes.release()
            # Muda o status para viagem concluida
            viagem.conclui_viagem()

    def run(self):
        globals.acquire_print()
        self.print_space_base_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass
        
        # Número de threads que produzem viagens = max de foguetes da base
        # Número de threads que consomem viagens = 1

        threads_cria_viagem = [
            Thread(target=self.__cria_viagem) for _ in range(self.constraints[2])
        ]
        thread_inicia_viagem = Thread(target=self.__inicia_viagem)

        [t.start() for t in threads_cria_viagem]
        thread_inicia_viagem.start()

        [t.join() for t in threads_cria_viagem]
        thread_inicia_viagem.join()


        
