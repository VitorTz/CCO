from random import randrange, random, choice
from time import sleep
from stars.planet import Planet
import globals


class Rocket:

    ################################################
    # O CONSTRUTOR DA CLASSE NÃO PODE SER ALTERADO #
    ################################################
    def __init__(self, type):
        self.id = randrange(1000)
        self.name = type
        if(self.name == 'LION'):
            self.fuel_cargo = 0
            self.uranium_cargo = 0

    def get_fuel_necessario(self, nome_base: str) -> int:
        """Retorna o combustivel necessário para produzir o foguete"""
        return globals.get_combustivel_foguete(nome_base, self.name)

    def get_uranium_necessario(self, nome_base: str) -> int:
        """Retorna o uranium necessário para produzir o foguete"""
        return 35

    def nuke(self, planet: Planet):
        """
        Faz a detonação do foguete.
        A detonação pode ser feita no polo norte ou sul,
        cada polo tem um mutex que deve ser adqurido para realizar a detonação
        Deste modo o número máximo de detonações simultaneas no planeta é 2
        e o número máximo de detonações simultaneas em cada polo é 1
        """
        # Obtem o mutex do planeta para verifica o nível de terraformação
        planet.mutex.acquire()
        if planet.terraform > 0.0:
            # Libera o mutex após verificar a terraformação
            planet.mutex.release() 
            # Escolhe um polo e obtem o mutex correspondente para fazer a detonação
            polo = choice(("North", "South"))
            mutex_polo = planet.mutex_north if polo == "North" else planet.mutex_south
            with mutex_polo:
                with planet.mutex_terraform:
                    planet.terraform -= self.damage()
            print(f"[EXPLOSION] - The {self.name} ROCKET reached the planet {planet.name} on {polo} Pole")
        else:
            planet.mutex.release()
        
    def voyage(self, planet):
        self.simulation_time_voyage(planet)
        return self.do_we_have_a_problem()

    ####################################################
    #                   ATENÇÃO                        # 
    #     AS FUNÇÕES ABAIXO NÃO PODEM SER ALTERADAS    #
    ###################################################
    def simulation_time_voyage(self, planet):
        if planet.name == 'MARS':
            sleep(2) # Marte tem uma distância aproximada de dois anos do planeta Terra.
        else:
            sleep(5) # IO, Europa e Ganimedes tem uma distância aproximada de cinco anos do planeta Terra.

    def do_we_have_a_problem(self):
        if(random() < 0.15):
            if(random() < 0.51):
                self.general_failure()
                return True
            else:
                self.meteor_collision()
                return True
        return False
            
    def general_failure(self):
        print(f"[GENERAL FAILURE] - {self.name} ROCKET id: {self.id}")
    
    def meteor_collision(self):
        print(f"[METEOR COLLISION] - {self.name} ROCKET id: {self.id}")

    def successfull_launch(self, base):
        if random() <= 0.1:
            print(f"[LAUNCH FAILED] - {self.name} ROCKET id:{self.id} on {base.name}")
            return False
        return True
    
    def damage(self):
        return random()

    def launch(self, base, planet):
        if(self.successfull_launch(base)):
            print(f"[{self.name} - {self.id}] launched.")
            self.voyage(planet)        
