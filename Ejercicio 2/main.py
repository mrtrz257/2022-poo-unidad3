from ManejadorFlores import ManejadorFlores
from ManejadorRamo import ManejadorRamo

from Flores import Flores
from Ramo import Ramo

def test():
    testFlor1 = Flores(9, "Aciano", "Azul", "'Planta herbácea anual de raíz axial, llega a medir un metro de altura'")
    testFlor2 = Flores(10, "Lila", "Lila", "'Grandes Arbustos o Pequeños arboles'")
    testRamo1 = Ramo("Grande", testFlor1)
    testRamo1.addFlor(testFlor2)
    testRamo2 = Ramo("Medio", testFlor2)
    print(testRamo1)
    print(testRamo2)

if __name__ == '__main__':
    test()
    flores = ManejadorFlores()
    ramos = ManejadorRamo()
    flores.crearArreglo()
    print("/--------------------/MENU/--------------------/")
    opcion = int(input("Opción 1: Crear un Ramo y cargar Flores\nOpción 2: Mostrar las 5 Flores más vendidas\nOpción 3: Mostrar Flores vendidas según Tipo de Ramo\nOpción 4: Salir\nIngresar Opción: "))
    while opcion != 4:
        if opcion == 1:
            tamanioRamo = input("Ingresar Tamaño del Ramo (Grande/Mediano/Pequeño): ")
            print("Lista de Flores:")
            print(flores.mostrarArreglo())
            codigoFlor = input("Ingrese Codigo de Flor para añadir al Ramo: ")
            verificarFlor = flores.buscarFlor(codigoFlor)
            indice = None
            if verificarFlor != -1:
                flor = flores.getFlor(verificarFlor)
                indice = ramos.CrearRamo(tamanioRamo, flor)
                flores.registrarVenta(verificarFlor)
                print(ramos.mostrarRamo())
            else:
                print("Codigo de Flor no Corresponde")
            agregarFlor = int(input("Desea Agregar más Flores al Ramo?\nSi: Ingresar 1\nNo: Ingresar 0\nIngresar Opción: "))
            if agregarFlor == 1:
                cantidadDeFlores = int(input("Ingrese cantidad de Flores para añadir al ramo (Maximo 3): "))
                if cantidadDeFlores <= 3:
                    for i in range(cantidadDeFlores):
                        print("Lista de Flores:")
                        print(flores.mostrarArreglo())
                        codigoFlor = input("Ingrese Codigo de Flor para añadir al Ramo: ")
                        verificarFlor = flores.buscarFlor(codigoFlor)
                        if verificarFlor != -1:
                            flor = flores.getFlor(verificarFlor)
                            ramos.agregarFlorARamo(indice, flor)
                            flores.registrarVenta(verificarFlor)
                            print(ramos.mostrarRamo())
                        else:
                            print("No se Encontro Codigo De Flor")

                else:
                    print("Cantidad No Permitida")
        elif opcion == 2:
            print("Top 5 Flores más Vendidas:")
            print(flores.mostrarFloresMasVendidas())
        elif opcion == 3:
            tipoDeRamo = input("Ingrese tipo de Ramo (Grande/Mediano/Pequeño): ")
            x = ramos.mostrarRamoSegunTamano(tipoDeRamo)
            if len(x)>0:
                print("Flores vendidas en Ramos de Tamaño {}:".format(tipoDeRamo))
                print(x)
            else:
                print("No se encontro Ramos con Tamaño indicado")
        else:
            print("Opción No Permitida")
        print("/--------------------/MENU/--------------------/")
        opcion = int(input("Opción 1: Crear un Ramo y cargar Flores\nOpción 2: Mostrar las 5 Flores más vendidas\nOpción 3: Mostrar Flores vendidas según Tipo de Ramo\nOpción 4: Salir\nIngresar Opción: "))
