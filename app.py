#importar paquetes y clases
from parte01.automovil import Automovil
from parte01.vehiculo import Vehiculo

from parte02.particular import Particular
from parte02.carga import Carga
from parte02.bibicleta import Bicicleta
from parte02.motocicleta import Motocicleta

from parte03 import guardar_leer_datos as tres

#menu principal
def menu():
    while True:
        print("\n===== Menú Principal =====")
        print("1. Parte 1: Gestión de Vehiculos")
        print("2. Parte 2: Instancias y Verificacion de Motocicleta")
        print("3. Parte 3: Guardar y Leer Archivo csv")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            parte_uno()
        elif opcion == '2':
            parte_dos()            
        elif opcion == '3':
            parte_tres()            
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


#parte uno
def parte_uno():
    cantidad = int(input("¿Cuántos Vehículos desea insertar?: "))

    vehiculos = []
    
    for i in range(cantidad):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Ingrese la marca del automóvil: ")
        modelo = input("Ingrese el modelo: ")
        nro_ruedas = int(input("Ingrese el número de ruedas: "))
        velocidad = int(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese el cilindraje en cc: "))

        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)
    
    print("\n***** Lista de Vehículos *****")
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Datos del automóvil {i}: {vehiculo}")


#parte dos
def parte_dos():

    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    for vehiculo in vehiculos:
        print(vehiculo)  

    # Crear instancia de Motocicleta
    moto = Motocicleta("Toyota","Nose",2,"nose","400cc","bb",2)

    # Verificar las relaciones de la instancia de Motocicleta
    print("\n*** Verificaciones de instacia de motocicleta ***")
    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(moto, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automóvil: {isinstance(moto, Automovil)}")
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(moto, Particular)}")
    print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(moto, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(moto, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(moto, Motocicleta)}")         


#parte tres
def parte_tres():
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    tres.guardar_datos_csv(vehiculos)

    print("\nLeyendo los datos guardados en el archivo CSV:\n")
    tres.leer_datos_csv()          