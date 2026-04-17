from Punto2.models.vehiculos import Vehiculo, Coche, Bicicleta, Camioneta, Motocicleta
from Punto2.models.objetos import Garaje
from Punto2.models.metodos import CatalogarVehiculos, CatalogarVehiculosPorRuedas
from Punto1.models.objetos import crear_figuras, mostrar_figuras

def menu_punto1():
    figuras = crear_figuras()
    mostrar_figuras(figuras)

def menu_punto2():
    vehiculos = []
    while True:
        print("\n--- Punto 2: Gestión de Vehículos ---")
        print("1. Cargar vehículos del garaje")
        print("2. Catalogar todos los vehículos")
        print("3. Catalogar por número de ruedas")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            vehiculos = Garaje()
        elif opcion == "2":
            if not vehiculos:
                print("⚠ Primero carga los vehículos (opción 1)")
            else:
                CatalogarVehiculos(vehiculos)
        elif opcion == "3":
            if not vehiculos:
                print("⚠ Primero carga los vehículos (opción 1)")
            else:
                try:
                    ruedas = int(input("Número de ruedas: "))
                    CatalogarVehiculosPorRuedas(vehiculos, ruedas)
                except ValueError:
                    print("⚠ Ingresa un número válido")
        elif opcion == "4":
            break
        else:
            print("Opción no válida")


def menu_principal():
    while True:
        print("\n========== TALLER VII ==========")
        print("1. Punto 1 - Figuras geométricas")
        print("2. Punto 2 - Vehículos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_punto1()
        elif opcion == "2":
            menu_punto2()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu_principal()