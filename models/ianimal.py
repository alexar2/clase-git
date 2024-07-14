#Presentado por Alexandra Roberto
#Modulo 2 Taller 3 Pruebas y Errores - Parte 1

from abc import ABC, abstractmethod

class iAnimal(ABC):
    @abstractmethod
    def comer(self, kilos):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass