# TODO: banderas
# TODO: acumuladores
# TODO: contadores

import random

random.seed(29)
N = 10_000

cantidad_numeros_entre_1_y_10000 = 0
cantidad_numeros_entre_10000_y_20000 = 0
cantidad_numeros_mayores_a_20000 = 0

cantidad_numeros_divisibles_por_6 = 0

for i in range(N):
    x = random.randint(1, 25_000)

    if 1 <= x < 10_000:
        cantidad_numeros_entre_1_y_10000 += 1
    if 10_000 <= x < 20_000:
        cantidad_numeros_entre_10000_y_20000 += 1
    if x >= 20_000:
        cantidad_numeros_mayores_a_20000 += 1

    if x % 6 == 0:
        cantidad_numeros_divisibles_por_6 += 1


print("Q 1, E 1:", cantidad_numeros_entre_1_y_10000)
print("Q 1, E 2:", cantidad_numeros_entre_10000_y_20000)
print("Q 1, E 3:", cantidad_numeros_mayores_a_20000)

print("Q 2:", cantidad_numeros_divisibles_por_6)