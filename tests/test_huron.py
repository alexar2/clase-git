#Presentado por Alexandra Roberto
#Modulo 2 Taller 3 Pruebas y Errores - Parte 1

import unittest
from models.huron import Huron

##clase enfocada a pruebas de los Hurones
class TestHuron(unittest.TestCase):
        
    def test_hacer_sonido(self): #test para saber que es caso de prueba
        huron = Huron("Huron", 3.4, 8, "Argentina", 15) #nombre, peso, edad, pais_origen, impuestos
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!") #devuelve el string Eek Eek

    def test_calcular_flete(self): #test calcular flete
        huron = Huron("Huron", 3.4, 8, "Argentina", 15) #nombre, peso, edad, pais_origen, impuestos
        self.assertEqual(huron.calcular_flete(), 15 * 3.4) #devuelva la operación correcta de impuesto*peso