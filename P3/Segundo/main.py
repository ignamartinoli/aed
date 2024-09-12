import random

from Reserva import Reserva


def promedio(total, n):
    resultado = 0

    if n != 0:
        resultado = total / n

    return resultado


def positivo(mensaje):
    while True:
        n = int(input(f"{mensaje}: "))

        if n > 0:
            break
        else:
            print(f"Fuera de rango [0, inf)")

    return n


def entre(menor, mayor, mensaje):
    while True:
        n = int(input(f"{mensaje}: "))

        if not (menor <= n <= mayor):
            print(f"Fuera de rango [{menor}, {mayor}]")
        else:
            break

    return n


def menu():
    print("\n[ Menu ]")
    print("1) Cargar reservas")
    print("2) Mostrar reservas")
    print("3) Personas por pais")
    print("4) Buscar por codigo")
    print("0) Salir")

    return entre(0, 5, "Opcion")


def cargar(vector):
    nombres = "tano", "tarqui", "jorge", "gero"
    letras = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    n = positivo("Cantidad")
    for i in range(n):
        codigo = random.choice(letras) + random.choice(letras) + random.choice(letras)
        email = f"{random.choice(nombres)}@gmail.com"
        cantidad = random.randint(1, 10)
        pais = random.randint(1, 18)  # 1 -> 18
        importe = random.uniform(20_000, 40_000)

        vector.append(Reserva(codigo, email, cantidad, pais, importe))


def ordenar(reservas):
    n = len(reservas)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if reservas[i].email > reservas[j].email:
                reservas[i], reservas[j] = reservas[j], reservas[i]


def mostrar(reservas):
    imp = positivo("Importe")
    p = entre(1, 18, "Pais")

    for reserva in reservas:
        if reserva.importe > imp and reserva.pais == p:
            print(reserva)


def persona_por_pais(reservas):
    total = 0
    n = 18

    paises = [0] * n

    for reserva in reservas:
        total += reserva.cantidad
        paises[reserva.pais - 1] += reserva.cantidad

    for i in range(n):
        cantidad = paises[i]
        if cantidad > 0:
            print(f"Pais {i + 1}: {cantidad}")

    prom = promedio(total, n)
    print(f"\nPromedio: {round(prom, 2)}\n")


def buscar_por_codigo(reservas):
    codigo = input("Codigo: ")

    se_encontro = False
    for reserva in reservas:
        if reserva.codigo == codigo:
            print(f"Cantidad: {reserva.cantidad}")
            print(f"Pais: {reserva.pais}")
            print(f"Email: {reserva.email}")

            se_encontro = True
            break

    if not se_encontro:
        print("No se encontro")


def main():
    reservas = []

    opcion = None
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            cargar(reservas)

        if len(reservas) == 0:
            print("No se cargaron reservas")
        else:
            if opcion == 2:
                ordenar(reservas)
                mostrar(reservas)
            elif opcion == 3:
                persona_por_pais(reservas)
            elif opcion == 4:
                buscar_por_codigo(reservas)


if __name__ == '__main__':
    main()