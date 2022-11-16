
class Artista(): #ACTUALIZAR CON PERSONA Y SERIALIZABLE

    
    _artistasDisponibles = []
    _canciones = []
    _puntaje = 0

    def __init__(self, str_nombre, *Genero_genero):
        
        self._nombre = str_nombre
        if(Genero_genero != None):
            self.genero = Genero_genero
        else:
            self._genero = "No especificado" #ACTUALIZAR CON ENUM
        
    def getNombre(self):

        return self._nombre #str
    
    def setNombre(self, str_nombre):

        self._nombre = str_nombre

    def getCanciones(self):

        return self._canciones #list
    
    def setCanciones(self, list_canciones):

        self._canciones = list_canciones
    
    def getGenero(self):

        return self._genero #Genero
    
    def setGenero(self, Genero_genero):

        self.genero = Genero_genero
    
    def getPuntaje(self):

        return self._puntaje #float

    def setPuntaje(self, float_puntaje):

        self._puntaje = float_puntaje
    
