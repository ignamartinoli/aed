import random

from Error import Error


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


def segundos(mensaje1, mensaje2):
    s1 = positivo(mensaje1)

    while True:
        s2 = positivo(mensaje2)

        if s2 > s1:
            break
        else:
            print(f"Fuera de rango, debe ser mayor a {s1}")

    return s1, s2


def menu():
    print("\n[ Menu ]")
    print("1) Cargar errores")
    print("2) Mostrar errores")
    print("3) Errores por horario")
    print("4) Buscar por numero de sistema y mensaje")
    print("0) Salir")

    return entre(0, 4, "Opcion")


def buscar_por_numero_mensaje(errores):
    num = positivo("Numero de sistema")
    desc = input("Descripcion: ")

    se_encontro = False
    for error in errores:
        if error.sistema == num and error.mensaje == desc:
            print(error)

            se_encontro = True
            break

    if not se_encontro:
        print("No se encontro")


def errores_por_horario(errores):
    n = 24
    horarios = [0] * n

    for error in errores:
        horarios[error.horario] += 1

    mayor_cantidad = None
    horario_mayor = None
    for i in range(n):
        cantidad = horarios[i]

        if mayor_cantidad is None:
            mayor_cantidad = cantidad
            horario_mayor = i
        else:
            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                horario_mayor = i

        if cantidad > 0:
            print(f"Horario {i}: {cantidad}")

    print(f"El horario con mas errores es el {horario_mayor}")


def ordenar(errores):
    n = len(errores)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if errores[i].codigo > errores[j].codigo:
                errores[i], errores[j] = errores[j], errores[i]


def mostrar(errores):
    s1, s2 = segundos("Segundo menor", "Segundo mayor")

    for error in errores:
        if s1 <= error.segundos <= s2:
            print(error)


def cargar(errores):
    mensajes ='El Zoom se cayo', 'No me deja compartir la pantalla', 'Se me escucha con eco'

    n = positivo("Cantidad")
    for i in range(n):
        codigo = i
        sistema = random.randint(100, 900)
        mensaje = random.choice(mensajes)
        horario = random.randint(0, 23)
        segundos = random.randint(1, 100_000)

        errores.append(Error(codigo, sistema, mensaje, horario, segundos))


def main():
    errores = []

    opcion = None
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            cargar(errores)

        if len(errores) == 0:
            print("No se cargaron errores")
        else:
            if opcion == 2:
                ordenar(errores)
                mostrar(errores)
            elif opcion == 3:
                errores_por_horario(errores)
            elif opcion == 4:
                buscar_por_numero_mensaje(errores)


if __name__ == '__main__':
    main()