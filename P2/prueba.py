def es_digito(letra):
    return letra in '0123456789'


def es_vocal(letra):
    return letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def es_letra(letra):
    return 'a' <= letra <= 'z' or 'A' <= letra <= 'Z' or letra == 'ñ' or letra == 'Ñ'


def es_consonante(letra):
    return es_letra(letra) and not es_vocal(letra)


def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio


def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    for letra in texto:
        if letra != ' ' and letra != '.':
            pass
        else:
            pass


if __name__ == '__main__':
    principal()