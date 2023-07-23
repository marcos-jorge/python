import unittest
from Matriz import sumaFilas
from Matriz import sumaColumnas

class TestMatriz(unittest.TestCase):

    def test_suma_filas(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        suma_filas = sumaFilas(matriz)
        self.assertEqual(suma_filas, [6, 15, 24])

    def test_suma_columnas(self):
        matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        suma_columnas = sumaColumnas(matriz)
        self.assertEqual(suma_columnas, [12, 15, 18])

if __name__ == '__main__':
    unittest.main()