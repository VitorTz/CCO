from threading import Lock, Semaphore
from typing import Tuple, Dict, Union
from mines.uranium import StoreHouse
from space.bases import SpaceBase
from stars.planet import Planet
from mines.oil import Pipeline
from queue import Queue


#  A total alteração deste arquivo é permitida.
#  Lembre-se de que algumas variáveis globais são setadas no arquivo simulation.py
#  Portanto, ao alterá-las aqui, tenha cuidado de não modificá-las. 
#  Você pode criar variáveis globais no código fora deste arquivo, contudo, agrupá-las em
#  um arquivo como este é considerado uma boa prática de programação. Frameworks como o Redux,
#  muito utilizado em frontend em libraries como o React, utilizam a filosofia de um store
#  global de estados da aplicação e está presente em sistemas robustos pelo mundo.

release_system = False
mutex_print = Lock()
planets = {}
bases = {}
mines = {}
simulation_time = None
status_terraform = False
nome_planetas = ("GANIMEDES", "EUROPA", "MARS", "IO")
nome_bases = ("ALCANTARA", "MOON", "MOSCOW", "CANAVERAL CAPE")
nome_foguetes = ("DRAGON", "FALCON", "LION")
nome_foguetes_explosivos = ("DRAGON", "FALCON")
nome_minas = ("oil_earth", "uranium_earth")

# Fila de lançamento das viagens de cada base
fila_viagens_base: Dict[str, Queue] = {
    nome: Queue() for nome in nome_bases
}

# Semaforo de produção dos foguetes
sema_foguetes: Dict[str, Semaphore] = {
    nome: Semaphore(value) for nome, value in zip(
        nome_bases, (1, 2, 5, 5)
    )
}

# Mutex que protege o nivel de terraformação dos planetas
mutex_terraform: Dict[str, Lock] = {
    planeta: Lock() for planeta in nome_planetas
}

mutex_planetas: Dict[str, Lock] = {
    planeta: Lock() for planeta in nome_planetas
}

mutex_polo_planetas: Dict[str, Dict[str, Lock]] = {
    planeta: {"North": Lock(), "South": Lock()} for planeta in nome_planetas
}

mutex_recursos_bases: Dict[str, Dict[str, Lock]] = {
    base: {"oil": Lock(), "uranium": Lock()} for base in nome_bases
}

combustivel_por_foguete: Dict[str, Dict[str, int]] = {
    'ALCANTARA': {
        nome: fuel for nome, fuel in zip(
            nome_foguetes, (70, 100, 100)
        )
    },
    'MOSCOW': {
        nome: fuel for nome, fuel in zip(
            nome_foguetes, (100, 120, 115)
        )
    },
    'CANAVERAL CAPE': {
        nome: fuel for nome, fuel in zip(
            nome_foguetes, (70, 120, 115)
        )
    },
    'MOON': {
        nome: fuel for nome, fuel in zip(
            nome_foguetes, (50, 90, None)
        )
    }
}

mutex_minas: Dict[str, Lock] = {
    nome: Lock() for nome in nome_minas
}

def get_mutex_minas(nome_mina: str) -> Lock:
    global mutex_minas
    return mutex_minas.get(nome_mina)

def get_combustivel_foguete(nome_base: str, nome_foguete: str) -> int:
    global combustivel_por_foguete
    return combustivel_por_foguete.get(nome_base).get(nome_foguete)

def get_mutex_planeta(nome_planeta: str) -> Lock:
    global mutex_planetas
    return mutex_planetas.get(nome_planeta)

def get_mutex_recurso_base(nome_base: str, recurso: str) -> Lock:
    global mutex_recursos_bases
    return mutex_recursos_bases.get(nome_base).get(recurso)

def get_mutex_polo_planeta(nome_planeta: str, polo: str) -> Lock:
    global mutex_polo_planetas
    return mutex_polo_planetas.get(nome_planeta).get(polo)

def get_mutex_terraform(nome_planeta: str) -> Lock:
    global mutex_terraform
    return mutex_terraform.get(nome_planeta)

def get_sema_foguetes(nome_base: str) -> Semaphore:
    global sema_foguetes
    return sema_foguetes.get(nome_base)

def get_nome_bases() -> Tuple[str]:
    global nome_bases
    return nome_bases

def get_nome_planetas() -> Tuple[str]:
    global nome_planetas
    return nome_planetas

def get_nome_foguetes_explosivos() -> Tuple[str]:
    global nome_foguetes_explosivos
    return nome_foguetes_explosivos

def terraformacao_esta_completa() -> bool:
    global status_terraform
    return status_terraform

def verifica_terraform() -> None:
    """Passa por todos os planetas e verifica se é necesário
    continuar a terraformação
    """
    global planets, status_terraform
    if not status_terraform:
        continuar = False
        for planeta in planets.values():
            planeta: Planet
            with planeta.mutex:
                if planeta.terraform > 0.0:
                    continuar = True
            
            if continuar:
                break

        if continuar is False:
            status_terraform = True

def get_fila_viagens(nome_base: str) -> Queue:
    global fila_viagens_base
    return fila_viagens_base.get(nome_base)

def acquire_print() -> None:
    global mutex_print
    mutex_print.acquire()

def release_print() -> None:
    global mutex_print
    mutex_print.release()

def set_planets_ref(all_planets) -> None:
    global planets
    planets = all_planets

def get_planets_ref() -> Dict[str, Planet]:
    global planets
    return planets

def set_bases_ref(all_bases) -> None:
    global bases
    bases = all_bases

def get_bases_ref() -> Dict[str, SpaceBase]:
    global bases
    return bases

def set_mines_ref(all_mines) -> None:
    global mines
    mines = all_mines

def get_mines_ref() -> Dict[str, Union[StoreHouse, Pipeline]]:
    global mines
    return mines

def set_release_system() -> None:
    global release_system
    release_system = True

def get_release_system() -> bool:
    global release_system
    return release_system

def set_simulation_time(time) -> None:
    global simulation_time
    simulation_time = time

def get_simulation_time():
    global simulation_time
    return simulation_time
