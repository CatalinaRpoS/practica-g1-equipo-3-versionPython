''' Módulo musica.py
    Autores: Carolina Álvarez Murillo, Miller Johan Chica Acero,
             Tomás Rodríguez Taborda, Jerónimo Ledesma Patiño,
             Catalina Restrepo Salgado
    Este módulo contiene la clase Música, de quien van a heredar Canción, Lista y MeGusta
'''

# Esta clase describe los principales atributos y comportamientos de la música que se
# va a gestionar en la aplicación
class Musica: 

    def __init__(self, nombre):
        self._nombre = nombre
        self._reproducciones = 0
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getReproducciones(self):
        return self._reproducciones
    
    def setReproducciones(self, reproducciones):
        self._reproducciones = reproducciones

    # Este método van a sobreescribirlo las clases que hereden de Música
    def aumentarReproducciones(self):
        pass
    
    # Este método van a sobreescribirlo las clases que hereden de Música
    def __str__(self):
        pass