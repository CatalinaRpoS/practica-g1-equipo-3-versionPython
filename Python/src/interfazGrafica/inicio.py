import tkinter as tk

class Inicio(tk.Tk):

    def __init__(self):

        # Creación de la ventana
        super().__init__()
        self.title("Spotifree")
        self.resizable(0, 0)

        # Para eliminar las líneas punteadas de la barra de menú
        self.option_add("*tearOff",  False)

        # Para que la ventana se ajuste al tamaño de la pantalla y esté centrada
        ancho = self.winfo_screenwidth()
        alto = self.winfo_screenheight()
        ancho_total = round(ancho/2 - ancho/2)
        alto_total = round(alto/2 - alto/2)

        self.geometry(str(ancho)+"x"+str(alto)+"+"+str(ancho_total)+"+"+str(alto_total))
        
        # Creación de la barra de menú
        self.__menu = tk.Menu(self)
        menu_inicio =tk.Menu(self.__menu)
        menu_inicio.add_command(label = "Descripcion", command = lambda: print("Descripción"))
        menu_inicio.add_command(label = "Salir", command = lambda: self.destroy())
        self.__menu.add_cascade(label = "Inicio", menu = menu_inicio)
        self.config(menu = self.__menu)

        self.__frameIzquierda = FrameIzquierda(self) 

        self.__frameIzquierda.grid(row = 0, column = 0, padx = (10,10))
        self.__frameIzquierda.grid(row = 0, column = 1, padx = (10,10))

class FrameIzquierda(tk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.ventana = ventana
        self.__p3 = tk.Frame(self)
        self.__p4_1 = tk.Frame(self)
        self.__p4_2 = tk.Frame(self)

        # Saludo de bienvenida
        saludo = "¡Bienvenido a Spotifree!"
        self.__saludo = tk.Label(self.__p3, text = saludo, font = ("Segoe Print", 20), fg = "#2C34FA")
        self.__saludo.pack()

        # Descripción del sistema
        descripcion = "Spotifree es un gestor de música del que se puede hacer uso ingresando como usuario. \nCada usuario tiene una colección en la que puede administrar sus listas de reproducción, agregando y eliminando canciones."
        self.__descripcion = tk.Label(self.__p3, text = descripcion, width = 100, justify = "left", font=("Verdana", 8))
        self.__descripcion.pack()
        self.__p3.grid(row = 0, column = 0, pady = (10,10))