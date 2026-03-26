class Vehiculo:
    def __init__(self, color, ruedas, tipo_de_vehiculo):
        self.color = color
        self.ruedas = ruedas
        self.tipo_de_vehiculo = tipo_de_vehiculo

    def _tipo_normalizado(self):
        tipo = self.tipo_de_vehiculo.lower().strip()
        if tipo == "carro":
            return "coche"
        if tipo == "moto":
            return "motocicleta"
        if tipo == "camion":
            return "camión"
        return tipo

    def info(self):
        tipo = self._tipo_normalizado()
        if tipo == "coche":
            return f"El vehículo es un {self.tipo_de_vehiculo} de color {self.color} con {self.ruedas} ruedas. Las ruedas pueden durar entre 5-10 años dependiendo del uso y mantenimiento.\nLas mejores marcas de neumáticos para coches son Michelin, Bridgestone, Goodyear, Continental y Pirelli."
        if tipo == "bicicleta":
            return f"El vehículo es una {self.tipo_de_vehiculo} de color {self.color} con {self.ruedas} ruedas. Las ruedas pueden durar entre 2-5 años dependiendo del uso y mantenimiento.\nLas mejores marcas de neumáticos para bicicletas son Continental, Schwalbe, Michelin, Vittoria y Maxxis."
        if tipo == "motocicleta":
            return f"El vehículo es una {self.tipo_de_vehiculo} de color {self.color} con {self.ruedas} ruedas. Las ruedas pueden durar entre 3-7 años dependiendo del uso y mantenimiento.\nLas mejores marcas de neumáticos para motocicletas son Michelin, Pirelli, Bridgestone, Continental y Dunlop."
        if tipo == "camión":
            return f"El vehículo es un {self.tipo_de_vehiculo} de color {self.color} con {self.ruedas} ruedas. Las ruedas pueden durar entre 1-3 años dependiendo del uso y mantenimiento.\nLas mejores marcas de neumáticos para camiones son Michelin, Bridgestone, Goodyear, Continental y Pirelli."
        return f"El vehículo es un {self.tipo_de_vehiculo} de color {self.color} con {self.ruedas} ruedas. No se tiene información sobre la duración de las ruedas ni las mejores marcas de neumáticos para este tipo de vehículo."

    def saveInfo(self):
        with open("vehiculo_info.txt", "w") as file:
            file.write(self.info())
            file.write("\n")
            file.write(self.tipoDeCombustible())

    def tipoDeCombustible(self):
        tipo = self._tipo_normalizado()
        if tipo == "coche":
            return "El tipo de combustible para un coche puede ser gasolina, diésel, eléctrico o híbrido."
        if tipo == "bicicleta":
            return "Las bicicletas no utilizan combustible, ya que son impulsadas por la fuerza humana."
        if tipo == "motocicleta":
            return "El tipo de combustible para una motocicleta puede ser gasolina o eléctrico."
        if tipo == "camión":
            return "El tipo de combustible para un camión puede ser diésel o eléctrico."
        return "No se tiene información sobre el tipo de combustible para este tipo de vehículo."


class ciudadDestino:
    def __init__(self, nombre):
        self.nombre = nombre


class Coche(Vehiculo):
    def __init__(self, color, ruedas, tipo_de_vehiculo, velocidad, cilindrada, ciudadDestino):
        super().__init__(color, ruedas, tipo_de_vehiculo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.ciudadDestino = ciudadDestino

    def _ciudad_normalizada(self):
        ciudad = self.ciudadDestino.nombre.lower().strip()
        if ciudad == "bogota":
            return "bogotá"
        if ciudad == "medellin":
            return "medellín"
        return ciudad

    def tiempoDesplazamiento(self):
        tipo = self._tipo_normalizado()
        ciudad = self._ciudad_normalizada()

        if ciudad == "bogotá":
            if tipo == "coche":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en un {self.tipo_de_vehiculo} es de aproximadamente 8 horas."
            if tipo == "bicicleta":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en una {self.tipo_de_vehiculo} es de aproximadamente 3 días."
            if tipo == "motocicleta":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en una {self.tipo_de_vehiculo} es de aproximadamente 6 horas."
            if tipo == "camión":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en un {self.tipo_de_vehiculo} es de aproximadamente 10 horas."
            return f"No se tiene información sobre el tiempo de desplazamiento a {self.ciudadDestino.nombre} para este tipo de vehículo."

        if ciudad == "medellín":
            if tipo == "coche":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en un {self.tipo_de_vehiculo} es de aproximadamente 6 horas."
            if tipo == "bicicleta":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en una {self.tipo_de_vehiculo} es de aproximadamente 2 días."
            if tipo == "motocicleta":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en una {self.tipo_de_vehiculo} es de aproximadamente 4 horas."
            if tipo == "camión":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en un {self.tipo_de_vehiculo} es de aproximadamente 8 horas."
            return f"No se tiene información sobre el tiempo de desplazamiento a {self.ciudadDestino.nombre} para este tipo de vehículo."

        if ciudad == "cali":
            if tipo == "coche":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en un {self.tipo_de_vehiculo} es de aproximadamente 4 horas."
            if tipo == "bicicleta":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en una {self.tipo_de_vehiculo} es de aproximadamente 1 día."
            if tipo == "motocicleta":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en una {self.tipo_de_vehiculo} es de aproximadamente 3 horas."
            if tipo == "camión":
                return f"El tiempo de desplazamiento a {self.ciudadDestino.nombre} en un {self.tipo_de_vehiculo} es de aproximadamente 6 horas."
            return f"No se tiene información sobre el tiempo de desplazamiento a {self.ciudadDestino.nombre} para este tipo de vehículo."

        return f"No se tiene información sobre el tiempo de desplazamiento a {self.ciudadDestino.nombre} para este tipo de vehículo."

    def gastoCombustible(self):
        tipo = self._tipo_normalizado()
        if tipo == "coche":
            return f"El gasto de combustible para un {self.tipo_de_vehiculo} teniendo en cuenta que un carro promedio tiene una autonomia de 600-700km por tanque y que el costo de la gasolina en Colombia es de aproximadamente 15250 pesos para un total de 1000km sería de aproximadamente 300000 pesos."
        if tipo == "bicicleta":
            return "Las bicicletas no utilizan combustible, por lo que no hay gasto de combustible."
        if tipo == "motocicleta":
            return f"El gasto de combustible para una {self.tipo_de_vehiculo} teniendo en cuenta que una moto promedio tiene una autonomia de 300-400km por tanque y que el costo de la gasolina en Colombia es de aproximadamente 15250 pesos para un total de 1000km sería de aproximadamente 50000 pesos."
        if tipo == "camión":
            return f"El gasto de combustible para un {self.tipo_de_vehiculo} teniendo en cuenta que un camión promedio tiene una autonomia de 200-300km por tanque y que el costo del diésel en Colombia es de aproximadamente 12000 pesos para un total de 1000km sería de aproximadamente 400000 pesos."
        return "No se tiene información sobre el gasto de combustible para este tipo de vehículo."