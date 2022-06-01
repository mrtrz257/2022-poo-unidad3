from Calefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __PotenciaMax = None
    def __init__(self, marca, modelo, potencia, matricula, calorias):
        super().__init__(marca, modelo, potencia, matricula, calorias)
        self.__PotenciaMax = int(potencia)
    def __str__(self):
        text = 'Marca: {} - Modelo: {} - '.format(self.getMarca(), self.getModelo())
        text += 'Potencia Maxima: {} Watts\n'.format(self.__PotenciaMax)
        return text
    def getPotencia(self):
        return self.__PotenciaMax
