class Reserva:
    def __init__(self, codigo, email, cantidad, pais, importe):
        self.codigo = codigo
        self.email = email
        self.cantidad = cantidad
        self.pais = pais  # 1 -> 18
        self.importe = importe

    def __str__(self):
        cadena = f"\n[ Reserva {self.codigo} ]\n"
        cadena += f"Email: {self.email}\n"
        cadena += f"Cantidad: {self.cantidad}\n"
        cadena += f"Pais: {self.pais}\n"
        cadena += f"Importe: ${round(self.importe, 2)}\n"

        return cadena