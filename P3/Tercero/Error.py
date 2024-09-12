class Error:
    def __init__(self, codigo, sistema, mensaje, horario, segundos):
        self.codigo = codigo
        self.sistema = sistema
        self.mensaje = mensaje
        self.horario = horario  # 0 -> 23
        self.segundos = segundos

    def __str__(self):
        cadena = f"\n[ Error {self.codigo} ]\n"
        cadena += f"Numero de sistema: #{self.sistema}\n"
        cadena += f"Mensaje: '{self.mensaje}'\n"
        cadena += f"Horario: {self.horario}hs\n"
        cadena += f"Segundos: {self.segundos}s\n"

        return cadena