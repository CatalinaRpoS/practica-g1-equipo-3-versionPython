class meGusta(Lista):
    
    __favoritosExistentes = []
    
    #falta inicializador estatico
    
    def __init__(self, favoritos, usuario):
        super().__init__("Tus Me Gusta", usuario, "Tus canciones favoritos")
        self.__favoritos = list(favoritos)
        self.__usuario = usuario
        meGusta.__favoritosExistentes.append(self)
        
    def agregarCancion(self, cancion):
        self.__favoritos.append(cancion)
        return "Cancion agregada con exito a tus Me Gusta"
    
    def eliminarCancion(self, cancion):
        self.__favoritos.remove(cancion)
        return "Cancion eliminado con exito de tus Me Gusta"
    
    def getFavoritos(self):
        return self.__favoritos
    
    def setFavoritos(self, favoritos):
        self.__favoritos = favoritos
        
    def getFavoritosExistentes(self):
        return self.__favoritosExistentes
    
    def setFavoritosExistentes(self, favoritosExistentes):
        self.__favoritosExistentes = favoritosExistentes
        
    def totalPorGenero(self, genero):
        total = 0
        for cancion in meGusta.getFavoritos(self):
            if(Cancion.getGenero() == genero):
                total += 1
        
        return total
    
    def __str__(self):
        des = ""
        lista = usuario.getFavoritos(self).getFavoritos(self)
        if(len(lista) > 0):
            for cancion in lista:
                des += cancion.descripcion() + "\n"
            
            return "Tus Canciones Favoritas:" + "\n" + "\n" + "Canciones: " + "\n" + des
        
        else:
            return "No tienes canciones favoritas"