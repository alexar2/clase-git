#Presentado por Alexandra Roberto
#Modulo 2 Taller 3 Pruebas y Errores - Parte 1

from models.ianimal import iAnimal
from abc import ABC, abstractmethod

class Animal(iAnimal,ABC):
    def __init__(self, nombre, peso, edad):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.kilos_comidos = 0

    def obtener_nombre(self):
        return self.nombre

    def obtener_peso(self):
        return self.peso

    def obtener_edad(self):
        return self.edad

    def comer(self, kilos):
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self.kilos_comidos
    
    @abstractmethod
    def hacer_sonido (self):
        pass