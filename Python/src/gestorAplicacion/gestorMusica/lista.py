import gestorMusica.musica


class Lista(gestorMusica.musica.Musica):

    _listasExistentes = [] #List[Lista]

    def __init__(self, str_nombre, Usuario_usuario = None, str_descripcion = "", list_lista = [], list_usuarios = [], set_listaColaborativa = {}):

        super().__init__(str_nombre)
        self.usuario = Usuario_usuario
        self._descripcion = str_descripcion
        self._lista = list_lista
        self.usuarios = list_usuarios
        self._listaColaborativa = set_listaColaborativa
        Lista._listasExistentes.append(self)
    
    def duracionLista(self):

        duracion = 0
        for i in self._lista:
            duracion += i.getDuracion()
        
        return duracion

    def getLista(self):

        return self._lista #list
    
    def setLista(self, list_lista):

        self._lista = list_lista

    def getListaColaborativa(self):

        return self._listaColaborativa #list

    def setListaColaborativa(self, list_listaColaborativa):

        self._listaColaborativa = list_listaColaborativa

    def getUsuario(self):

        return self.usuario #Usuario

    def setUsuario(self, Usuario_usuario)

        self.usuario = Usuario_usuario

    def getListasExistentes():

        return Lista._listasExistentes #list
    
    def setListasExistentes(list_listasExistentes):

        Lista._listasExistentes = list_listasExistentes
    
    def getUsuarios(self):

        return self.usuarios #list
    
    def setUsuarios(self, list_usuarios):

        self.usuarios = list_usuarios
    
    def agregarCancion(self, Cancion_cancion):

        self._lista.append(Cancion_cancion)

        return "Se ha agregado la canción " + Cancion_cancion.getNombre() + " a la lista " + self.nombre + " con exito"
    
    def eliminarCancion(self, Cancion_cancion):

        self._lista.remove(Cancion_cancion)

        return "Se ha eliminado la canción " + Cancion_cancion.getNombre() + " de la lista " + self.nombre + " con exito"
    
    def toString(self):

        return "Se está reproduciendo la lista: " + self._nombre
    
    def infoLista(self):

        des = 0

        if len(self._lista) > 0:

            for i in self._lista:

                des += i.descripcion() + "\n"
            
            return "Lista: " + self._nombre + "\n" + "\n" + "Canciones: " + "\n" + des
        
        else:
            
            return "La lista: " + self._nombre + " está vacía\n"


    # MAÑANA ACABO XD


    




