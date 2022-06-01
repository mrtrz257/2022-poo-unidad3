from CalefactorElectrico import CalefactorElectrico
from CalefactorAGas import CalefactorAGas
from Coleccion import Coleccion
import csv

def test():
    calElectrico1 = CalefactorElectrico("Magiclick", "C1009", 2000, None, None)
    calAGas1 = CalefactorAGas("Eskabe", "S21 MX 3",None ,"GN01-00001-06-057", 3000)
    calElectrico2 = CalefactorElectrico("Peabody", "PE-VC20", 2500, None, None)
    calAGas2 = CalefactorAGas("Emege", "3150 SCE",None, "01-1017-23-007", 5000)
    print(calElectrico1, calElectrico2)
    print(calAGas1, calAGas2)

def ArchivoCalefElectricos(arreglo):
    archivo = open('calefactor-electrico.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        unCalefactorElec = CalefactorElectrico(fila[0], fila[1], fila[2], None, None)
        arreglo.agregarCalefactor(unCalefactorElec)
    archivo.close()

def ArchivoCalefAGas(arreglo):
    archivo = open('calefactor-a-gas.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        unCalefactorAGas = CalefactorAGas(fila[0], fila[1],None, fila[2], fila[3])
        arreglo.agregarCalefactor(unCalefactorAGas)
    archivo.close()

if __name__ == '__main__':
    #test()
    arreglo = Coleccion()
    cantidadDeCalefactores = int(input("Ingresar Cantidad de Calefactores para agregar(Maximo 8): "))
    arreglo.crearArreglo(cantidadDeCalefactores)
    ArchivoCalefElectricos(arreglo)
    ArchivoCalefAGas(arreglo)
    print(arreglo.mostrarArreglo())

