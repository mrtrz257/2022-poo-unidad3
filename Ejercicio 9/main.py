import unittest
from Palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo = None
    def setUp(self):
        self.__palindromo = Palindromo('ana')
    def testPalindromo1(self):
        self.assertTrue(self.__palindromo.esPalindromo())
    def testPalindromo2(self):
        self.__palindromo.setPalabra('ANA')
        self.assertTrue(self.__palindromo.esPalindromo())
    def testPalindromo3(self):
        self.__palindromo.setPalabra('menem')
        self.assertTrue(self.__palindromo.esPalindromo())
    def testPalindromo4(self):
        self.__palindromo.setPalabra('MENEM')
        self.assertTrue(self.__palindromo.esPalindromo())
    def testPalindromo5(self):
        self.__palindromo.setPalabra('Palabra')
        self.assertTrue(self.__palindromo.esPalindromo())

if __name__ == '__main__':
    unittest.main()
