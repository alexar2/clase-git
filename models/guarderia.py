#clase alimentar_boa, configurada con estructura try
from models.boa import BoaConstrictor
from models.huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [
            BoaConstrictor("BoaPepita", 10, 5, "Brazil", 100), #nombre, peso, edad, pais_origen, impuestos
            BoaConstrictor("BoaLolita", 12, 7, "Peru", 120) #nombre, peso, edad, pais_origen, impuestos
        ]
        self.hurones = [
            Huron("HuronPablo", 3, 2, "Argentina", 1500), #nombre, peso, edad, pais_origen, impuestos
            Huron("HuronPedro", 2.5, 3, "Chile", 1200) #nombre, peso, edad, pais_origen, impuestos
        ]

    def alimentar_boa(self, boa):
        if boa is None:
            raise ValueError("Esta Boa no existe!")

        try:
            resultado = boa.agregar_raton()
            if resultado == "Éxito":
                return "Éxito"
            else:
                return "La boa está llena"
        except ValueError as e:
            return str(e)
