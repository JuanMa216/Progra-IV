from punto1 import Coche, ciudadDestino, Vehiculo
from punto2 import Coche_P2, Bicicleta_P2, Camion, Motocicleta, CategoriaVehiculo, CategoriaVehiculoRuedas
from punto3 import *
from punto4 import *

def separador(caracter="=", largo=70):
    print(caracter * largo)


def titulo(texto):
    separador("=")
    print(texto.center(70))
    separador("=")


def esperar_enter():
    input("\nPresiona Enter para volver al menú...")


def Menu():
    while True:
        titulo("TALLER V - PROGRAMACION ORIENTADA A OBJETOS")
        print("Selecciona una opción:")
        print("  1) Punto 1 - Pruebas de clases y métodos")
        print("  2) Punto 2")
        print("  3) Punto 3")
        print("  4) Punto 4")
        print("  5) Salir")
        separador("-")

        punto_opcion = input("Ingresa tu opción: ").strip()

        if punto_opcion == "1":
            punto1()
            esperar_enter()
        elif punto_opcion == "2":
            punto2()
            esperar_enter()
        elif punto_opcion == "3":
            punto3()
            esperar_enter()
            break
        elif punto_opcion == "4":
            punto4()
            esperar_enter()
        elif punto_opcion == "5":
            print("Saliendo...")
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.\n")

def punto1():
    titulo("PUNTO 1 - PRUEBAS DE CLASES Y METODOS")

    pruebas = [
        {
            "nombre": "Coche hacia Bogota",
            "vehiculo": Vehiculo("rojo", 4, "coche"),
            "destino": ciudadDestino("Bogota"),
            "esperado_info": "coches",
            "esperado_combustible": "gasolina",
            "esperado_tiempo": "8 horas",
            "esperado_gasto": "300000",
        },
        {
            "nombre": "Moto hacia Medellin",
            "vehiculo": Vehiculo("negra", 2, "moto"),
            "destino": ciudadDestino("Medellin"),
            "esperado_info": "motocicletas",
            "esperado_combustible": "motocicleta",
            "esperado_tiempo": "4 horas",
            "esperado_gasto": "50000",
        },
        {
            "nombre": "Camion hacia Cali",
            "vehiculo": Vehiculo("blanco", 6, "camion"),
            "destino": ciudadDestino("Cali"),
            "esperado_info": "camiones",
            "esperado_combustible": "camión",
            "esperado_tiempo": "6 horas",
            "esperado_gasto": "400000",
        },
        {
            "nombre": "Bicicleta hacia ciudad no registrada",
            "vehiculo": Vehiculo("azul", 2, "bicicleta"),
            "destino": ciudadDestino("Pasto"),
            "esperado_info": "bicicletas",
            "esperado_combustible": "no utilizan combustible",
            "esperado_tiempo": "No se tiene información",
            "esperado_gasto": "no hay gasto",
        },
    ]

    aprobadas = 0

    for indice, prueba in enumerate(pruebas, start=1):
        vehiculo = prueba["vehiculo"]
        destino = prueba["destino"]
        coche = Coche(vehiculo.color, vehiculo.ruedas, vehiculo.tipo_de_vehiculo, 120, 2000, destino)

        resultado_info = vehiculo.info()
        resultado_combustible = vehiculo.tipoDeCombustible()
        resultado_tiempo = coche.tiempoDesplazamiento()
        resultado_gasto = coche.gastoCombustible()

        checks = [
            prueba["esperado_info"].lower() in resultado_info.lower(),
            prueba["esperado_combustible"].lower() in resultado_combustible.lower(),
            prueba["esperado_tiempo"].lower() in resultado_tiempo.lower(),
            prueba["esperado_gasto"].lower() in resultado_gasto.lower(),
        ]

        estado = "OK" if all(checks) else "ERROR"
        if estado == "OK":
            aprobadas += 1

        separador("-")
        print(f"Prueba {indice}: {prueba['nombre']}")
        print(f"Estado: {estado}")
        print(f"Info: {resultado_info}")
        print(f"Combustible: {resultado_combustible}")
        print(f"Tiempo: {resultado_tiempo}")
        print(f"Gasto: {resultado_gasto}")

    separador("=")
    print(f"Resumen: {aprobadas} de {len(pruebas)} pruebas aprobadas.")

    
    pruebas[0]["vehiculo"].saveInfo()
    print("Se guardó un reporte en vehiculo_info.txt")

def punto2():
    titulo("PUNTO 2")
    vehiculos = [
        Coche_P2("rojo", 4, 120, 2000),
        Bicicleta_P2("azul", 2, "urbana"),
        Camion("blanco", 6, 100, 5000, "10 toneladas"),
        Motocicleta("negra", 2, "deportiva", 150, 600),
    ]
    print("Categoría de cada vehículo:")
    CategoriaVehiculo(vehiculos)
    CategoriaVehiculoRuedas(vehiculos, 2)
    CategoriaVehiculoRuedas(vehiculos, 4)
    CategoriaVehiculoRuedas(vehiculos, 6)

def punto3():
    titulo("PUNTO 3")
    Triangulo1 = Triangulo(10, 5)
    Rectangulo1 = Rectangulo(10, 5)
    Circulo1 = Circulo(7)
    figuras = [Triangulo1, Rectangulo1, Circulo1]
    for figura in figuras:
        print(f"{figura.tipo} - Área: {figura.area():.2f}")

def punto4():
    titulo("PUNTO 4")
    taxi = Taxi(4, 2.5, "Sedan")
    bus = Bus(40, 1.0, "Ruta urbana")
    metro = Metro(200, 0.5, "Línea 1")

    distancia = 10  

    print(f"Pasaje en Taxi para {distancia} km: ${taxi.calcularPasaje(distancia):.2f}")
    print(f"Pasaje en Bus para {distancia} km: ${bus.calcularPasaje(distancia):.2f}")
    print(f"Pasaje en Metro para {distancia} km: ${metro.calcularPasaje(distancia):.2f}")

def punto5():
    separador("=")
    print("Gracias por usar el menú del Taller V. Hasta pronto.")
    separador("=")


if __name__ == "__main__":
    Menu()
    
    