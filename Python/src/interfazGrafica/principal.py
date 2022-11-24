import tkinter as tk
from baseDatos.serializador import Serializador
from tkinter import messagebox

class Principal(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("Spotifree")
        self.resizable(False, False)
        
        ancho_total = self.winfo_screenwidth()
        alto_total = self.winfo_screenheight()
        
        # Aplicamos la siguiente formula para calcular donde debería posicionarse

        self.geometry(str(ancho_total )+"x"+str(alto_total)+"+"+"0"+"+"+"0")

        # Menu

        menubar = tk.Menu(self)
        
        menuArchivo = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label="Archivo", menu=menuArchivo)
        menuProceso = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Procesos y Consultas", menu=menuProceso)
        menuAyuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menuAyuda)

        self.config(menu = menubar)

        # Comandos

        menuArchivo.add_command(label="Aplicacion",command=self.informacionApp)
        menuArchivo.add_command(label="Salir", command=self.abrirVentanaInicio)

        menuProceso.add_command(label="Crear usuario")
        menuProceso.add_command(label="Crear artista")
        menuProceso.add_command(label="Mostrar usuario")
        menuProceso.add_command(label="Mostrar artista")
        menuProceso.add_command(label="Mostrar cancion")
        menuProceso.add_command(label="Acceder")

        menuAyuda.add_command(label="Acerca de")

        #Frame
        self.__frames = []
        
    def informacionApp(self):
        messagebox.showinfo("Spotifree","Spotifree es un gestor de musica. Donde el usuario podra agregar a sus artistas favoritas y sus canciones, a la misma que puede crear listas con canciones disponibles en la aplicacion. Aparte podra disfrutar de 5 funciones unicas para descubrir nuevas experiencias.")


    def agregarFrame(self, frame: tk.Frame):

        self.__frames.append(frame)

    def cambiarFrame(self, frameUtilizado: tk.Frame):
        
        for frame in self.__frames:
            frame.pack_forget()
        
        frameUtilizado.pack(expand=True, pady = (10,10))

    def abrirVentanaInicio(self):
        from interfazGrafica.inicio import Inicio
        Serializador.serializarDatos()
        self.destroy()
        Inicio()