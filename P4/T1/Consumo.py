class Consumo:
    def __init__(self, numero, hora, tipo, monto):
        self.numero = numero
        self.hora = hora
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        tipos = 'SMS', 'Llamada', 'Uso de datos'

        return f'[ #{self.numero} ] {self.hora}hs - {tipos[self.tipo - 1]} - ${self.monto}'