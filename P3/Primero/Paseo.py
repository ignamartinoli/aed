class Paseo:
    def __init__(self, id, nombre, tipo, monto):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo  # 0 -> 19
        self.monto = monto

    def __str__(self):
        cadena = f"\n[ Paseo {self.id} ]\n"
        cadena += f"Nombre: {self.nombre}\n"
        cadena += f"Tipo: {self.tipo}\n"
        cadena += f"Monto: ${round(self.monto, 2)}\n"

        return cadena