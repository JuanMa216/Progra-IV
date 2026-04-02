from punto1 import Alumno, Profesor, ProfesorAyudante
from punto2 import Alexa, BombillaInteligente, CamaraDeSeguridad, SmartTV


def pedir_entero(mensaje):
	while True:
		try:
			return int(input(mensaje))
		except ValueError:
			print("Ingresa un numero valido.")


def pedir_bool(mensaje):
	while True:
		respuesta = input(mensaje).strip().lower()
		if respuesta in ("si", "s", "1", "true"):
			return True
		if respuesta in ("no", "n", "0", "false"):
			return False
		print("Responde si o no.")


def pedir_referencias(registros, mensaje):
	entrada = input(mensaje).strip()
	if not entrada:
		return []

	referencias = []
	for identificador in entrada.split(","):
		identificador = identificador.strip()
		if identificador in registros:
			referencias.append(registros[identificador])
		else:
			print(f"No existe el ID '{identificador}'. Se omite.")
	return referencias


def datos_base_persona():
	return {
		"ID": input("ID: ").strip(),
		"nombre": input("Nombre: ").strip(),
		"edad": pedir_entero("Edad: "),
		"facultad": input("Facultad: ").strip(),
		"cargo": input("Cargo: ").strip(),
		"antiguedad": pedir_entero("Antiguedad (anios): "),
	}


def datos_base_dispositivo():
	return {
		"marca": input("Marca: ").strip(),
		"modelo": input("Modelo: ").strip(),
		"consumo": pedir_entero("Consumo energetico (W): "),
		"voltaje": pedir_entero("Voltaje (V): "),
	}


def menu_principal():
	print("\n--- MENU TALLER VI ---")
	print("1. Probar punto1")
	print("2. Probar punto2")
	print("3. Salir")


def menu_punto1():
	print("\n--- PUNTO 1 ---")
	print("1. Registrar alumno")
	print("2. Registrar profesor")
	print("3. Registrar profesor ayudante")
	print("4. Mostrar registros")
	print("5. Calcular sueldo de profesor")
	print("6. Guardar profesor")
	print("7. Volver")


def menu_punto2():
	print("\n--- PUNTO 2 ---")
	print("1. Registrar SmartTV")
	print("2. Registrar camara de seguridad")
	print("3. Registrar bombilla inteligente")
	print("4. Registrar Alexa")
	print("5. Mostrar dispositivos")
	print("6. Encender dispositivo")
	print("7. Conectar dispositivo a red")
	print("8. Ejecutar accion especial")
	print("9. Guardar informacion")
	print("10. Volver")


def registrar_alumno(alumnos, profesores):
	print("\nRegistro de alumno")
	base = datos_base_persona()
	semestre = pedir_entero("Semestre: ")
	carrera = input("Carrera: ").strip()
	lista_profesores = pedir_referencias(profesores, "IDs de profesores separados por coma: ")
	alumno = Alumno(
		base["ID"],
		base["nombre"],
		base["edad"],
		base["facultad"],
		base["cargo"],
		base["antiguedad"],
		semestre,
		lista_profesores,
		carrera,
	)
	alumnos[alumno.ID] = alumno
	print("Alumno registrado.")


def registrar_profesor(profesores, alumnos):
	print("\nRegistro de profesor")
	base = datos_base_persona()
	horas_clase = pedir_entero("Horas de clase: ")
	experiencia = input("Experiencia: ").strip()
	lista_estudiantes = pedir_referencias(alumnos, "IDs de alumnos separados por coma: ")
	profesor = Profesor(
		base["ID"],
		base["nombre"],
		base["edad"],
		base["facultad"],
		base["cargo"],
		base["antiguedad"],
		horas_clase,
		experiencia,
		lista_estudiantes,
	)
	profesores[profesor.ID] = profesor
	print("Profesor registrado.")


def registrar_profesor_ayudante(profesores_ayudantes, profesores, alumnos):
	print("\nRegistro de profesor ayudante")
	base = datos_base_persona()
	horas_clase = pedir_entero("Horas de clase: ")
	experiencia = input("Experiencia: ").strip()
	semestre = pedir_entero("Semestre: ")
	carrera = input("Carrera: ").strip()
	lista_estudiantes = pedir_referencias(alumnos, "IDs de alumnos separados por coma: ")
	lista_profesores = pedir_referencias(profesores, "IDs de profesores separados por coma: ")
	ayudante = ProfesorAyudante(
		base["ID"],
		base["nombre"],
		base["edad"],
		base["facultad"],
		base["cargo"],
		base["antiguedad"],
		horas_clase,
		experiencia,
		lista_estudiantes,
		semestre,
		lista_profesores,
		carrera,
	)
	profesores_ayudantes[ayudante.ID] = ayudante
	print("Profesor ayudante registrado.")


def mostrar_punto1(alumnos, profesores, profesores_ayudantes):
	if not alumnos and not profesores and not profesores_ayudantes:
		print("No hay registros.")
		return

	if alumnos:
		print("\nAlumnos:")
		for alumno in alumnos.values():
			alumno.mostrar_informacion()
			print("-")

	if profesores:
		print("\nProfesores:")
		for profesor in profesores.values():
			profesor.mostrar_informacion()
			print("-")

	if profesores_ayudantes:
		print("\nProfesores ayudantes:")
		for ayudante in profesores_ayudantes.values():
			ayudante.mostrar_informacion()
			print("-")


def calcular_sueldo(profesores):
	if not profesores:
		print("No hay profesores registrados.")
		return

	id_profesor = input("ID del profesor: ").strip()
	if id_profesor in profesores:
		print(f"Sueldo mensual: {profesores[id_profesor].sueldo_mensual()}")
	else:
		print("No existe un profesor con ese ID.")


def guardar_profesor(profesores):
	if not profesores:
		print("No hay profesores registrados.")
		return

	id_profesor = input("ID del profesor a guardar: ").strip()
	if id_profesor in profesores:
		profesores[id_profesor].guardar_informacion()
		print("Informacion guardada en 'profesor.txt'.")
	else:
		print("No existe un profesor con ese ID.")


def mostrar_dispositivos(registros):
	if not registros:
		print("No hay dispositivos registrados.")
		return

	for clave, dispositivo in registros.items():
		print(f"\n--- {clave} ({type(dispositivo).__name__}) ---")
		dispositivo.mostrar_informacion()


def pedir_dispositivo(registros):
	if not registros:
		print("No hay dispositivos registrados.")
		return None

	print("\nDispositivos registrados:")
	for clave, dispositivo in registros.items():
		print(f"- {clave}: {type(dispositivo).__name__} ({dispositivo.marca} {dispositivo.modelo})")

	clave = input("Ingrese el identificador del dispositivo: ").strip()
	if clave not in registros:
		print("No existe un dispositivo con ese identificador.")
		return None
	return registros[clave]


def registrar_smarttv(registros):
	print("\nRegistro de SmartTV")
	base = datos_base_dispositivo()
	id_dispositivo = input("Identificador: ").strip()
	registros[id_dispositivo] = SmartTV(base["marca"], base["modelo"], base["consumo"], base["voltaje"])
	print("SmartTV registrada correctamente.")


def registrar_camara(registros):
	print("\nRegistro de camara de seguridad")
	base = datos_base_dispositivo()
	intruso = pedir_bool("¿Intruso detectado? (si/no): ")
	id_dispositivo = input("Identificador: ").strip()
	registros[id_dispositivo] = CamaraDeSeguridad(base["marca"], base["modelo"], base["consumo"], base["voltaje"], intruso)
	print("Camara registrada correctamente.")


def registrar_bombilla(registros):
	print("\nRegistro de bombilla inteligente")
	base = datos_base_dispositivo()
	color = input("Color del LED: ").strip()
	id_dispositivo = input("Identificador: ").strip()
	registros[id_dispositivo] = BombillaInteligente(base["marca"], base["modelo"], base["consumo"], base["voltaje"], color)
	print("Bombilla registrada correctamente.")


def registrar_alexa(registros):
	print("\nRegistro de Alexa")
	base = datos_base_dispositivo()
	asistente = input("Asistente virtual: ").strip()
	bluetooth = pedir_bool("¿Tiene Bluetooth? (si/no): ")
	id_dispositivo = input("Identificador: ").strip()
	registros[id_dispositivo] = Alexa(base["marca"], base["modelo"], base["consumo"], base["voltaje"], asistente, bluetooth)
	print("Alexa registrada correctamente.")


def encender_dispositivo(registros):
	dispositivo = pedir_dispositivo(registros)
	if dispositivo is not None:
		dispositivo.encender()


def conectar_dispositivo(registros):
	dispositivo = pedir_dispositivo(registros)
	if dispositivo is None:
		return

	if not hasattr(dispositivo, "nueva_conexion"):
		print("Este dispositivo no admite conexion a red.")
		return

	ip = input("IP: ").strip()
	protocolo = input("Protocolo de seguridad: ").strip()
	velocidad = pedir_entero("Velocidad de conexion (Mbps): ")
	latencia = pedir_entero("Latencia (ms): ")
	dispositivo.nueva_conexion(ip, protocolo, velocidad, latencia)


def accion_especial(registros):
	dispositivo = pedir_dispositivo(registros)
	if dispositivo is None:
		return

	if isinstance(dispositivo, SmartTV):
		dispositivo.reiniciar()
	elif isinstance(dispositivo, CamaraDeSeguridad):
		dispositivo.grabar_video()
		dispositivo.reporteSeguridad()
	elif isinstance(dispositivo, BombillaInteligente):
		nuevo_color = input("Nuevo color del LED: ").strip()
		dispositivo.cambiarColor(nuevo_color)
	elif isinstance(dispositivo, Alexa):
		cancion = input("Cancion a reproducir: ").strip()
		dispositivo.reproducirMusica(cancion)


def guardar_informacion(registros):
	dispositivo = pedir_dispositivo(registros)
	if dispositivo is not None and hasattr(dispositivo, "guardar_informacion"):
		dispositivo.guardar_informacion()
		print("Informacion guardada en 'dispositivo.txt'.")


def menu_punto1_loop():
	alumnos = {}
	profesores = {}
	profesores_ayudantes = {}

	while True:
		menu_punto1()
		opcion = input("Seleccione una opcion: ").strip()
		if opcion == "1":
			registrar_alumno(alumnos, profesores)
		elif opcion == "2":
			registrar_profesor(profesores, alumnos)
		elif opcion == "3":
			registrar_profesor_ayudante(profesores_ayudantes, profesores, alumnos)
		elif opcion == "4":
			mostrar_punto1(alumnos, profesores, profesores_ayudantes)
		elif opcion == "5":
			calcular_sueldo(profesores)
		elif opcion == "6":
			guardar_profesor(profesores)
		elif opcion == "7":
			break
		else:
			print("Opcion no valida.")


def menu_punto2_loop():
	registros = {}

	while True:
		menu_punto2()
		opcion = input("Seleccione una opcion: ").strip()
		if opcion == "1":
			registrar_smarttv(registros)
		elif opcion == "2":
			registrar_camara(registros)
		elif opcion == "3":
			registrar_bombilla(registros)
		elif opcion == "4":
			registrar_alexa(registros)
		elif opcion == "5":
			mostrar_dispositivos(registros)
		elif opcion == "6":
			encender_dispositivo(registros)
		elif opcion == "7":
			conectar_dispositivo(registros)
		elif opcion == "8":
			accion_especial(registros)
		elif opcion == "9":
			guardar_informacion(registros)
		elif opcion == "10":
			break
		else:
			print("Opcion no valida.")


def main():
	while True:
		menu_principal()
		opcion = input("Seleccione una opcion: ").strip()
		if opcion == "1":
			menu_punto1_loop()
		elif opcion == "2":
			menu_punto2_loop()
		elif opcion == "3":
			print("Saliendo del programa...")
			break
		else:
			print("Opcion no valida.")


if __name__ == "__main__":
	main()