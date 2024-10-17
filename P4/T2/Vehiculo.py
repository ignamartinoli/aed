class Vehiculo:
    def __init__(self, identificador, tamano, tipo, costo):
        self.identificador = identificador
        self.tamano = tamano
        self.tipo = tipo
        self.costo = costo

    def __str__(self):
        tamanos = 'Subcompacto', 'Compacto', 'Mediano', 'Grande'
        tipos = 'Nafta', 'Gasoil', 'GNC', 'Electrico', 'Hidrogeno'

        return f'[ {self.identificador} ] {tamanos[self.tamano - 1]} - {tipos[self.tipo]} - ${round(self.costo, 2)}'