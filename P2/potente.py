def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    cant_letras_palabra = 0
    primera_letra_t = False
    segunda_letra_a = False
    incluye_letra_m = False
    cant_mas_larga = None
    pos_mas_larga = None

    posicion = 0

    for letra in texto:
        if letra != " " and letra != ".":
            cant_letras_palabra += 1

            if cant_letras_palabra == 1 and letra == "t":
                primera_letra_t = True
            if cant_letras_palabra == 2 and letra == "a":
                segunda_letra_a = True

            if letra == "m":
                incluye_letra_m = True
        else:
            posicion += 1

            if primera_letra_t and segunda_letra_a and not incluye_letra_m:
                if cant_mas_larga is None:
                    cant_mas_larga = cant_letras_palabra
                    pos_mas_larga = posicion
                else:
                    if cant_mas_larga < cant_letras_palabra:
                        cant_mas_larga = cant_letras_palabra
                        pos_mas_larga = posicion

            cant_letras_palabra = 0
            primera_letra_t = False
            segunda_letra_a = False
            incluye_letra_m = False

    print(pos_mas_larga)

if __name__ == '__main__':
    principal()