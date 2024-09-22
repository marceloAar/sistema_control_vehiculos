from parte01.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, Tipo: {self.tipo}'
