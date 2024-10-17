import os.path
import pickle
import random

from utils import *
from Consumo import *


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print(f'ERROR: no existe el archivo {fd}')
        return

    cantidad = 0

    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        cantidad += 1
        print(pickle.load(m))
    m.close()

    print(f'Cantidad: {cantidad}')


def generar_archivo(consumos, fd):
    t = input('Numero: ')

    m = open(fd, 'wb')
    for consumo in consumos:
        if consumo.tipo == 1 and consumo.numero == t:
            pickle.dump(consumo, m)
    m.close()


def mostrar_monto_por_hora_y_tipo(consumos):
    montos = [[0] * 3 for i in range(24)]

    for consumo in consumos:
        f = consumo.hora
        c = consumo.tipo - 1
        montos[f][c] += consumo.monto

    for f in range(12):
        for c in range(3):
            monto = montos[f][c]

            if monto != 0:
                print(f'{f}hs - tipo {c + 1}: ${round(monto, 2)}')


def mostrar_consumos(consumos):
    for consumo in consumos:
        print(consumo)


def cargar_consumos(consumos):
    n = positivo('Cantidad')

    for _ in range(n):
        numero = f'{random.randint(351_000_0000, 351_999_9999)}'
        hora = random.randint(0, 23)  # 0 -> 23
        tipo = random.randint(1, 3)  # 1 -> 3
        monto = round(random.uniform(200, 4000), 2)  # float

        agregar_en_orden(consumos, Consumo(numero, hora, tipo, monto))


def menu():
    print('\n[ MENU ]')
    print('1. Cargar consumos ordenados')
    print('2. Mostrar consumos')
    print('3. Mostrar montos por hora y tipo')
    print('4. Generar archivo')
    print('5. Mostrar archivo')

    return positivo('Opcion')


def main():
    consumos = []
    fd = 'consumos.dat'

    while True:
        opcion = menu()

        if opcion == 1:
            cargar_consumos(consumos)
        elif not consumos:
            print('ERROR: no existen consumos')
        elif opcion == 2:
            mostrar_consumos(consumos)
        elif opcion == 3:
            mostrar_monto_por_hora_y_tipo(consumos)
        elif opcion == 4:
            generar_archivo(consumos, fd)
        elif opcion == 5:
            mostrar_archivo(fd)
        elif opcion == 6:
            break

    print('Fin')


if __name__ == '__main__':
    main()