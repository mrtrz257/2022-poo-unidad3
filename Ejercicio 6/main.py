from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa
from ObjectEncoder import ObjectEncoder

if __name__ == '__main__':
    band = True
    jsonF = ObjectEncoder()
    dicc = jsonF.leerJSONArchivo('aparatosElectricos.json')
    Manejador = jsonF.decodificarDiccionario(dicc)

