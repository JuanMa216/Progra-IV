class PersonalUniversitario:
    def __init__(self, ID, nombre, edad, facultad, cargo, antiguedad):
        self.ID = ID
        self.nombre = nombre
        self.edad = edad
        self.facultad = facultad
        self.cargo = cargo
        self.antiguedad = antiguedad
    
    def mostrar_informacion(self):
        print(f"ID: {self.ID}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Facultad: {self.facultad}")
        print(f"Cargo: {self.cargo}")
        print(f"Antigüedad: {self.antiguedad}")

    def _experiencia_normalizada_ganancias(self):
        experiencia = self.experiencia.lower()
        if experiencia == "transitorio":
            return self.horas_clase * 30.000
        if experiencia == "catedratico":
            return self.horas_clase * 40.000 
        if experiencia == "maestria":
            return self.horas_clase * 70.000
        if experiencia == "doctorado":
            return self.horas_clase * 120.000
        return 0
    
    def antiguedad(self):
        return self.antiguedad
    
    def guardar_informacion(self):
        with open("profesor.txt", "w") as file:
            file.write(f"ID: {self.ID}\n")
            file.write(f"Nombre: {self.nombre}\n")
            file.write(f"Edad: {self.edad}\n")
            file.write(f"Facultad: {self.facultad}\n")
            file.write(f"Cargo: {self.cargo}\n")
            file.write(f"Antigüedad: {self.antiguedad}\n")
            file.write(f"Horas de clase: {self.horas_clase}\n")
            file.write(f"Experiencia: {self.experiencia}\n")
            file.write("Estudiantes:\n")
            for estudiante in self.estudiantes:
                file.write(f"Estudiante: {estudiante.nombre}\n")
            
    

class Profesor(PersonalUniversitario):
    def __init__(self, ID, nombre, edad, facultad, cargo, antiguedad, horas_clase, experiencia, estudiantes):
        super().__init__(ID, nombre, edad, facultad, cargo, antiguedad)
        self.horas_clase = horas_clase
        self.experiencia = experiencia
        self.estudiantes = estudiantes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Horas de clase: {self.horas_clase}")
        print(f"Experiencia: {self.experiencia}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(f"Estudiante: {estudiante.nombre}")

    
    def sueldo_mensual(self):
        print("Datos tomados de la Universidad Nacional de Colombia: ")
        return self._experiencia_normalizada_ganancias()
    
class Alumno(PersonalUniversitario):
    def __init__(self, ID, nombre, edad, facultad, cargo, antiguedad, semestre, profesores, carrera):
        super().__init__(ID, nombre, edad, facultad, cargo, antiguedad)
        self.semestre = semestre
        self.profesores = profesores
        self.carrera = carrera

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print("Profesores:")
        for profesor in self.profesores:
            print(f"Profesor: {profesor.nombre}")
            
class ProfesorAyudante(Profesor, Alumno):
    def __init__(self, ID, nombre, edad, facultad, cargo, antiguedad, horas_clase, experiencia, estudiantes, semestre, profesores, carrera):
        Profesor.__init__(self, ID, nombre, edad, facultad, cargo, antiguedad, horas_clase, experiencia, estudiantes)
        Alumno.__init__(self, ID, nombre, edad, facultad, cargo, antiguedad, semestre, profesores, carrera)

    def mostrar_informacion(self):
        Profesor.mostrar_informacion(self)
        Alumno.mostrar_informacion(self)
