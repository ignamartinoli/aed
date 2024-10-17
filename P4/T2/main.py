import os.path
import pickle
import random

from T2.Vehiculo import Vehiculo
from T2.utils import *


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print(f'ERROR: el archivo {fd} no existe')
        return

    total = 0
    cantidad = 0

    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        vehiculo = pickle.load(m)
        print(vehiculo)

        if vehiculo.tipo == 3:
            total += vehiculo.costo
            cantidad += 1
    m.close()

    print(f'Promedio: ${round(promedio(total, cantidad), 2)}')


def generar_archivo(fd, vehiculos):
    m = open(fd, 'wb')
    for vehiculo in vehiculos:
        if vehiculo.tamano >= 3:
            pickle.dump(vehiculo, m)
    m.close()


def buscar_vehiculo(vehiculos):
    identificador = positivo('Identificador')

    posicion = busqueda_binaria(identificador, vehiculos)

    if posicion != -1:
        vehiculo = vehiculos[posicion]
        print(vehiculo)

        if vehiculo.tipo >= 2:
            print('Opcion ecologica!')
    else:
        print('ERROR: no se encontro')


def mostrar_vehiculos(vehiculos):
    for vehiculo in vehiculos:
        print(vehiculo)


def cargar_vehiculos_ordenados(vehiculos):
    n = positivo('Cantidad')

    for _ in range(n):
        identificador = random.randint(1, 999_999)
        tamano = random.randint(1, 4)
        tipo = random.randint(0, 4)
        costo = random.uniform(200, 4_000)

        agregar_en_orden(vehiculos, Vehiculo(identificador, tamano, tipo, costo))



def menu():
    print('\n[ MENU ]')
    print('1. Cargar vehiculos ordenados')
    print('2. Mostrar vehiculos')
    print('3. Buscar vehiculo')
    print('4. Generar archivo')
    print('5. Mostrar archivo')

    return positivo('Opcion')


def main():
    vehiculos = []
    fd = 'vehiculos.dat'

    while True:
        opcion = menu()

        if opcion == 1:
            cargar_vehiculos_ordenados(vehiculos)
        elif not vehiculos:
            print('ERROR: no existen vehiculos')
        elif opcion == 2:
            mostrar_vehiculos(vehiculos)
        elif opcion == 3:
            buscar_vehiculo(vehiculos)
        elif opcion == 4:
            generar_archivo(fd, vehiculos)
        elif opcion == 5:
            mostrar_archivo(fd)
        else:
            break

    print('Fin')


if __name__ == '__main__':
    main()