from threading import Thread, Lock
from time import sleep

import globals


######################################################################
#                                                                    #
#              Não é permitida a alteração deste arquivo!            #
#                                                                    #
######################################################################

class Pipeline(Thread):

    def __init__(self, unities, location, constraint):
        Thread.__init__(self)
        self.unities = unities
        self.location = location
        self.constraint = constraint
    
    @property
    def mutex(self) -> Lock:
        """Mutex que protege as alterações no atributo unities"""
        return globals.get_mutex_minas("oil_earth")

    def print_pipeline(self):
        print(
            f"🔨 - [{self.location}] - {self.unities} oil unities are produced."
        )

    def produce(self):
        """
        A alteração feita em unities é protegida
        por um mutex. Tanto bases que estão reabastecendo
        quanto a própria mina podem fazer alterações em unities.
        Deste modo a mina está ou produzindo ou cedendo recursos
        para as bases.
        """
        with self.mutex:
            # Aumenta a produção já a posse do mutex que possibilita
            # alterações em unities fica revezando muitas vezes
            for _ in range(20):
                if (self.unities < self.constraint):
                    self.unities += 17
                    self.print_pipeline()
                    sleep(0.001)
                else:
                    break

    def run(self):
        globals.acquire_print()
        self.print_pipeline()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while not globals.terraformacao_esta_completa():
            self.produce()
