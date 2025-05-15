import random

random.seed(9_655)
N = 21_000

cantidad_numeros_entre_1000_y_9000 = 0
cantidad_numeros_entre_9000_y_19000 = 0
cantidad_numeros_mayores_a_19000 = 0

cantidad_entre_4000_y_10000 = 0
promedio = 0

menor_no_divisible_por_5 = None

cantidad_numeros_mayores_a_15000 = 0
porcentaje = 0

for i in range(N):
    x = random.randint(1_000, 29_000)

    if 1_000 <= x < 9_000:
        cantidad_numeros_entre_1000_y_9000 += 1
    if (9_000 <= x < 19_000) and (x % 2 != 0) and (x % 7 == 0):
        cantidad_numeros_entre_9000_y_19000 += 1
    if (x >= 19_000) and (x % 3 == 0):
        cantidad_numeros_mayores_a_19000 += 1

    if 4_000 <= x <= 10_000:
        cantidad_entre_4000_y_10000 += x

    if x % 5 != 0:
        if menor_no_divisible_por_5 is None or x < menor_no_divisible_por_5:
            menor_no_divisible_por_5 = x

    if x >= 15_000:
        cantidad_numeros_mayores_a_15000 += 1

if N != 0:
    promedio = cantidad_entre_4000_y_10000 // N

if N != 0:
    porcentaje = (cantidad_numeros_mayores_a_15000 * 100) // N