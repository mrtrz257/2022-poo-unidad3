from Calefactor import Calefactor

class CalefactorAGas(Calefactor):
    __matricula = None
    __calorias = None
    def __init__(self, marca, modelo, potencia, matricula, calorias):
        super().__init__(marca, modelo, potencia, matricula, calorias)
        self.__matricula = str(matricula)
        self.__calorias = int(calorias)
    def __str__(self):
        text = 'Marca: {} - Modelo: {} - '.format(self.getMarca(), self.getModelo())
        text += 'Matricula: {} - '.format(self.__matricula)
        text += '{} kilocalorias/m3\n'.format(self.__calorias)
        return text
    def getMatricula(self):
        return self.__matricula
    def getCalorias(self):
        return self.__calorias
