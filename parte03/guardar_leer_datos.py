import csv

from parte02.bibicleta import Bicicleta
from parte02.carga import Carga
from parte02.motocicleta import Motocicleta
from parte02.particular import Particular

def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    with open(nombre_archivo, "w", newline='') as archivo:
        archivo_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            archivo_csv.writerow([vehiculo.__class__, vehiculo.__dict__])

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    with open(nombre_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for fila in archivo_csv:
            print(fila)

# guardar y leer los datos
def guardar_leer():
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    guardar_datos_csv(vehiculos)

    print("\nLeyendo los datos guardados en el archivo CSV:\n")
    leer_datos_csv()