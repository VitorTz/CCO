from threading import Thread, Lock
import globals

class Planet(Thread):

    ################################################
    # O CONSTRUTOR DA CLASSE NÃO PODE SER ALTERADO #
    ################################################
    def __init__(self, terraform,name):
        Thread.__init__(self)
        self.terraform = terraform
        self.name = name
    
    @property
    def mutex(self) -> Lock:
        """Mutex que representa o satelite que retorna dados do planeta"""
        return globals.get_mutex_planeta(self.name)

    @property
    def mutex_terraform(self) -> Lock:
        """Mutex que protege o nivel de terraformação do planeta"""
        return globals.get_mutex_terraform(self.name)
    
    @property
    def mutex_north(self) -> Lock:
        """Mutex das detonações no polo norte"""
        return globals.get_mutex_polo_planeta(self.name, "North")
    
    @property
    def mutex_south(self) -> Lock:
        """Mutex das detonações no polo sul"""
        return globals.get_mutex_polo_planeta(self.name, "South")

    def nuke_detected(self):
        while(self.terraform > 0):
            before_percentage = self.terraform
            while(before_percentage == self.terraform):
                pass
            print(f"[NUKE DETECTION] - The planet {self.name} was bombed. {self.terraform}% UNHABITABLE")

    def print_planet_info(self):
        print(f"🪐 - [{self.name}] → {self.terraform}% UNINHABITABLE")

    def run(self):
        globals.acquire_print()
        self.print_planet_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while not globals.terraformacao_esta_completa():
            self.nuke_detected()