import tkinter as tk

class Principal(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title = "Spotifree"
        self.resizable(0, 0)
        
        ancho_total = self.winfo_screenwidth()
        alto_total = self.winfo_screenheight()
        
        # Aplicamos la siguiente formula para calcular donde debería posicionarse

        self.geometry(str(ancho_total )+"x"+str(alto_total)+"+"+"0"+"+"+"0")

        # MENUUUUUUUUUUS :D

        self.__menubar = tk.Menu(self)
        self.config(menu= self.__menubar)

        menuArchivo = tk.Menu(self.__menubar, tearoff= 0)
        self.__menubar.add_cascade(label= "Archivo", menu= menuArchivo)
        menuProceso = tk.Menu(self.__menubar, tearoff= 0)
        self.__menubar.add_cascade(label= "Procesos y Consultas", menu= menuProceso)
        menuAyuda = tk.Menu(self.__menubar, tearoff= 0)
        self.__menubar.add_cascade(label= "Ayuda", menu= menuAyuda)

        # COMANDOOOOOOOOOOOOS OwO

        menuArchivo.add_command(label= "Aplicacion")
        menuArchivo.add_command(label= "Salir")

        menuProceso.add_command(label = "Crear usuario")
        menuProceso.add_command(label = "Crear artista")
        menuProceso.add_command(label = "Mostrar usuario")
        menuProceso.add_command(label = "Mostrar artista")
        menuProceso.add_command(label = "Mostrar cancion")
        menuProceso.add_command(label = "Acceder")

        menuAyuda.add_command(label = "Acerca de")

        #FRAAAAAAAAAAAME
        self.__frames = []
    
    def añadirFrame(self, frame: tk.Frame):

        self.__frames.append(frame)

    def cambiarFrame(self, frame):

        frame.pack_forget() #La cosa esa no funciona >:v

        
        
