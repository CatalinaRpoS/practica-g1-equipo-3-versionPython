''' Módulo musica.py
    Autores: Carolina Álvarez Murillo, Miller Johan Chica Acero,
             Tomás Rodríguez Taborda, Jerónimo Ledesma Patiño,
             Catalina Restrepo Salgado
    Este módulo contiene la clase Coleccion
'''

class Coleccion:
    
    coleccionesExistentes=[]

    def __init__(self, usuario, listas=[], cancionesRecomendadas=[],colaborativas=[]):
        self._usuario=usuario
        self._listas=listas
        self._cancionesRecomendadas=cancionesRecomendadas
        self._colaborativas=colaborativas
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
        return "Se ha agregado la lista "+lista.getNombre()+" a la Colección con éxito"

    def eliminarLista(self,lista):
        posicion=self._listas.index(lista)
        self._listas.pop(posicion)
        return "Se ha eliminado la lista "+lista.getNombre()+" de la Colección con éxito"
    
    