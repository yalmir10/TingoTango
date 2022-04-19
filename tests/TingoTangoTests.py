import unittest
from src.logica.TingoTango import TingoTango

class TingoTangoPrueba(unittest.TestCase):
    def setUp(self):
        self.TT = TingoTango()

    def tearDown(self):
        self.TT = None

    def test_TingoTango_multiploTres_retornaTingo(self):
        # Arrange
            self.numero = 3
            self.resultadoEsperado = "Tingo"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero)
        #Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)

    def test_TingoTango_multiploCinco_retornaTango(self):
        # Arrange
            self.numero = 5
            self.resultadoEsperado = "Tango"
        # Do
            self.resultadoActual = self.TT.textoTingoTango(self.numero)
        #Assert
            self.assertEqual(self.resultadoEsperado,self.resultadoActual)

    def test_TingoTango_multiploquince_retornaTingoTango(self):
        # Arrange
        self.numero = 15
        self.resultadoEsperado = "TingoTango"
        # Do
        self.resultadoActual = self.TT.textoTingoTango(self.numero)
        # Assert
        self.assertEqual(self.resultadoEsperado, self.resultadoActual)

    def test_TingoTango_otroNumero_retornaNumero(self):
        # Arrange
        self.numero = 7
        self.resultadoEsperado = "7"
        # Do
        self.resultadoActual = self.TT.textoTingoTango(self.numero)
        # Assert
        self.assertEqual(self.resultadoEsperado, self.resultadoActual)

    def test_TingoTango_multiplo_retornaStr(self):
        # Arrange
        self.numero = 'a'
        self.resultadoEsperado = None
        # Do
        self.resultadoActual = self.TT.textoTingoTango(self.numero)
        # Assert
        self.assertEqual(self.resultadoEsperado, self.resultadoActual)
