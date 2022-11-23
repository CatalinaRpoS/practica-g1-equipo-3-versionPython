from gestorAplicacion.gestorMusica.cancion import Cancion
from gestorAplicacion.gestorMusica.coleccion import Coleccion
from gestorAplicacion.gestorMusica.lista import Lista
from gestorAplicacion.gestorMusica.meGusta import meGusta
from gestorAplicacion.gestorMusica.genero import Genero
from gestorAplicacion.gestorPersonas.persona import Persona
from gestorAplicacion.gestorPersonas.usuario import Usuario
from gestorAplicacion.gestorPersonas.artista import Artista
from baseDatos.deserializador import Deserializador
from interfazGrafica.inicio import Inicio

def main():
    Deserializador.deserializarDatos()
    aplicacion = Inicio()
    aplicacion.mainloop()
    return 0

if __name__=="__main__":

    ''' a1=Artista("Juanes",Genero.ROCK)
    a2=Artista("BTS",Genero.KPOP)
    a3=Artista("Ferxxo",Genero.REGGAETON)

    u1=Usuario("Carolina",Genero.KPOP)
    u2=Usuario("Miller",Genero.REGGAETON)
    u3=Usuario("Catalina",Genero.NO_ESPECIFICADO)
    u4=Usuario("Jeronimo",Genero.ROCK)
    u5=Usuario("Tomas",Genero.SALSA)

    c1=Cancion("Dynamite",a2,Genero.KPOP,300,2020)
    c2=Cancion("Camisa negra",a1,Genero.ROCK,200,2015)
    c3=Cancion("Ferxxo 100",a3,Genero.REGGAETON,360,2019) '''

    Deserializador.deserializarDatos()
    main()
    
    # Serializador.serializarDatos()