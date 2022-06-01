from Facultad import Facultad

from ManejadorFacultad import ManejadorFacultad

def test():
    testFacultad = Facultad(7, "Universidad Catolica de Cuyo", "Av. Ignacio de la Roza 1516", "Rivadavia, San Juan", "0264 429-2300", None, None)
    print(testFacultad)

if __name__ == '__main__':
    test()
    facultades = ManejadorFacultad()
    facultades.crearFacultad()
    print("/=======================/MENU/=======================/")
    opcion = int(input("Opción 1: Mostrar Nombre y Duración de Carreras de una Facultad\nOpción 2: Mostrar Datos de una Facultad según Nombre de Carrera\nOpción 3: Salir\nIngresar Opción: "))
    while opcion != 3:
        if opcion == 1:
            codigoFacultad = int(input("Ingrese codigo de Facultad: "))
            datos = facultades.DatosCarrera(codigoFacultad)
            if len(datos)<1:
                print("No se encontro codigo de Facultad")
            else:
                print(datos)
        elif opcion == 2:
            nomCarrera = input("Ingresar Nombre de Carrera: ")
            codigoFac = facultades.buscarCodigoFacultad(nomCarrera)
            if codigoFac != -1:
                print('Codigo de Carrera: {}'.format(facultades.buscarCodigoCarrera(nomCarrera)))
                print('{}'.format(facultades.getDatosFacultad(codigoFac+1)))
            else:
                print("No se encontro Carrera")
        else:
            print("Opción No Corresponde")
        print("/=======================/MENU/=======================/")
        opcion = int(input("Opción 1: Mostrar Nombre y Duración de Carreras de una Facultad\nOpción 2: Mostrar Datos de una Facultad según Nombre de Carrera\nOpción 3: Salir\nIngresar Opción: "))
