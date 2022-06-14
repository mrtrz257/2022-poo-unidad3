from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa
from ObjectEncoder import ObjectEncoder
from Lista import Manejador

def generarJSON(lista):
    heladera1 = Heladera("Patrick", "HPK", "Negro", "Francia", 100000, 388, True, False)
    lista.agregarElemento(heladera1)
    lavarropa1 = Lavarropa("Drean", "6.06 ECO", "Blanco", "Argentina", 63000, 6, 600, 29, "Superior")
    lista.agregarElemento(lavarropa1)
    televisor1 = Televisor("Samsung", "Smart", "Negro", "Corea", 70000, "LED", 43, "4K", True)
    lista.agregarElemento(televisor1)
    d = lista.toJson()
    jsonF.guardarJSONArchivo(d, 'datosAparatos.json')
    return lista

if __name__ == '__main__':
    jsonF = ObjectEncoder()
    lista = Manejador()
    generarJSON(lista)
    #dicc = jsonF.leerJSONArchivo('datosAparatos.json')
    #aparatos = jsonF.decodificarDiccionario(dicc)
    print("/___________________/MENU/___________________/")
    opcion = int(input("Opción 1: Agregar Aparato a la Lista\nOpción 2: Mostrar Aparato en Posición Determinada\nOpción 3: Mostrar Aparatos Marca Phillips\nOpción 4: Mostrar Lavarropas con Carga Superior\nOpción 5: Mostrar Datos de Todos los Aparatos\nOpción 6: Almacenar Aparatos en archivo\nOpcion 7: Salir\nIngresar Opción: "))
    while opcion != 7:
        if opcion == 1:
            tipo = int(input("Que tipo de Aparato desea Ingresar:\n1-Heladera\n2-Televisor\n3-Lavarropa\nIngresar Opción: "))
            marca = input("Ingrese Marca: ")
            modelo = input("Ingrese Modelo: ")
            color = input("Ingrese Color: ")
            pais = input("Ingrese Pais: ")
            precio = float(input("Ingrese Precio: "))
            if tipo == 1:
                capLit = float(input("Ingresar Capacidad en Litros: "))
                freezer = bool(input("Tiene Freezer? True/False: "))
                ciclica = bool(input("Tiene Ciclica? True/False: "))
                unaHeladera = Heladera(marca, modelo, color, pais, precio, capLit, freezer, ciclica)
                lista.agregarAparato(unaHeladera)
            elif tipo == 2:
                pantalla = input("Ingresar Tipo de Pantalla: ")
                pulg = int(input("Ingresar cantidad de pulgadas: "))
                definicion = input("Ingresar Tipo de Definición: ")
                internet = bool(input("Tiene conexion a Internet? True/False: "))
                unTelevisor = Televisor(marca, modelo, color, pais, precio, pantalla, pulg, definicion, internet)
                lista.agregarAparato(unTelevisor)
            elif tipo == 3:
                capLav = int(input("Ingrese Capacidad de Lavado: "))
                velCentr = int(input("Ingrese Velocidad de Centrifugado: "))
                cantProg = int(input("Ingrese Cantidad de Programas: "))
                tipoCarga = input("Ingrese Tipo de Carga: ")
                unLavarropa = Lavarropa(marca, modelo, color, pais, precio, capLav, velCentr, cantProg, tipoCarga)
                lista.agregarAparato(unLavarropa)
        elif opcion == 2:
            posicion = int(input("Ingresar Posicion del Aparato: "))
            objeto = lista.mostarElemento(posicion)
            print(objeto)
        elif opcion == 3:
            AparatosPhillips = lista.mostrarSegunMarca()
            print("Cantidad de Aparatos Marca Phillips: {}".format(AparatosPhillips))
        elif opcion == 4:
            AparatosCargaSup = lista.mostrarSegunCarga()
            print("Marcas de Lavarropas con carga superior: ")
            print(AparatosCargaSup)
        elif opcion == 5:
            lista.listarDatos()
        elif opcion == 6:
            d = lista.toJson()
            jsonF.guardarJSONArchivo(d, 'datosAparatos.json')
        else:
            print("Opcion No Corresponde")
        print("/___________________/MENU/___________________/")
        opcion = int(input("Opción 1: Agregar Aparato a la Lista\nOpción 2: Mostrar Aparato en Posición Determinada\nOpción 3: Mostrar Aparatos Marca Phillips\nOpción 4: Mostrar Lavarropas con Carga Superior\nOpción 5: Mostrar Datos de Todos los Aparatos\nOpción 6: Almacenar Aparatos en archivo\nOpcion 7: Salir\nIngresar Opción: "))
