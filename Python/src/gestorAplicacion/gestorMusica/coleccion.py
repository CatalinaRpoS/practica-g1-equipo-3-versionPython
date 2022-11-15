class Coleccion:
    
    coleccionesExistentes=[]

    def __init__(self, usuario, listas, cancionesRecomendadas,colaborativas):
        self._usuario=usuario
        self._listas=[]
        self._cancionesRecomendadas=[]
        self._colaborativas=[]
        Coleccion.coleccionesExistentes.append(self)
    
    def getUsuario(self):
        return self._usuario
    
    def setUsuario(self,usuario):
        self._usuario=usuario

    def getListas(self):
        return self._listas
    
    def setListas(self,listas):
        self._listas=listas
    
    @classmethod
    def getColeccionesExistentes(cls):
        return cls.coleccionesExistentes
    
    @classmethod
    def setColeccionesExistentes(cls,coleccionesExistentes):
        cls.coleccionesExistentes=coleccionesExistentes
    
    def agregarLista(self,lista):
        self._listas.append(lista)
        return ""
