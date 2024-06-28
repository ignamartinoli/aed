def es_digito(letra):
    return letra in '0123456789'


def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    cant_letras = 0
    pos_penultima = 0
    pos_ultima = 0

    cant_palabras_digito = 0

    for letra in texto:
        if letra != " " and letra != ".":
            cant_letras += 1

            if es_digito(letra):
                if pos_ultima == 0:
                    pos_ultima = cant_letras
                else:
                    pos_penultima = pos_ultima
                    pos_ultima = cant_letras
        else:
            mitad = cant_letras // 2

            if pos_ultima > mitad and pos_penultima > mitad:
                cant_palabras_digito += 1

            cant_letras = 0
            pos_penultima = 0
            pos_ultima = 0

    print(cant_palabras_digito)


if __name__ == '__main__':
    principal()
