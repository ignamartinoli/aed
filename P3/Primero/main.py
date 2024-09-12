import random

from Paseo import Paseo

def positivo(mensaje):
    while True:
        numero = int(input(f"{mensaje}: "))

        if not (numero > 0):
            print(f"Fuera de rango [0, inf)")
        else:
            return numero


def entre(menor, mayor, mensaje):
    while True:
        numero = int(input(f"{mensaje}: "))

        if not (menor <= numero <= mayor):
            print(f"Fuera de rango [{menor}, {mayor}]")
        else:
            break

    return numero


def menu():
    print("\n[ Menu ]\n")
    print("1) Cargar paseos")
    print("2) Mostrar paseos ordenados")
    print("3) Total recaudo por tipo")
    print("4) Buscar por nombre")
    print("0) Salir")

    return entre(0, 4, "Opcion")


def buscar_nombre(paseos):
    nom = input("Nombre: ")

    se_encontro = False
    for paseo in paseos:
        if paseo.nombre == nom:
            print(f"\n[ Paseo {paseo.id} ]")
            print(f"Monto: ${round(paseo.monto, 2)}\n")

            se_encontro = True
            break

    if not se_encontro:
        print("No se encontro")


def recaudo_por_paseo(paseos):
    tipos = [0] * 20

    for paseo in paseos:
        tipos[paseo.tipo] += paseo.monto

    c = positivo("Valor")
    for i in range(20):
        valor = tipos[i]
        if valor > c:
            print(f"Tipo {i}: ${round(valor, 2)}")


def ordenar(paseos):
    n = len(paseos)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if paseos[i].id > paseos[j].id:
                paseos[i], paseos[j] = paseos[j], paseos[i]


def mostrar(paseos):
    suma = 0

    for paseo in paseos:
        print(paseo)

        suma += paseo.monto

    print(f"Monto total: ${round(suma, 2)}")


def cargar(paseos):
    nombres = ("Tano", "Jorge", "Gero", "Tarqui")

    cantidad = positivo("Cantidad de paseos")
    for i in range(cantidad):
        id = i
        nombre = random.choice(nombres)
        tipo = random.randint(0, 19)
        monto = random.uniform(25_000, 80_000)

        paseos.append(Paseo(id, nombre, tipo, monto))


def main():
    paseos = []

    opcion = None
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            cargar(paseos)

        if len(paseos) == 0:
            print("No hay paseos cargados")
        else:
            if opcion == 2:
                ordenar(paseos)
                mostrar(paseos)
            elif opcion == 3:
                recaudo_por_paseo(paseos)
            elif opcion == 4:
                buscar_nombre(paseos)


if __name__ == '__main__':
    main()