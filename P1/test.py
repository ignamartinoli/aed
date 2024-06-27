import random

random.seed(87)

primero = None

contador = 0

for i in range(10_000):
    n = random.randint(0, 1)

    """
    Cantidad de numeros iguales al primero
    """

    if primero is None:
        primero = n
    elif n == primero:
        contador += 1

for i in range(13_000):
    n = random.randint(0, -10_000)
