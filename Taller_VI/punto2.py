class DispositivoElectronico:
    def __init__(self, marca, modelo, consumoEnergetico, voltaje):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico
        self.voltaje = voltaje
        
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Consumo Energético: {self.consumoEnergetico} W")
        print(f"Voltaje: {self.voltaje} V")
        
    def encender(self):
        print(f"{self.marca} {self.modelo} se ha encendido.")
        
        
class ConectividadARed:
    def __init__(self, IP, protocoloSeguridad, velocidadConexion, estadoConexion, latencia):
        self.IP = IP
        self.protocoloSeguridad = protocoloSeguridad
        self.velocidadConexion = velocidadConexion
        self.estadoConexion = estadoConexion
        self.latencia = latencia
    
    def mostrar_informacion(self):
        print(f"IP: {self.IP}")
        print(f"Protocolo de Seguridad: {self.protocoloSeguridad}")
        print(f"Velocidad de Conexión: {self.velocidadConexion} Mbps")
        print(f"Estado de Conexión: {self.estadoConexion}")
        print(f"Latencia: {self.latencia} ms")
        
    def conectar_a_red(self, red):
        print(f"Conectando a la red {red}...")
        self.estadoConexion = "Conectado"
        print(f"{self.marca} {self.modelo} se ha conectado a la red {red}.")
        
    def guardar_informacion(self):
        with open("dispositivo.txt", "w") as file:
            file.write(f"Marca: {self.marca}\n")
            file.write(f"Modelo: {self.modelo}\n")
            file.write(f"Consumo Energético: {self.consumoEnergetico} W\n")
            file.write(f"Voltaje: {self.voltaje} V\n")
            if self.IP is not None:
                file.write(f"IP: {self.IP}\n")
                file.write(f"Protocolo de Seguridad: {self.protocoloSeguridad}\n")
                file.write(f"Velocidad de Conexión: {self.velocidadConexion} Mbps\n")
                file.write(f"Estado de Conexión: {self.estadoConexion}\n")
                file.write(f"Latencia: {self.latencia} ms\n")
            else:
                file.write("No hay información de conectividad disponible.\n")
        
class SmartTV(DispositivoElectronico, ConectividadARed):
    def __init__(self, marca, modelo, consumoEnergetico, voltaje):
        super().__init__(marca, modelo, consumoEnergetico, voltaje)
        self.IP = None
        self.protocoloSeguridad = None
        self.velocidadConexion = None
        self.estadoConexion = None
        self.latencia = None
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        if self.IP is not None:
            print(f"IP: {self.IP}")
            print(f"Protocolo de Seguridad: {self.protocoloSeguridad}")
            print(f"Velocidad de Conexión: {self.velocidadConexion} Mbps")
            print(f"Estado de Conexión: {self.estadoConexion}")
            print(f"Latencia: {self.latencia} ms")
        else:
            print("No hay información de conectividad disponible.")
            
    def estado_conexion(self):
        if self.estadoConexion is not None:
            return self.estadoConexion
        else:
            return "No hay información de conectividad disponible."
        
    def consumo_energetico(self):
        return self.consumoEnergetico
    
    def nueva_conexion(self, IP, protocoloSeguridad, velocidadConexion, latencia):
        self.IP = IP
        self.protocoloSeguridad = protocoloSeguridad
        self.velocidadConexion = velocidadConexion
        self.latencia = latencia
        self.estadoConexion = "Conectado"
        print(f"{self.marca} {self.modelo} se ha conectado a la red con IP {self.IP}.")
        
    def reiniciar(self):
        print(f"{self.marca} {self.modelo} se está reiniciando...")
        self.estadoConexion = "Desconectado"
        print(f"{self.marca} {self.modelo} se ha reiniciado y está desconectado.")
        
class CamaraDeSeguridad(DispositivoElectronico, ConectividadARed):
    def __init__(self, marca, modelo, consumoEnergetico, voltaje, intrusoDetectado):
        super().__init__(marca, modelo, consumoEnergetico, voltaje)
        self.IP = None
        self.protocoloSeguridad = None
        self.velocidadConexion = None
        self.estadoConexion = None
        self.latencia = None
        self.intrusoDetectado = intrusoDetectado
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        if self.IP is not None:
            print(f"IP: {self.IP}")
            print(f"Protocolo de Seguridad: {self.protocoloSeguridad}")
            print(f"Velocidad de Conexión: {self.velocidadConexion} Mbps")
            print(f"Estado de Conexión: {self.estadoConexion}")
            print(f"Latencia: {self.latencia} ms")
        else:
            print("No hay información de conectividad disponible.")
            
    def estado_conexion(self):
        if self.estadoConexion is not None:
            return self.estadoConexion
        else:
            return "No hay información de conectividad disponible."
        
    def consumo_energetico(self):
        return self.consumoEnergetico
    
    def nueva_conexion(self, IP, protocoloSeguridad, velocidadConexion, latencia):
        self.IP = IP
        self.protocoloSeguridad = protocoloSeguridad
        self.velocidadConexion = velocidadConexion
        self.latencia = latencia
        self.estadoConexion = "Conectado"
        print(f"{self.marca} {self.modelo} se ha conectado a la red con IP {self.IP}.")
        
    def reiniciar(self):
        print(f"{self.marca} {self.modelo} se está reiniciando...")
        self.estadoConexion = "Desconectado"
        print(f"{self.marca} {self.modelo} se ha reiniciado y está desconectado.")
        
    def grabar_video(self):
        print(f"{self.marca} {self.modelo} está grabando video...")
    
    def reporteSeguridad(self):
        if self.intrusoDetectado:
            print(f"¡Alerta! Intruso detectado por {self.marca} {self.modelo}.")
        else:
            print(f"No se han detectado intrusos por {self.marca} {self.modelo}.")
            
class BombillaInteligente(DispositivoElectronico, ConectividadARed):
    def __init__(self, marca, modelo, consumoEnergetico, voltaje, colorLed):
        super().__init__(marca, modelo, consumoEnergetico, voltaje)
        self.colorLed = colorLed
        self.IP = None
        self.protocoloSeguridad = None
        self.velocidadConexion = None
        self.estadoConexion = None
        self.latencia = None
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Color del LED: {self.colorLed}")
        if self.IP is not None:
            print(f"IP: {self.IP}")
            print(f"Protocolo de Seguridad: {self.protocoloSeguridad}")
            print(f"Velocidad de Conexión: {self.velocidadConexion} Mbps")
            print(f"Estado de Conexión: {self.estadoConexion}")
            print(f"Latencia: {self.latencia} ms")
        else:
            print("No hay información de conectividad disponible.")
    
    def estado_conexion(self):
        if self.estadoConexion is not None:
            return self.estadoConexion
        else:
            return "No hay información de conectividad disponible."
        
    def consumo_energetico(self):
        return self.consumoEnergetico
    
    def nueva_conexion(self, IP, protocoloSeguridad, velocidadConexion, latencia):
        self.IP = IP
        self.protocoloSeguridad = protocoloSeguridad
        self.velocidadConexion = velocidadConexion
        self.latencia = latencia
        self.estadoConexion = "Conectado"
        print(f"{self.marca} {self.modelo} se ha conectado a la red con IP {self.IP}.")
        
    def reiniciar(self):
        print(f"{self.marca} {self.modelo} se está reiniciando...")
        self.estadoConexion = "Desconectado"
        print(f"{self.marca} {self.modelo} se ha reiniciado y está desconectado.")
        
    def cambiarColor(self, nuevoColor):
        self.colorLed = nuevoColor
        print(f"{self.marca} {self.modelo} ha cambiado el color del LED a {self.colorLed}.")
        
class Alexa(DispositivoElectronico, ConectividadARed):
    def __init__(self, marca, modelo, consumoEnergetico, voltaje, asistenteVirtual, bluetooth):
        super().__init__(marca, modelo, consumoEnergetico, voltaje)
        self.asistenteVirtual = asistenteVirtual
        self.bluetooth = bluetooth
        self.IP = None
        self.protocoloSeguridad = None
        self.velocidadConexion = None
        self.estadoConexion = None
        self.latencia = None
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Asistente Virtual: {self.asistenteVirtual}")
        print(f"Bluetooth: {self.bluetooth}")
        if self.IP is not None:
            print(f"IP: {self.IP}")
            print(f"Protocolo de Seguridad: {self.protocoloSeguridad}")
            print(f"Velocidad de Conexión: {self.velocidadConexion} Mbps")
            print(f"Estado de Conexión: {self.estadoConexion}")
            print(f"Latencia: {self.latencia} ms")
        else:
            print("No hay información de conectividad disponible.")
    
    def estado_conexion(self):
        if self.estadoConexion is not None:
            return self.estadoConexion
        else:
            return "No hay información de conectividad disponible."
        
    def consumo_energetico(self):
        return self.consumoEnergetico
    
    def nueva_conexion(self, IP, protocoloSeguridad, velocidadConexion, latencia):
        self.IP = IP
        self.protocoloSeguridad = protocoloSeguridad
        self.velocidadConexion = velocidadConexion
        self.latencia = latencia
        self.estadoConexion = "Conectado"
        print(f"{self.marca} {self.modelo} se ha conectado a la red con IP {self.IP}.")
        
    def reiniciar(self):
        print(f"{self.marca} {self.modelo} se está reiniciando...")
        self.estadoConexion = "Desconectado"
        print(f"{self.marca} {self.modelo} se ha reiniciado y está desconectado.")
        
    def reproducirMusica(self, cancion):
        if self.bluetooth:
            print(f"{self.marca} {self.modelo} está reproduciendo la canción '{cancion}'.")
        else:
            print(f"{self.marca} {self.modelo} no tiene Bluetooth para reproducir música.")