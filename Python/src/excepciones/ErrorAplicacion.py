class ErrorAplicacion(Exception):

    def __init__(self, error) -> None:
        self._error = "Manejo de errores de la Aplicación: " + error

class UsuarioNoExiste(ErrorAplicacion):

    def __init__(self, nombre):
        super().__init__("el usuario {} no exixte".format(nombre))

