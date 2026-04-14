# main.py
from punto2 import Sistema, PacienteGeneral, PacientePrioritario, PacienteUrgencia

def registrar_paciente(sistema):
    print("\n--- REGISTRAR PACIENTE ---")
    print("Tipo de paciente:")
    print("1. General")
    print("2. Prioritario")
    print("3. Urgencias")
    tipo = input("Seleccione el tipo: ").strip().lower()

    try:
        documento = int(input("Documento: "))
        nombre = input("Nombre: ").strip()
        edad = int(input("Edad: "))
    except ValueError:
        print("Error: documento y edad deben ser números enteros.")
        return

    if tipo == "1" or tipo == "general":
        eps = input("Nombre de la EPS: ").strip()
        paciente = PacienteGeneral(documento, nombre, edad, "Pendiente", eps)
    elif tipo == "2" or tipo == "prioritario":
        condicion = input("Condición especial: ").strip()
        paciente = PacientePrioritario(documento, nombre, edad, "Pendiente", condicion)     
    elif tipo == "3" or tipo == "urgencias":
        gravedad = input("Nivel de gravedad: ").strip()
        paciente = PacienteUrgencia(documento, nombre, edad, "Pendiente", gravedad)
    else:
        print("Tipo de paciente inválido.")
        return

    sistema.registrarPaciente(paciente)


def mostrar_pacientes(sistema):
    print("\n--- LISTA DE PACIENTES ---")
    sistema.mostrarPacientes()


def buscar_paciente(sistema):
    print("\n--- BUSCAR PACIENTE ---")
    try:
        documento = int(input("Ingrese el documento a buscar: "))
    except ValueError:
        print("Error: el documento debe ser un número entero.")
        return
    paciente = sistema.buscarPaciente(documento)
    if paciente:
        print(paciente)


def atender_paciente(sistema):
    print("\n--- ATENDER SIGUIENTE PACIENTE ---")
    sistema.atenderPaciente()


def guardar_json(sistema):
    print("\n--- GUARDAR EN JSON ---")
    sistema.guardarJSON()


def cargar_json(sistema):
    print("\n--- CARGAR DESDE JSON ---")
    sistema.cargarJSON()


def mostrar_menu():
    print("\n=============================")
    print("   SISTEMA DE ATENCIÓN       ")
    print("       CLÍNICA               ")
    print("=============================")
    print("1. Registrar paciente")
    print("2. Mostrar todos los pacientes")
    print("3. Buscar paciente por documento")
    print("4. Atender siguiente paciente")
    print("5. Guardar en JSON")
    print("6. Cargar desde JSON")
    print("0. Salir")
    print("=============================")


def main():
    sistema = Sistema()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_paciente(sistema)
        elif opcion == "2":
            mostrar_pacientes(sistema)
        elif opcion == "3":
            buscar_paciente(sistema)
        elif opcion == "4":
            atender_paciente(sistema)
        elif opcion == "5":
            guardar_json(sistema)
        elif opcion == "6":
            cargar_json(sistema)
        elif opcion == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()