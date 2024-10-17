class Consumo:
    def __init__(self, numero: str, hora):
        self.numero: str = numero
        self.hora = hora  # [0, 23]
        self.tipo = tipo  # 1: SMS, 2: llamada, 3: uso de datos
        self.monto = monto

    def __str__(self):
        return f"[ #{self.numero} ] {self.hora}hs; {self.tipo}; ${self.monto}"