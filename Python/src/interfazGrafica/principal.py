import tkinter as tk
from baseDatos.serializador import Serializador

class Principal(tk.Tk):

    #Frame
    frames = []
        

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

        menuAyuda.add_command(label="Acerca de",command=self.integrantes)

        
    def informacionApp(self):
        ventanaDialogo=tk.Toplevel(self)
        window_height = 220
        window_width = 800

        screen_width = ventanaDialogo.winfo_screenwidth()
        screen_height = ventanaDialogo.winfo_screenheight()

        x= int((screen_width/2) - (window_width/2))
        y= int((screen_height/2) - (window_height/2))

        ventanaDialogo.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
        ventanaDialogo.title("Spotifree")
        txt="Spotifree es un gestor de musica.\nDonde el usuario podra agregar a sus artistas favoritas y sus canciones,\na la misma que puede crear listas con canciones disponibles en la aplicacion.\nAparte podra disfrutar de 5 funciones unicas para descubrir nuevas experiencias."
        info=tk.Label(ventanaDialogo,text=txt,justify = "center",font=("Verdana", 12))
        info.pack(fill=tk.Y, expand=True)

    def integrantes(self):
        ventanaIntegrantes=tk.Toplevel(self)
        window_height = 220
        window_width = 400

        screen_width = ventanaIntegrantes.winfo_screenwidth()
        screen_height = ventanaIntegrantes.winfo_screenheight()

        x= int((screen_width/2) - (window_width/2))
        y= int((screen_height/2) - (window_height/2))

        ventanaIntegrantes.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
        ventanaIntegrantes.title("Spotifree")
        txt="Autores:\n Miller Johan Chica Acero\nCatalina Restrepo Salgado\nCarolina Alvarez Murillo\nTomas Rodriguez Taborda\nJeronimo Ledesma Patiño"
        info=tk.Label(ventanaIntegrantes,text=txt,justify = "center",font=("Verdana", 12))
        info.pack(fill=tk.Y, expand=True)
    
    def cambiarFrame(frameUtilizado):
        
        for frame in Principal.frames:
            frame.pack_forget()
        
        frameUtilizado.pack(expand=True, pady = (10,10))

    def abrirVentanaInicio(self):
        from interfazGrafica.inicio import Inicio
        Serializador.serializarDatos()
        self.destroy()
        Inicio()