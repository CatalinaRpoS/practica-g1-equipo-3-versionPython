import tkinter as tk
from baseDatos.serializador import Serializador
from interfazGrafica.fieldframe import FieldFrame
from gestorAplicacion.gestorPersonas.usuario import Usuario

class Principal2():
    frames=[]

    def __init__(self, usuario, ventana_principal, ventana_anterior):
        
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

        def volver():
            from interfazGrafica.principal import Principal
            Serializador.serializarDatos()
            self.withdraw()
            Principal(ventana_principal)
            
        menubar = tk.Menu(self)
        menuArchivo = tk.Menu(menubar)
        menuProceso = tk.Menu(menubar)
        
    
        # Barra de menú
        menuProceso.add_command(label="Mostrar Listas", command= lambda: cambiarFrame(frameCrearUsuario))
        menuProceso.add_command(label="Mostrar Favoritos")
        menuProceso.add_command(label="Reproducir")
        menuProceso.add_command(label="Ranking")
        menuProceso.add_command(label="Agrupacion")
        menuProceso.add_command(label="Colaborativa")
        menuProceso.add_command(label="Resumen")
       
        menuArchivo.add_command(label="Regresar a la Ventana Anterior",command=volver)

        menubar.add_cascade(label="Archivo",menu=menuArchivo)
        menubar.add_cascade(label="Procesos y Consultas", menu=menuProceso)
        self.config(menu=menubar)

        #MostrarLista
        #FieldFrame para crear Artista
        
        frameCrearUsuario = tk.Frame(self)
        nombrecrearUsuario = tk.Label(frameCrearUsuario, text="Menu para crear el usuario", font=("Verdana", 16), fg = "#31a919")
        blankCrearUsuario = tk.Label(frameCrearUsuario,text="Por favor ingrese el nombre del usuario",font=("Verdana", 12))
        fieldCrearUsuario = FieldFrame(frameCrearUsuario, None, ["Nombre"], None, None, None)
          
          #image1 = Image.open(r"C:\Users\tomy2\Documents\practica-g1-equipo-3-versionPython\Python\src\contenidoGrafico\imagenArtista1.png")
          #resized1 = image1.resize((200,200), Image.ANTIALIAS)
          #new_pic1 = ImageTk.PhotoImage(resized1)
          
          #lab_img1 = Label(frameCrearArtista, image=new_pic1)
          #lab_img1.place(x = 100, y = 50)
          
          #image2 = Image.open(r"C:\Users\tomy2\Documents\practica-g1-equipo-3-versionPython\Python\src\contenidoGrafico\Artista2.jpg")
          #resized2 = image2.resize((200,200), Image.ANTIALIAS)
          #new_pic2 = ImageTk.PhotoImage(resized2)
          
          #lab_img2 = Label(frameCrearArtista, image=new_pic2)
          #lab_img2.place(x = 1000, y = 50)"""

        comboLabel = tk.Label(frameCrearUsuario,text="Genero",font=("Verdana", 12))
        comboLabel.place(x = 30, y = 150)

        def crearUsuario (): pass
        fieldCrearUsuario.crearBotones(crearUsuario)
          
        outputUsuario = tk.Text(frameCrearUsuario, height=100, font=("Verdana", 10))
        Principal2.frames.append(outputUsuario)
          
        nombrecrearUsuario.pack()
        blankCrearUsuario.pack()
        fieldCrearUsuario.pack(pady=(10,10))
          
        Principal2.frames.append(frameCrearUsuario)    

        self.mainloop()