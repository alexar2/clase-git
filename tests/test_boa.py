#Presentado por Alexandra Roberto
#Modulo 2 Taller 3 Pruebas y Errores - Parte 1

import unittest
from models.boa import BoaConstrictor

##clase enfocada a pruebas de las Boas
class TestBoa(unittest.TestCase):
# Prueba Punto 1 Pruebas Unitarias       
    def test_hacer_sonido(self): #test hacer sonido
        boa = BoaConstrictor("Boa_Constrictora", 10, 20, "Mexico", 300) #nombre, peso, edad, pais_origen, impuestos
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!") #devuelve el string Tsss

    def test_calcular_flete(self): #test calcular flete
        boa = BoaConstrictor("Boa_Constrictora", 10, 20, "Mexico", 300) #nombre, peso, edad, pais_origen, impuestos
        self.assertEqual(boa.calcular_flete(), 300 * 10) # devuelva la operación correcta de impuesto*peso

    def test_agregar_raton(self): #test alimentar a las Boas
        boa = BoaConstrictor("Boa_Constrictora", 10, 20, "Mexico", 300) #nombre, peso, edad, pais_origen, impuestos
        boa.agregar_raton()
        self.assertEqual(boa.ratones_comidos, 1)#compara los ratones comidos después de agregar raton
# Prueba Punto 2 Muchos Ratones
    def test_agregar_raton_condicion (self): #Punto 2 Muchos Ratones
        boa = BoaConstrictor("Boa_Constrictora", 10, 20, "Mexico", 300)
        
        # Probamos agregar ratones hasta el límite
        for _ in range(10):
            self.assertEqual(boa.agregar_raton(), "Éxito")
        
        # Ahora probamos agregar un ratón más para verificar la condición
        with self.assertRaises(ValueError) as context:
            boa.agregar_raton()

        self.assertEqual(str(context.exception), "Demasiados Ratones!")


