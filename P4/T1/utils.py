def agregar_en_orden(v, consumo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if consumo.numero == v[c].numero:
            pos = c
            break

        else:
            if consumo.numero < v[c].numero:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [consumo]


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