from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# from PIL import ImageTk, Image
from baseDatos.serializador import Serializador
from interfazGrafica.fieldframe import FieldFrame
from gestorAplicacion.gestorPersonas.usuario import Usuario
from gestorAplicacion.gestorPersonas.artista import Artista
from gestorAplicacion.gestorMusica.cancion import Cancion
from gestorAplicacion.gestorMusica.genero import Genero
from gestorAplicacion.gestorMusica.lista import Lista
from gestorAplicacion.gestorMusica.meGusta import MeGusta

class Principal2():
    frames=[]
    
    def __init__(self, usuario: Usuario, ventana_principal, ventana_anterior):
        
        self = tk.Toplevel(ventana_principal)
        self.title("Colección de {}".format(usuario.getNombre()))
        self.option_add('*tearOff', False)
        self.resizable(False, False)

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
        menuProceso.add_command(label="Mostrar Listas", command= lambda: cambiarFrame(frameMostrarLista))
        menuProceso.add_command(label="Mostrar Favoritos", command=lambda: cambiarFrame(frameVerCanciones))
        menuProceso.add_command(label="Reproducir")
        menuProceso.add_command(label="Ranking")
        menuProceso.add_command(label="Agrupacion")
        menuProceso.add_command(label="Colaborativa")
        menuProceso.add_command(label="Resumen")
       
        menuArchivo.add_command(label="Regresar a la Ventana Anterior",command=volver)

        menubar.add_cascade(label="Archivo",menu=menuArchivo)
        menubar.add_cascade(label="Procesos y Consultas", menu=menuProceso)
        self.config(menu=menubar)

# Frame Inicial
        frameInicial= tk.Frame(self)
        nombreInicial = tk.Label(frameInicial, text="¿Cómo usar Spotifree?", font=("Segoe Print", 20), fg="#2C34FA")
        textoInicial = f"¡Bienvenido a la pantalla principal! Desde aquí puedes comenzar a explorar todas las\n" \
                         f"funciones que hemos preparado para ti. Conoce a los artistas que se han registrado en\n" \
                         f"Spotifree y dale un vistazo a todas las canciones que puedes disfrutar. Si gustas, puedes\n" \
                         f"crear una cuenta y acceder a tu propia Colección, ¿qué esperas?" 
        descInicial = tk.Label(frameInicial, text=textoInicial, font=("Verdana", 12))
       
        Principal2.frames.append(frameInicial)

        nombreInicial.pack()
        descInicial.pack()

        Principal2.frames.append(frameInicial)

        cambiarFrame(frameInicial)
        #MostrarLista

        frameMostrarLista = tk.Frame(self)
        nombreMostrarLista = tk.Label(frameMostrarLista, text="Menu para mostrar y editar listas", font=("Verdana", 16), fg = "#31a919", pady= 20)

        texto = """Selecciona MOSTRAR para ver las canciones de tu lista
Selecciona AGREGAR para añadir una cancion a tu lista
Selecciona ELIMINAR para remover una cancion de tu lista
Selecciona REPRODUCIR para escuchar tu lista"""
        blankMostrarLista = tk.Label(frameMostrarLista, text = texto, font=("Verdana", 12))
        fieldMostrarLista = FieldFrame(frameMostrarLista, None, ["Nombre Lista", "Nombre Cancion"], None, None, None)
        output = tk.Text(frameMostrarLista, border= False, width= 100)

        def MostrarLista():
            
            nombreLista = fieldMostrarLista.getValue("Nombre Lista")
            Lista = [x for x in usuario.getColeccion().getListas() if x.getNombre() == nombreLista]

            if len(Lista)>0:
                output.insert("end", Lista[0].infoLista() + "\n")
            else:
                output.insert("end", "Ingrese un nombre de lista valido \n") 
        
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
                Lista[0].aumentarReproducciones()
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
        
        def visualizar():
              texto=usuario.getFavoritos().__str__()
              mostrarSalida(texto,salidaFavoritos)

        def agregar():
              nCancion=fieldAE.getValue("Nombre cancion")
              canciones = Cancion.getCancionesDisponibles()
              c=None
              for cancion in canciones:
                  if nCancion==cancion.getNombre():
                        c=cancion
              if c==None:
                    messagebox.showinfo("Aviso", "Esa cancion no existe")
              else:
                    texto=usuario.agregarMeGusta(c)
                    mostrarSalida(texto,salidaFavoritos)

        def eliminar():
              nCancion=fieldAE.getValue("Nombre cancion")
              canciones = Cancion.getCancionesDisponibles()
              c=None
              for cancion in canciones:
                  if nCancion==cancion.getNombre():
                        c=cancion
              if c==None:
                    messagebox.showinfo("Aviso", "Esa cancion no existe")
              else:
                    texto=usuario.eliminarMeGusta(c)
                    mostrarSalida(texto,salidaFavoritos)

        def reproducir():
              usuario.reproducir(usuario.getFavoritos())
              mostrarSalida(usuario.getFavoritos().__str__(), salidaFavoritos)
        
        frameVerCanciones= tk.Frame(self)
        nombreVerCanciones = tk.Label(frameVerCanciones, text="Favoritos", font=("Segoe Print", 16), fg="#2C34FA")
        descVerCanciones = tk.Label(frameVerCanciones,text="Selecciona MOSTRAR para visualizar las canciones que tienes en favoritos\nSelecciona AGREGAR para agregar una cancion a favoritos\nSelecciona ELIMINAR para eliminar una cancion a favoritos\nSelecciona REPRODUCIR para reproducir favoritos",font=("Verdana", 12))
        fieldAE = FieldFrame(frameVerCanciones, None, ["Nombre cancion"], None, None, None)
        salidaFavoritos= tk.Text(frameVerCanciones, width= 90,font=("Segoe Print", 10),border= False)
        
        botonM: tk.Button = fieldAE.crearBotones(visualizar, texto= "MOSTRAR", Column=0)
        botonA: tk.Button = fieldAE.crearBotones(agregar, texto= "AGREGAR", Column=1)
        botonE: tk.Button = fieldAE.crearBotones(eliminar, texto= "ELIMINAR", Column=2)
        botonRepro: tk.Button = fieldAE.crearBotones(reproducir, texto= "REPRODUCIR", Column=3, Padx= 70)
    
        nombreVerCanciones.pack()
        descVerCanciones.pack()
        fieldAE.pack(pady=(10,10))
        salidaFavoritos.pack()

        Principal2.frames.append(frameVerCanciones)

        self.mainloop()