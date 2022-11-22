import tkinter as tk
import pathlib
import os

class Inicio(tk.Tk):

    def __init__(self):

        # Creación de la ventana
        super().__init__()
        self.title("Spotifree")
        self.resizable(0, 0)

        # Para eliminar las líneas punteadas de la barra de menú
        self.option_add("*tearOff",  False)
        #Para crear la pantalla de tamaño completo
        ancho_total = self.winfo_screenwidth()
        alto_total = self.winfo_screenheight()

        self.geometry(str(ancho_total )+"x"+str(alto_total))

        
        # Creación de la barra de menú
        self.__menu = tk.Menu(self)
        menu_inicio =tk.Menu(self.__menu)
        menu_inicio.add_command(label = "Descripcion", command = lambda: self.descripcion())
        menu_inicio.add_command(label = "Salir", command = lambda: self.destroy())
        self.__menu.add_cascade(label = "Inicio", menu = menu_inicio)
        self.config(menu = self.__menu)

        self.__frameIzquierda = FrameIzquierda(self) 
        self.__frameDerecha = FrameDerecha(self) 
        self.__frameIzquierda.grid(row = 0, column = 0, padx = (10,10))
        self.__frameDerecha.grid(row = 0, column = 1, padx = (10,10))

    def descripcion(self):
        print("Hola")
        self.__frameIzquierda.descripcion.pack(pady=(10,0))
        self.geometry("1420x840")

        
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
        descripcion = f"Spotifree es un gestor de música del que se puede hacer uso ingresando como usuario. \nCada usuario tiene una colección en la que puede administrar sus listas de reproducción, \nagregando y eliminando canciones."
        self.descripcion = tk.Label(self.__p3, text = descripcion, width = 85, justify = "left", font=("Verdana", 8))
        
        self.__p3.grid(row = 0, column = 0, pady = (10,10))

class FrameDerecha(tk.Frame):
    __posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def __init__(self, ventana):
        super().__init__(ventana)
        
        self.__p5 = tk.Frame(self)
        self.__p6 = tk.Frame(self)

        self.__text = None
        self.__next_cf = 0
        self.__fotos = [None, None, None, None]
        self.__labels = []


        self.cargarCFTexto(0)
        
        for i in range(0, 4):
            label = tk.Label(self.__p6, width = 320, height = 240)
            (r, c) = FrameDerecha.__posicion_imagen[i]
            label.grid(row = r, column = c)
            self.__labels.append(label)
            # Se cargan las primeras imagenes
            self.cargarCFImagen(0, i)


        self.__p5.grid()
        self.__p6.grid()

    # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    def proximo(self, _):
        if self.__next_cf < 4:
            self.__next_cf = self.__next_cf + 1
        else:
            self.__next_cf = 0

        self._fotos = [None, None, None, None]
        self.cargarCFTexto(self.__next_cf)
        for i in range(0, 4):
            self.cargarCFImagen(self.__next_cf, i)


    def cargarCFImagen(self, cf_num, numero):
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\contenidoGrafico\CF{0}{1}.png'.format(cf_num, numero))
        foto = tk.PhotoImage(file = path)
        self.__labels[numero].configure(image = foto)
        self.__labels[numero].image = foto

    # Carga el texto para la hoja de vida respecto al numero asignado

    def cargarCFTexto(self, numero):
        self.__text = tk.Text(self.__p5, height = 10, font = ("Verdana",10), width = 80)
        self.__text.grid(row = 1, column = 0)
        self.__text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\contenidoGrafico\CF{0}4.txt'.format(numero))

        with open(path, "r+") as cf_text:
            self.__text.insert(tk.INSERT, cf_text.read())
