import tkinter as tk
from baseDatos.serializador import Serializador

class Principal(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("Spotifree")
        self.resizable(False, False)
        
        ancho_total = self.winfo_screenwidth()
        alto_total = self.winfo_screenheight()
        
        # Aplicamos la siguiente formula para calcular donde debería posicionarse

        self.geometry(str(ancho_total )+"x"+str(alto_total)+"+"+"0"+"+"+"0")

        # MENUUUUUUUUUUS :D

        menubar = tk.Menu(self)
        
        menuArchivo = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label="Archivo", menu=menuArchivo)
        menuProceso = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Procesos y Consultas", menu=menuProceso)
        menuAyuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menuAyuda)

        self.config(menu = menubar)

        # COMANDOOOOOOOOOOOOS OwO

        menuArchivo.add_command(label="Aplicacion")
        menuArchivo.add_command(label="Salir", command=self.abrirVentanaInicio)

        menuProceso.add_command(label="Crear usuario")
        menuProceso.add_command(label="Crear artista")
        menuProceso.add_command(label="Mostrar usuario")
        menuProceso.add_command(label="Mostrar artista")
        menuProceso.add_command(label="Mostrar cancion")
        menuProceso.add_command(label="Acceder")

        menuAyuda.add_command(label="Acerca de")

        #FRAAAAAAAAAAAME
        self.__frames = []
    
    def añadirFrame(self, frame: tk.Frame):

        self.__frames.append(frame)

    def cambiarFrame(self, frame):

        frame.pack_forget() #La cosa esa no funciona >:v

    def abrirVentanaInicio(self):
        from interfazGrafica.inicio import Inicio
        Serializador.serializarDatos()
        self.destroy()
        Inicio()