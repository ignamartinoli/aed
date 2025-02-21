from Paseo import Paseo
import random


def positivo(mensaje: str):
    while True:
        numero = int(input(f"{mensaje}: "))

        if not (numero > 0):
            print("Fuera de rango [0, inf)")
        else:
            break

    return numero


def entre(menor: int, mayor: int, mensaje: str):
    while True:
        numero = int(input(f"{mensaje}: "))

        if not (menor <= numero <= mayor):
            print(f"Fuera de rango [{menor}, {mayor}]")
        else:
            break

    return numero


def buscar(paseos: list[Paseo]):
    nombre = input('Nombre: ')

    for paseo in paseos:
        if paseo.nombre == nombre:
            print(f"Id: {paseo.identificacion} | Monto: ${round(paseo.monto, 2)}")
            break
    else:
        print(f"No se encontraron paseos con el nombre '{nombre}'")


def recaudacion_por_tipo(paseos: list[Paseo]):
    tipos = 20
    recaudaciones: list[float] = [0] * tipos

    cantidad_minima = positivo('Monto mínimo')

    for paseo in paseos:
        recaudaciones[paseo.tipo] += paseo.monto

    for i in range(tipos):
        recaudacion = recaudaciones[i]

        if recaudacion > cantidad_minima:
            print("Tipo {:<2} -> ${}".format(i, round(recaudacion, 2)))


def ordenar(paseos: list[Paseo]):
    n = len(paseos)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if paseos[i].identificacion > paseos[j].identificacion:
                paseos[i], paseos[j] = paseos[j], paseos[i]


def mostrar(paseos: list[Paseo]):
    for paseo in paseos:
        print(paseo)


def cargar(paseos: list[Paseo]):
    paseos.clear()

    cantidad = positivo('Cantidad de paseos')

    nombres = 'Calamuchita', 'Sierras'

    for i in range(cantidad):
        identificacion = random.randint(0, 9999)
        nombre = random.choice(nombres)
        tipo = random.randint(0, 19)
        monto = random.uniform(100, 10_000)

        paseos.append(Paseo(identificacion, nombre, tipo, monto))


def menu():
    print('-[Menu]-')
    print('1) Cargar')
    print('2) Mostrar')
    print('3) Recaudación por tipo')
    print('4) Buscar')
    print('0) Salir')

    return entre(0, 5, 'Opcion')


def principal():
    paseos: list[Paseo] = []

    while True:
        opcion = menu()

        if opcion == 1:
            cargar(paseos)
        elif not paseos:
            print('No se cargaron paseos.')
        elif opcion == 2:
            ordenar(paseos)
            mostrar(paseos)
        elif opcion == 3:
            recaudacion_por_tipo(paseos)
        elif opcion == 4:
            buscar(paseos)
        else:
            break

    print('Fin.')


if __name__ == '__main__':
    principal()
