class ErrorAplicacion(Exception):

    def __init__(self, error):
        self.__error = "Manejo de errores de la Aplicación: " + error
    
    def mostrarMensaje(self):
        return self.__error

class UsuarioNoExiste(ErrorAplicacion):

    def __init__(self, nombre):
        super().__init__("el usuario {} no exixte".format(nombre))

