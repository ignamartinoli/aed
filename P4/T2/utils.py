def promedio(total, n):
    resultado = 0
    if n != 0:
        resultado = total / n

    return resultado

def busqueda_binaria(identificador, vehiculos):
    n = len(vehiculos)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if identificador == vehiculos[c].identificador:
            pos = c
            break

        else:
            if identificador < vehiculos[c].identificador:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = -1

    return pos


def agregar_en_orden(v, vehiculo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if vehiculo.identificador == v[c].identificador:
            pos = c
            break

        else:
            if vehiculo.identificador < v[c].identificador:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [vehiculo]


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
