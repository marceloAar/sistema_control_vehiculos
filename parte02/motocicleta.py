from .bibicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return super().__str__() + f', Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}'
