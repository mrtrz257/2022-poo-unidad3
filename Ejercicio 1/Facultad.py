from Carrera import Carrera

class Facultad:
    __codigoFacultad = 0
    __nombreFacultad = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carrera = []
    def __init__(self, codigoFacu = 0, nombreFacu = '', direc = '', local = '', telefono = '', i = 0, reader = None):
        self.__codigoFacultad = int(codigoFacu)
        self.__nombreFacultad = str(nombreFacu)
        self.__direccion = str(direc)
        self.__localidad = str(local)
        self.__telefono = str(telefono)
        if(reader!=None):
            lista = []
            band = True
            filaCarrera = next(reader)
            while band and i > 0:
                unaCarrera = Carrera(filaCarrera[1], filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5])
                lista.append(unaCarrera)
                i -= 1
                if(i > 0):
                    filaCarrera = next(reader)
            self.__carrera = lista.copy()
    def __str__(self):
        return '{} {} {} {} {}'.format(self.__codigoFacultad, self.__nombreFacultad, self.__direccion, self.__localidad, self.__telefono)
    def getCodFacultad(self):
        return self.__codigoFacultad
    def getNomFacultad(self):
        return self.__nombreFacultad
    def getLocalidad(self):
        return self.__localidad
    def mostrarCarreras(self):
        text = ''
        for elemento in self.__carrera:
            text += '{}'.format(elemento.getNombreCarrera()) + '\n'
        return text
    def getDatosCarrera(self):
        text = '{}\n'.format(self.__nombreFacultad)
        for elemento in self.__carrera:
            text += '{}'.format(elemento.getDatosCarrera()) + '\n'
        return text
    def getNombreCarrera(self, carrera):    #Verifica que el nombre de una carrera exista
        band = True
        i = 0
        x = ''
        while band and i<len(self.__carrera):
            if carrera == self.__carrera[i].getNombreCarrera():
                x = self.__carrera[i].getNombreCarrera()
                band = False
            i += 1
        return x
    def getCodigoCarrera(self, carrera):    #Busca el codigo de una carrera segun su nombre
        band = True
        i = 0
        cod = ''
        while band and i < len(self.__carrera):
            if carrera == self.__carrera[i].getNombreCarrera():
                cod = self.__carrera[i].getCodigoCarrera()
                band = False
            i += 1
        return cod
