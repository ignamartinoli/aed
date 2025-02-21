class Paseo:
    def __init__(self, identificacion: int, nombre: str, tipo: int, monto: float):
        self.identificacion: int = identificacion
        self.nombre: str = nombre
        self.tipo: int = tipo
        self.monto: float = monto

    def __str__(self):
        return 'Id: {:<4} | Nombre: {:<15} | Tipo: {:<2} | Monto: ${:<6}'.format(
            self.identificacion, self.nombre, self.tipo, round(self.monto, 2)
        )
