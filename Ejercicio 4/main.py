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
    test()
    arreglo = Coleccion()
    cantidadDeCalefactores = int(input("Ingresar Cantidad de Calefactores para agregar(Maximo 8): "))
    if cantidadDeCalefactores <= 8:
        arreglo.setDimensionArreglo(cantidadDeCalefactores)
        ArchivoCalefElectricos(arreglo)
        ArchivoCalefAGas(arreglo)
        #print(arreglo.mostrarArreglo())
        print("/--------------------/MENU/--------------------/")
        opcion = int(input("Opción 1: Mostrar Calefactor a Gas de menor costo de Consumo\nOpción 2: Mostrar Calefactor Electrico de Menor costo de Consumo\nOpción 3: Mostrar Datos de Calefactor de Menor Consumo\nOpción 4: Salir\nIngresar Opción: "))
        while opcion != 4:
            if opcion == 1:
                costo = float(input("Ingresar Costo por m3: "))
                cantidadAConsumir = float(input("Ingresar Cantidad que estima consumir en m3: "))
                calefactorAgasMin = arreglo.calcularConsumoMinimoAGas(cantidadAConsumir, costo)
                print(arreglo.mostrarNombreCalefactor(calefactorAgasMin))
            elif opcion == 2:
                costo = float(input("Ingresar Costo del Kilowatt/H: "))
                cantidadAConsumir = float(input("Ingresar Cantidad que estima consumir por hora: "))
                calefactorElectricoMin = arreglo.calcularConsumoMinimoElectrico(cantidadAConsumir, costo)
                print(arreglo.mostrarNombreCalefactor(calefactorElectricoMin))
            elif opcion == 3:
                costo = float(input("Ingresar Costo: "))
                cantidadAConsumir = float(input("Ingresar Cantidad estimada a Consumir: "))
                calefactorMinimo = arreglo.calcularConsumoMinimoGeneral(cantidadAConsumir, costo)
                print(arreglo.mostrarDatosCalefactor(calefactorMinimo))
            else:
                print("Opción No Corresponde")
            print("/--------------------/MENU/--------------------/")
            opcion = int(input("Opción 1: Mostrar Calefactor a Gas de menor costo de Consumo\nOpción 2: Mostrar Calefactor Electrico de Menor costo de Consumo\nOpción 3: Mostrar Datos de Calefactor de Menor Consumo\nOpción 4: Salir\nIngresar Opción: "))
    else:
        print("Cantidad No Permitida")
        