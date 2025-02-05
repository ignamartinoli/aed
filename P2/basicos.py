def es_vocal(caracter):
    return caracter in 'aeiouAEIOU'


cadena = 'Aritos de platasss.'  # input("Ingrese una cadena: ")

# SE RESETEA NO TE OLVIDES
contador = 0
incluye_a = False
empieza_con_vocal = False
hay_t_despues_de_tercer = False

cantidad_palabras_mayores_6 = 0
cantidad_palabras_mayores_4_y_a = 0
cantidad_empieza_vocal_y_t_despues_tercer = 0

for caracter in cadena:
    # Afuera de palabra
    if caracter == ' ' or caracter == '.':
        print(caracter)
        if contador > 6:
            cantidad_palabras_mayores_6 += 1

        if contador > 4 and incluye_a:
            cantidad_palabras_mayores_4_y_a += 1

        if empieza_con_vocal and hay_t_despues_de_tercer:
            cantidad_empieza_vocal_y_t_despues_tercer += 1

        # Reset
        contador = 0
        incluye_a = False
        empieza_con_vocal = False
        hay_t_despues_de_tercer = False

    # Adentro de palabra
    else:
        # print(caracter)
        contador += 1

        if caracter == 'a' or caracter == 'A':
            incluye_a = True

        if contador == 1 and es_vocal(caracter):
            empieza_con_vocal = True

        if contador >= 3 and caracter == 't':
            hay_t_despues_de_tercer = True


print(f"Cantidad palabras mayores a 4 y con A: {cantidad_palabras_mayores_4_y_a}")
print(f"Cantidad palabras mayores a 6: {cantidad_palabras_mayores_6}")
print(
    f"Cantidad palabras empiezan con vocal y t despues de tercer: {cantidad_empieza_vocal_y_t_despues_tercer}"
)
