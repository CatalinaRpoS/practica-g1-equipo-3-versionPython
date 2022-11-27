from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from PIL import ImageTk, Image
from gestorAplicacion.gestorMusica.lista import Lista
from baseDatos.serializador import Serializador
from interfazGrafica.fieldframe import FieldFrame
from gestorAplicacion.gestorPersonas.usuario import Usuario
from gestorAplicacion.gestorPersonas.artista import Artista
from gestorAplicacion.gestorMusica.cancion import Cancion
from gestorAplicacion.gestorMusica.genero import Genero
from gestorAplicacion.gestorMusica.lista import Lista
from gestorAplicacion.gestorMusica.meGusta import meGusta

class Principal2():
    frames=[]
    
    def __init__(self, usuario: Usuario, ventana_principal, ventana_anterior):
        
        self = tk.Toplevel(ventana_principal)
        self.title("Colección de {}".format(usuario.getNombre()))
        self.option_add('*tearOff', False)
        self.resizable(False, False)
        user = usuario

        ancho_total = self.winfo_screenwidth()
        alto_total = self.winfo_screenheight()
        # Aplicamos la siguiente formula para calcular donde debería posicionarse
        self.geometry(str(ancho_total)+"x"+str(alto_total)+"+"+"0"+"+"+"0")

    
        # Cambiar frame
        def cambiarFrame(frameUtilizado):
               for frame in Principal2.frames:
                    frame.place_forget()
               frameUtilizado.place(relx=0.5, rely=0.5, anchor="c")

        def mostrarSalida(string, texto):
               texto.delete("1.0", "end")
               texto.insert(tk.INSERT, string)
               texto.pack(fill=tk.X, expand=True, padx=(10,10))

        def volver():
            from interfazGrafica.principal import Principal
            Serializador.serializarDatos()
            self.withdraw()
            Principal(ventana_principal)
            
        menubar = tk.Menu(self)
        menuArchivo = tk.Menu(menubar)
        menuProceso = tk.Menu(menubar)
        
    
        # Barra de menú
        menuProceso.add_command(label="Crear/Eliminar Listas", command= lambda: cambiarFrame(frameCrearLista))
        menuProceso.add_command(label="Mostrar/Editar Listas", command= lambda: cambiarFrame(frameMostrarLista))
        menuProceso.add_command(label="Mostrar Favoritos", command=lambda: cambiarFrame(frameVerCanciones))
        menuProceso.add_command(label="Reproducir",command=lambda: cambiarFrame(frameReproducir))
        menuProceso.add_command(label="Ranking",command=lambda: cambiarFrame(frameRanking))
        menuProceso.add_command(label="Agrupacion")
        menuProceso.add_command(label="Colaborativa")
        menuProceso.add_command(label="Resumen")
       
        menuArchivo.add_command(label="Regresar a la Ventana Anterior",command=volver)

        menubar.add_cascade(label="Archivo",menu=menuArchivo)
        menubar.add_cascade(label="Procesos y Consultas", menu=menuProceso)
        self.config(menu=menubar)

# Frame Inicial
        frameInicial= tk.Frame(self)
        nombreInicial = tk.Label(frameInicial, text="Sigue explorando", font=("Verdana", 20), fg="#2C34FA")
        textoInicial = f"¡Bienvenido a tu coleccion! Desde aquí puedes visualizar tus listas y favoritoa\n" \
                         f"Reproducirlas, agregar y eliminar canciones o incluso crear listas nuevas\n" \
                         f"Ademas, contamos con unas funciones bastante novedosas\n" \
                         f"Animate a probar todo lo que tenemos para ofrecerte, ¿qué esperas?" 
        descInicial = tk.Label(frameInicial, text=textoInicial, font=("Verdana", 12))
       
        #CrearLista

        def crearLista(): 

            nombres = fieldCrearLista.getValue("Canciones").split(",")
            canciones = [cancion for cancion in Cancion.getCancionesDisponibles() if cancion.getNombre() in nombres]
    
            lista = Lista(fieldCrearLista.getValue("Nombre"), usuario, fieldCrearLista.getValue("Descripcion"),canciones)
            usuario.getColeccion().agregarLista(lista)

            return "Se ha creado tu lista con exito"
        
        def eliminarLista(): 

            for lista in usuario.getColeccion().getListas():

                if lista.getNombre() == fieldCrearLista.getValue("Nombre"):
                    usuario.getColeccion().eliminarLista(lista)
                    return "Se ha eliminado la lista " + fieldCrearLista.getValue("Nombre") + " con exito"
            
        frameCrearLista = tk.Frame(self)
        nombrecrearLista = tk.Label(frameCrearLista, text="Menu para crear/eliminar listas", font=("Verdana", 16), fg = "#31a919")
        blankCrearLista = tk.Label(frameCrearLista,text="Por favor ingrese los nombres de las canciones separados por coma", font=("Verdana", 12))
        fieldCrearLista = FieldFrame(frameCrearLista, None, ["Nombre", "Descripcion", "Canciones"], None, None, None)
          
        botonCrear: tk.Button = fieldCrearLista.crearBotones(crearLista, texto= "CREAR")
        botonEliminar: tk.Button = fieldCrearLista.crearBotones(eliminarLista, texto= "ELIMINAR", Column= 1)
          
        outputLista = tk.Text(frameCrearLista, height=100, font=("Verdana", 10))
        Principal2.frames.append(outputLista)
          
        nombrecrearLista.pack()
        blankCrearLista.pack()
        fieldCrearLista.pack(pady=(10,10))
          
        Principal2.frames.append(frameInicial)

        nombreInicial.pack()
        descInicial.pack()

        Principal2.frames.append(frameInicial)

        cambiarFrame(frameInicial)
        Principal2.frames.append(frameCrearLista)


        #MostrarLista

        frameMostrarLista = tk.Frame(self)
        nombreMostrarLista = tk.Label(frameMostrarLista, text="Menu para mostrar y editar listas", font=("Verdana", 14), fg = "#2C34FA", pady= 20)

        texto = """Selecciona MOSTRAR para ver las canciones de tu lista
Selecciona AGREGAR para añadir una cancion a tu lista
Selecciona ELIMINAR para remover una cancion de tu lista
Selecciona REPRODUCIR para escuchar tu lista"""
        blankMostrarLista = tk.Label(frameMostrarLista, text = texto, font=("Verdana", 10))
        fieldMostrarLista = FieldFrame(frameMostrarLista, None, ["Nombre Lista", "Nombre Cancion"], None, None, None)
        output = tk.Text(frameMostrarLista,font=("Verdana", 10), border= False, width= 100)

        def MostrarLista():
            
            nombreLista = fieldMostrarLista.getValue("Nombre Lista")
            Lista = [x for x in usuario.getColeccion().getListas() if x.getNombre() == nombreLista]

            if len(Lista)>0:
                messagebox.showinfo("Aviso", Lista[0].infoLista())
                # output.insert("end", Lista[0].infoLista() + "\n")
            else:
                messagebox.showinfo("Aviso", "¡Esta lista no existe!")
                # output.insert("end", "Ingrese un nombre de lista valido \n") 
        
        def AgregarCancion():

            nombreLista = fieldMostrarLista.getValue("Nombre Lista")
            nombreCancion = fieldMostrarLista.getValue("Nombre Cancion")
            lista = [x for x in usuario.getColeccion().getListas() if x.getNombre() == nombreLista]
            
            cancion = [x for x in Cancion.getCancionesDisponibles() if x.getNombre() == nombreCancion]

            if len(cancion) > 0 and len(lista):
                lista[0].agregarCancion(cancion[0])
                output.insert("end", "Cancion agregada con exito \n") 
            
            else:
                output.insert("end", "Ingrese un nombre de cancion y/o lista valido \n")  
        

        def EliminarCancion():

            nombreLista = fieldMostrarLista.getValue("Nombre Lista")
            nombreCancion = fieldMostrarLista.getValue("Nombre Cancion")
            lista = [x for x in usuario.getColeccion().getListas() if x.getNombre() == nombreLista]
            
            cancion = [x for x in Cancion.getCancionesDisponibles() if x.getNombre() == nombreCancion]

            if len(cancion) > 0 and len(lista):
                lista[0].eliminarCancion(cancion[0])
                output.insert("end", "Cancion eliminada con exito \n")   
            
            else:
                output.insert("end", "Ingrese un nombre de cancion y/o lista valido \n")    

        def ReproducirLista():

            nombreLista = fieldMostrarLista.getValue("Nombre Lista")
            Lista = [x for x in usuario.getColeccion().getListas() if x.getNombre() == nombreLista]

            if len(Lista)>0:

                usuario.reproducir(lista= Lista[0])
                output.insert("end", "Se ha reproducido la lista con exito \n")     

            else:
                output.insert("end","Ingrese un nombre de lista valido \n")
       
        botonMostrar: tk.Button = fieldMostrarLista.crearBotones(MostrarLista, texto= "MOSTRAR", Column=0)
        botonAgregar: tk.Button = fieldMostrarLista.crearBotones(AgregarCancion, texto= "AGREGAR", Column=1)
        botonEliminar: tk.Button = fieldMostrarLista.crearBotones(EliminarCancion, texto= "ELIMINAR", Column=2)
        botonReproducir: tk.Button = fieldMostrarLista.crearBotones(ReproducirLista, texto= "REPRODUCIR", Column=3, Padx= 70)
      
        nombreMostrarLista.pack()
        blankMostrarLista.pack()
        fieldMostrarLista.pack(pady=(10,10))
        output.pack()

        Principal2.frames.append(frameMostrarLista)    
        
        frameVerCanciones = tk.Frame(self)
        nombreVC = tk.Label(frameVerCanciones, text="Menu para mostrar y editar favoritos", font=("Verdana", 14), fg="#2C34FA", pady= 20)
        texto = """Selecciona MOSTRAR para ver las canciones de tus favoritos
Selecciona AGREGAR para añadir una cancion a tus favoritos
Selecciona ELIMINAR para remover una cancion de tus favoritos
Selecciona REPRODUCIR para escuchar tus favoritos"""
        desVC = tk.Label(frameVerCanciones, text = texto,font=("Verdana", 10))
        fieldFavoritos = FieldFrame(frameVerCanciones, None, ["Nombre Cancion"], None, None, None)
        salidaFavoritos = tk.Text(frameVerCanciones,font=("Verdana", 10), border= False, width= 100)

        def Mostrar():
            favoritos = usuario.getFavoritos().getFavoritos()
            if len(favoritos)>0:
               mostrarSalida(usuario.getFavoritos().__str__(),salidaFavoritos)
            else:
               messagebox.showinfo("Aviso", "No tiene canciones en favoritos")
        
        def Agregar():
              nCancion=fieldFavoritos.getValue("Nombre Cancion")
              canciones = Cancion.getCancionesDisponibles()
              c=None
              for cancion in canciones:
                  if nCancion==cancion.getNombre():
                        c=cancion
              if c==None:
                    messagebox.showinfo("Aviso", "Esta canción no existe")
              else:
                texto=usuario.agregarMeGusta(c)
                mostrarSalida(texto, salidaFavoritos)

        def Eliminar():
            nCancion = fieldFavoritos.getValue("Nombre Cancion")
            canciones = Cancion.getCancionesDisponibles()
            c = None
            for cancion in canciones:
                if nCancion == cancion.getNombre():
                    c = cancion
            if c == None:
                messagebox.showinfo("Aviso", "Esa cancion no existe")
            else:
                for cancion in usuario.getFavoritos().getFavoritos():
                    if nCancion == cancion.getNombre():
                        c = cancion
                texto = usuario.eliminarMeGusta(c)
                mostrarSalida(texto, salidaFavoritos)
  

        def Reproducir():
            favoritos = usuario.getFavoritos()
            if len(favoritos.getFavoritos()) > 0:
                mostrarSalida("Tus favoritos se estan reproduciendo", salidaFavoritos)
            else:
                messagebox.showinfo("Aviso", "No tienes canciones para reproducir")
       
        botonMostrar: tk.Button = fieldFavoritos.crearBotones(Mostrar, texto= "MOSTRAR", Column=0)
        botonAgregar: tk.Button = fieldFavoritos.crearBotones(Agregar, texto= "AGREGAR", Column=1)
        botonEliminar: tk.Button = fieldFavoritos.crearBotones(Eliminar, texto= "ELIMINAR", Column=2)
        botonReproducir: tk.Button = fieldFavoritos.crearBotones(Reproducir, texto= "REPRODUCIR", Column=3, Padx= 70)
        Principal2.frames.append(salidaFavoritos)
        nombreVC.pack()
        desVC.pack()
        fieldFavoritos.pack(pady=(10,10))

        Principal2.frames.append(frameVerCanciones)    
        
        frameReproducir = tk.Frame(self)
        nombreR= tk.Label(frameReproducir, text="Reproducir cancion", font=("Verdana", 14), fg = "#2C34FA", pady= 20)

        texto = "Selecciona REPRODUCIR para escuchar la cancion ingresada"
        desR = tk.Label(frameReproducir, text = texto, font=("Verdana", 10))
        fieldRepro = FieldFrame(frameReproducir, None, ["Nombre Cancion"], None, None, None)
        
        def reproducirCancion():
            nCancion=fieldRepro.getValue("Nombre Cancion")
            canciones = Cancion.getCancionesDisponibles()
            c=None
            for cancion in canciones:
                if nCancion==cancion.getNombre():
                    c=cancion
            if c==None:
                messagebox.showinfo("Aviso", "Esa cancion no existe")
            else:
                texto= usuario.reproducirCancion(c)
                mostrarSalida(texto,salidaRepro)
       
        repro = tk.Button(frameReproducir, text="Reproducir", font=("Verdana", 12), fg="white", bg="#2C34FA", command=reproducirCancion)
          
        salidaRepro= tk.Text(frameReproducir,font=("Verdana", 10), border= False, width= 100)
        Principal2.frames.append(salidaRepro) 

        nombreR.pack()
        desR.pack()
        fieldRepro.pack(pady=(10,10))
        repro.pack()

        Principal2.frames.append(frameReproducir) 

        frameRanking = tk.Frame(self)
        nombreRanking = tk.Label(frameRanking, text="Ranking BILLBOARD", font=("Verdana", 14), fg = "#2C34FA", pady= 20)

        desRanking = tk.Label(frameRanking, text = "Selecciona Ver para visualizar el ranking", font=("Verdana", 10))
        
        def billboard():
            artistaTop=usuario.topArtista()
            if artistaTop==None:
                imprimir="No tienes artista favorito\n"
            else:
                imprimir="Tu artista favorito es "+artistaTop.getNombre()+"\n"
            
            for artista in Artista.getArtistasDisponibles():
                puntaje=0.0
                if artista.getGenero().__eq__(Usuario.genFavoritoSpotyfree()):
                    puntaje=artista.getReproducciones(artista)*Artista.FACTORREPRODUCCIONES+artista.getMeGusta(artista)*Artista.FACTORMEGUSTA+Usuario.BONIFICACION
                    artista.setPuntaje(puntaje);
                else:
                    puntaje=artista.getReproducciones(artista)*Artista.FACTORREPRODUCCIONES+artista.getMeGusta(artista)*Artista.FACTORMEGUSTA
                    artista.setPuntaje(puntaje)
            if Cancion.topCancion()!=None:
                aBoniCancion = Cancion.topCancion().getArtista()
                oldPuntaje = aBoniCancion.getPuntaje()
                aBoniCancion.setPuntaje(oldPuntaje+Usuario.BONIFICACION)
            
            imprimir=imprimir+"\nRANKING BILLBOARD 2022\n"
            ListaArtista = Artista.ordenarPorPuntaje()
            for a in range(len(ListaArtista)):
                if a==0:
                    artistaUno=ListaArtista[a].getNombre()
                imprimir=imprimir+"#"+str(a+1)+ListaArtista[a].getNombre()+"\n"
            if artistaTop!=None:
                if artistaUno==artistaTop.getNombre():
                    imprimir=imprimir+"\n"+"FELICITACIONES! Tu artista favorito es el numero uno"
                else:
                    imprimir=imprimir+"\n"+"A seguir esforzandose para que tu artista favoritos sea el numero uno"
            mostrarSalida(imprimir,salidaRanking)
       
        ranking = tk.Button(frameRanking, text="Ver", font=("Verdana", 12), fg="white", bg="#2C34FA", command=billboard)
          
        salidaRanking= tk.Text(frameRanking,font=("Verdana", 10), border= False, width= 100)
        Principal2.frames.append(salidaRanking) 

        nombreRanking.pack()
        desRanking.pack()
        ranking.pack()

        Principal2.frames.append(frameRanking) 
        
        self.mainloop()