from .vehiculo import Vehiculo 

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc'
