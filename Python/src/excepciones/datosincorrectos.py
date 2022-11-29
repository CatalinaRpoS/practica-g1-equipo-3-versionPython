from excepciones.erroraplicacion import ErrorAplicacion

class DatosIncorrectos(ErrorAplicacion):
    
    def __init__(self, error):
        super().__init__(error)

class Numero(DatosIncorrectos):

    def __init__(self):
        super().__init__("¡Debes ingresar un número!")