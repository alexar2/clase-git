#Presentado por Alexandra Roberto
#Modulo 2 Taller 3 Pruebas y Errores - Parte 1

from models.animal import Animal
from abc import ABC, abstractmethod

class Animal_Exotico(Animal,ABC):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self):
        return round(self.impuestos * self.peso, 2)
        
    @abstractmethod
    def hacer_sonido (self):
        pass