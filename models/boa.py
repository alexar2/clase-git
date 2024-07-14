#Presentado por Alexandra Roberto
#Modulo 2 Taller 3 Pruebas y Errores - Parte 1

from models.animalexotico import Animal_Exotico

class BoaConstrictor(Animal_Exotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self)->str:
        return "¡Tsss!"

    def comer_raton(self)->None:
        return self.ratones_comidos
#Parámetro: si tiene 10 o mas retorne "la boa esta llena" - si tiene menos de 10, +1 al contador y retorne "Éxito"

    def agregar_raton(self):
        self.ratones_comidos += 1
    
    def agregar_raton_condicion (self):
        if self.ratones_comidos >= 10:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1
        return "Éxito"