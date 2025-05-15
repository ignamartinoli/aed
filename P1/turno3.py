import random

random.seed(47)
N = 13_000

numero_menor_que_termina_en_23 = None

cantidad_numeros_entre_4000_y_11000 = 0
porcentaje = 0

for i in range(N):
    x = random.randint(1, 33_000)

    x_termina_en_23 = x % 100 == 23
    if x_termina_en_23:
        if numero_menor_que_termina_en_23 is None or x < numero_menor_que_termina_en_23:
            numero_menor_que_termina_en_23 = x

    if 4_000 <= x <= 11_000:
        cantidad_numeros_entre_4000_y_11000 += 1

# TODO: N -> 100%
# TODO: c -> ?%
# TODO: c * 100 / N
if N != 0:
    porcentaje = (cantidad_numeros_entre_4000_y_11000 * 100) // N

print("Q 3:", numero_menor_que_termina_en_23)
print("Q 4:", porcentaje)