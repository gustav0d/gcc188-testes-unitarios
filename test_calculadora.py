import unittest
from calculadora import somar, subtrair, multiplicar, dividir, potencia, calcular_media


class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        """Testa soma em diferentes combinações de valores."""
        casos = [
            (2, 3, 5),
            (0, 5, 5),
            (0, 0, 0),
            (-3, 5, 2),
            (-2, -3, -5),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(somar(a, b), esperado)

    def test_subtrair(self):
        """Testa subtração com resultados positivos, negativos e zero."""
        casos = [
            (10, 3, 7),
            (3, 10, -7),
            (0, 0, 0),
            (-5, -3, -2),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtrair(a, b), esperado)

    def test_multiplicar(self):
        """Testa multiplicação com positivos, zero e negativos."""
        casos = [
            (3, 4, 12),
            (5, 0, 0),
            (-2, 3, -6),
            (-2, -3, 6),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplicar(a, b), esperado)

    def test_dividir(self):
        """Testa divisão exata, decimal, negativa e zero no numerador."""
        casos = [
            (10, 2, 5.0),
            (7, 2, 3.5),
            (-9, 3, -3.0),
            (0, 5, 0.0),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(dividir(a, b), esperado)

    def test_dividir_por_zero(self):
        """Divisão por zero deve lançar ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

    def test_potencia(self):
        """Testa potenciação com expoente positivo, zero e negativo."""
        casos = [
            (2, 3, 8),
            (5, 0, 1),
            (10, 2, 100),
            (2, -1, 0.5),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)

    def test_calcular_media(self):
        """Testa média com inteiros, decimais, negativos, um elemento e zeros."""
        casos = [
            ([1, 2, 3, 4], 2.5),
            ([1.5, 2.5], 2.0),
            ([-2, -4], -3.0),
            ([7], 7.0),
            ([0, 0, 0], 0.0),
        ]
        for lista, esperado in casos:
            with self.subTest(lista=lista):
                self.assertEqual(calcular_media(lista), esperado)

    def test_calcular_media_lista_vazia(self):
        """Lista vazia deve lançar ValueError."""
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()
