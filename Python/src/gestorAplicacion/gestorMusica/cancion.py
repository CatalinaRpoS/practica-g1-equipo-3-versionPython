from gestorAplicacion.gestorMusica.musica import Musica

class Cancion(Musica):
    __cancionesDisponibles = []
    
    def __init__(self, nombre, artista, genero, duracion, ano):
        super().__init__(nombre)
        self.__artista = artista
        self.__genero = genero
        self.__duracion = duracion
        self.__ano = ano
        Cancion.__cancionesDisponibles.append(self)
        # Para agregar la canción al portafolio del artista
        artista.agregarCancion(self)
        
    #falta simular el this    
    #falta inicializador estatico
    
    def getArtista(self):
        return self.__artista
    
    def setArtista(self, artista):
        self.__artista = artista
        
    def getGenero(self):
        return self.__genero
    
    def setGenero(self, genero):
        self.__genero = genero
    
    def getDuracion(self):
        return self.__duracion
    
    def setDuracion(self, duracion):
        self.__duracion = duracion
        
    def getAno(self):
        return self.__ano
    
    def setAno(self, ano):
        self.__ano = ano
    
    @classmethod
    def getCancionesDisponibles(cls):
        return cls.__cancionesDisponibles
    
    @classmethod
    def setCancionesDisponibles(cls, cancionesDisponibles):
        cls.__cancionesDisponibles = cancionesDisponibles
        
    def __str__(self):
        return "Se esta reproduciendo la cancion " + self.getNombre()
    
    def descripcion(self):
        return "Título: " + self.getNombre() + "\nArtista: " + self.getArtista().getNombre()
    
    @classmethod
    def topCancion(cls):
        masEscuchada = ""
        mayor = 0
        for cancion in Cancion.getCancionDisponibles(cls):
            if Cancion.getReproducciones() > mayor:
                masEscuchada = cancion
                mayor = Cancion.getReproducciones()
        
        return masEscuchada