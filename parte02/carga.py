from parte01.automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f', Carga: {self.carga} Kg'