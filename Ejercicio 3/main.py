from Equipo import Equipo
from Jugador import Jugador
from Contrato import Contrato

import csv
from ManejadorEquipos import ManejadorEquipos
from ManejadorJugadores import ManejadorJugadores
from ManejadorContratos import ManejadorContratos

def test():
    equipo1 = Equipo("Boca Juniors", "Buenos Aires")
    jugador1 = Jugador("Juan Ramirez", "25000256", "Buenos Aires", "Argentina", "25/05/1993")
    jugador2 = Jugador("Guillermo Fernandez", "23340266", "Santa Fe", "Argentina", "11/10/1991")
    equipo1.ContratarJugador("30/07/2021", "31/12/2024", 5500000, jugador1)
    equipo1.ContratarJugador("30/01/2021", "31/12/2024", 6500000, jugador2)
    equipo1.mostrarContratos()

def archivoEquipos(arregloEquipos):
    archivo = open('Equipos.csv')
    reader = csv.reader(archivo, delimiter=';')
    band = False
    for fila in reader:
        if band == False:
            dimension = int(fila[0])
            arregloEquipos.setDimensionArreglo(dimension)
            band = True
        else:
            unEquipo = Equipo(fila[0], fila[1])
            arregloEquipos.agregarArregloEquipos(unEquipo)
    archivo.close()
    return arregloEquipos

def archivoJugadores(listaJugadores):
    archivo = open('jugadores.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        unJugador = Jugador(fila[0], fila[1], fila[2], fila[3], fila[4])
        listaJugadores.agregarJugador(unJugador)
    archivo.close()
    return listaJugadores

if __name__ == '__main__':
    test()
    print("--------------------------------------")
    arregloEquipos = ManejadorEquipos()
    archivoEquipos(arregloEquipos)
    print(arregloEquipos.mostrarEquipos())
    listaJugadores = ManejadorJugadores()
    archivoJugadores(listaJugadores)
    print(listaJugadores.mostrarListaJugadores())
    arregloContratos = ManejadorContratos()
    cantidadDeContratos = 0
    print("/---------------------/MENU/---------------------/")
    opcion = int(input("Opción 1: Generar Contrato\nOpción 2: Buscar Contrato Segun DNI\nOpción 3: Ver Contratos que vencen en 6 Meses\nOpcion 4: Mostrar Importe Total de Contratos de un Equipo\nOpción 5: Generar Archivo con Contratos Generados\nOpcion 6: Salir\nElegir Opción: "))
    while opcion != 6:
        if opcion == 1:
            nombreEquipo = input("Ingrese nombre de Equipo para Generar Contrato: ")
            verificarEquipo = arregloEquipos.buscarEquipo(nombreEquipo)
            if verificarEquipo != -1:
                equipo = arregloEquipos.getEquipo(verificarEquipo)
                nombreJugador = input("Ingrese nombre y Apellido de Jugador: ")
                verificarJugador = listaJugadores.buscarJugador(nombreJugador)
                if verificarJugador != -1:
                    jugador = listaJugadores.getJugador(verificarJugador)
                    inicioContrato = input("Ingrese Fecha de Inicio de Contrato (Formato Dia/Mes/Año): ")
                    finContrato = input("Ingrese Fecha de Finalizacion de Contrato (Formato Dia/Mes/Año): ")
                    pagoMensual = int(input("Ingrese Sueldo Mensual: "))
                    unContrato = Contrato(inicioContrato, finContrato, pagoMensual, jugador, equipo)
                    cantidadDeContratos += 1
                    arregloContratos.setDimensionArreglo(cantidadDeContratos)
                    arregloContratos.agregarArregloContratos(unContrato)
                    arregloEquipos.agregarContrato(verificarEquipo, unContrato)
                    print(unContrato)
                else:
                    print("No se Encontro Jugador")
            else:
                print("No se Encontro Equipo")
        elif opcion == 2:
            dni = input("Ingresar DNI de Jugador: ")
            verificaContrato = arregloContratos.buscarJugador(dni)
            if verificaContrato != -1:
                print(arregloContratos.muestraEquipoYContrato(verificaContrato))
            else:
                print("No se encontro Jugador con DNI Ingresado o No existe Contrato")
        elif opcion == 3:
            nombreEquipo = input("Ingresar Nombre de Equipo: ")
            verificarEquipo = arregloEquipos.buscarEquipo(nombreEquipo)
            if verificarEquipo != -1:
                contratos = arregloEquipos.contratosSeisMeses(verificarEquipo)
                print('{}'.format(contratos))
            else:
                print("No se Encontro Equipo")
        elif opcion == 4:
            nombreEquipo = input("Ingrese Nombre de Equipo: ")
            verificarEquipo = arregloEquipos.buscarEquipo(nombreEquipo)
            if verificarEquipo != -1:
                importe = arregloEquipos.ImporteTotal(verificarEquipo)
                print('Importe Total (Mensual) de Sueldos del Equipo: ${}'.format(importe))
            else:
                print("No se Encontro Equipo")
        elif opcion == 5:
            arregloContratos.guardarArchivoContratos()
            print("Archivo con Contratos Guardados Generado")
        else:
            print("Opción Ingresada No Corresponde")
        print("/---------------------/MENU/---------------------/")
        opcion = int(input("Opción 1: Generar Contrato\nOpción 2: Buscar Contrato Segun DNI\nOpción 3: Ver Contratos que vencen en 6 Meses\nOpcion 4: Mostrar Importe Total de Contratos de un Equipo\nOpción 5: Generar Archivo con Contratos Generados\nOpcion 6: Salir\nElegir Opción: "))
