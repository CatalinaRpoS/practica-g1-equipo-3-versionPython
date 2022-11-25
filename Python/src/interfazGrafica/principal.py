import tkinter as tk
from baseDatos.serializador import Serializador
from interfazGrafica.fieldframe import FieldFrame
from gestorAplicacion.gestorPersonas.usuario import Usuario

class Principal(tk.Tk):
    
     # Frames
     frames = []

     def __init__(self):

          super().__init__()
          self.title("Spotifree")
          self.option_add('*tearOff', False)
          self.resizable(False, False)

          ancho_total = self.winfo_screenwidth()
          alto_total = self.winfo_screenheight()
       
          # Aplicamos la siguiente formula para calcular donde debería posicionarse
          self.geometry(str(ancho_total)+"x"+str(alto_total)+"+"+"0"+"+"+"0")

          # Cambiar frame
          def cambiarFrame(frameUtilizado):
               for frame in Principal.frames:
                    frame.pack_forget()
               frameUtilizado.pack(fill=tk.BOTH, expand=True, pady = (10,10))

          # Mostrar un output
          def mostrarSalida(string, texto):
               texto.delete("1.0", "end")
               texto.insert(tk.INSERT, string)
               texto.pack(fill=tk.X, expand=True, padx=(10,10))
       
          def informacionAplicacion():
               ventanaDialogo = tk.Tk()
               window_height = 220
               window_width = 800
            
               screen_width = ventanaDialogo.winfo_screenwidth()
               screen_height = ventanaDialogo.winfo_screenheight()
               x = int((screen_width/2) - (window_width/2))
               y = int((screen_height/2) - (window_height/2))
            
               ventanaDialogo.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
               ventanaDialogo.title("Spotifree")
               txt = "Spotifree es un gestor de musica.\nDonde el usuario podra agregar a sus artistas favoritas y sus canciones,\na la misma que puede crear listas con canciones disponibles en la aplicacion.\nAparte podra disfrutar de 5 funciones unicas para descubrir nuevas experiencias."
               info = tk.Label(ventanaDialogo, text=txt, justify="center", font=("Verdana", 12))
               info.pack(fill=tk.Y, expand=True)

          def autores():
               ventanaIntegrantes = tk.Tk()
               window_height = 220
               window_width = 400
            
               screen_width = ventanaIntegrantes.winfo_screenwidth()
               screen_height = ventanaIntegrantes.winfo_screenheight()
            
               x = int((screen_width/2) - (window_width/2))
               y = int((screen_height/2) - (window_height/2))
            
               ventanaIntegrantes.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
               ventanaIntegrantes.title("Spotifree")
               txt = "Autores:\nMiller Johan Chica Acero\nCatalina Restrepo Salgado\nCarolina Alvarez Murillo\nTomas Rodriguez Taborda\nJeronimo Ledesma Patiño"
               info = tk.Label(ventanaIntegrantes, text=txt, justify="center", font=("Verdana", 12))
               info.pack(fill=tk.Y, expand=True)

          def volver():
               from interfazGrafica.inicio import Inicio
               Serializador.serializarDatos()
               self.destroy()
               Inicio()
        
          menubar = tk.Menu(self)
          menuArchivo = tk.Menu(menubar)
          menuProceso = tk.Menu(menubar)
          menuAyuda = tk.Menu(menubar)  

          # Barra de menú
    
          menuAyuda.add_command(label="Acerca de", command=lambda: autores())

          menuProceso.add_command(label="Crear usuario")
          menuProceso.add_command(label="Crear artista")
          menuProceso.add_command(label="Mostrar usuarios")
          menuProceso.add_command(label="Mostrar artistas")
          menuProceso.add_command(label="Mostrar canciones")
          menuProceso.add_command(label="Acceder como usuario", command=lambda:cambiarFrame(frameBiblioteca))
      
          menuArchivo.add_command(label="Aplicacion", command= lambda: informacionAplicacion())
       
          menuArchivo.add_command(label="Salir", command= lambda: volver())

          menubar.add_cascade(label="Archivo",menu=menuArchivo)
          menubar.add_cascade(label="Procesos y consultas", menu=menuProceso)
          menubar.add_cascade(label="Ayuda", menu=menuAyuda)
          self.config(menu=menubar)

          #Funcion para abrir biblioteca
          def abrirBiblioteca():
               username=FieldBiblioteca.getValue("Nombre")
               usuario=None
               for i in Usuario.getUsuariosExistentes():
                    if i.getNombre()==username:
                         usuario=i
               if usuario==None:
                    resultado="El usuario no existe"
                    mostrarSalida(resultado,outputBiblioteca)
               else:
                    from interfazGrafica.principal2 import Principal2
                    self.destroy()
                    Principal2(usuario)
                             
          #FieldFrame para abrir biblioteca
          frameBiblioteca= tk.Frame(self)
          nombreBiblioteca = tk.Label(frameBiblioteca, text="Abrir la biblioteca de un usuario", font=("Verdana", 16), fg = "#31a919")
          descBiblioteca = tk.Label(frameBiblioteca,text="Por favor ingrese el nombre del usuario",font=("Verdana", 12))
          FieldBiblioteca = FieldFrame(frameBiblioteca, None, ["Nombre"], None, None, None)
          FieldBiblioteca.crearBotones(abrirBiblioteca)

          outputBiblioteca= tk.Text(frameBiblioteca, height=100, font=("Verdana", 10))
          Principal.frames.append(outputBiblioteca)

          nombreBiblioteca.pack()
          descBiblioteca.pack()
          FieldBiblioteca.pack(pady=(10,10))

          Principal.frames.append(frameBiblioteca)

          self.mainloop()