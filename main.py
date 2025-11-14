from customtkinter import *
from tkinter import * 
from tkinter import filedialog
import numpy as np
import tkinter.messagebox

class App:
    
    # Constructor
    def __init__(self, master):
        
        # Atributos/Características de la clase
        # Listas de frames del GIF de inicio (splash screen)

        self.state_stop = False
        self.master = master
        self.master.title("Análisis bibliográficos de textos")
        self.master.state("zoomed")
        self.master.resizable(0, 0) 
        self.ancho = master.winfo_screenwidth()
        self.alto = master.winfo_screenheight()
        self.file_name_t = ""

        # Botones
        self.txts_btn = CTkButton(master, text = "Selecciona la ruta del archivo a examinar", command = self.elegirPathTXTs, width = self.ancho/3, height = self.alto/12)
        self.txts_btn.place(x = self.ancho/12, y = self.alto/12)

        # Etiquetas
        self.nombre_archivo_label = CTkLabel(master, text = "Nombre del archivo: ", anchor = 'w', width = self.ancho/3, height = self.alto/14)
        self.nombre_archivo_label.place(x = self.ancho/12, y = self.alto/12 * 2)
        # Nombre de los desarroladores     
        self.dev_label = CTkLabel(master, text = "Developers: Jazmín, Alexis & Emiliano", anchor = 'w', width = self.ancho/6, height = self.alto/25)  
        self.dev_label.place(x = self.ancho / 8 * 6, y = self.alto / 35 * 28) 

    # Métodos
    def elegirPathTXTs(self):
        
        # Try and except para cachar los errores al cargar el achivo
        try:
            
            cont = 0
            # Abrir la ruta del archivo
            self.filename = filedialog.askopenfilename(initialdir='C:/', title = "Abrir archivo para procesar sus textos", filetypes = (("txt files", "*.txt"), ))
            # Inicializar los renglones del archivo
            self.filas = []
            
            if self.filename != "":
                # Obtener solo el nombre del archivo sin todo el path
                self.file_name_t = os.path.basename(self.filename)
                # Setear el texto de la etiqueta para que incluya el nombre del archivo
                self.nombre_archivo_label.configure(text = "Nombre del archivo: " + str(self.file_name_t), anchor = "w")
                # "Barrer" el archivo línea por línea
                with open(self.filename, "r", encoding='utf-8') as archivo:
                    for linea in archivo:
                        # linea.isspace(): la línea contiene puros espacios en blanco
                        if linea != "" and linea.isspace() == False:
                            # rstrip() elimina el salto de línea al final
                            self.filas.append(linea.rstrip())
                            # Imprimir en consola la fila "cont"
                            print(self.filas[cont])  
                            cont += 1
            
            tkinter.messagebox.showinfo(title = "Aviso", message="Archivo Cargado")
            print(str(self.filename))

        except FileNotFoundError:
            tkinter.messagebox.showinfo(title = "Error", message="El archivo no existe en la ruta especificada")
        except:
            tkinter.messagebox.showinfo(title = "Error", message="Un error ocurrió al momento de cargar el archivo")


GUI = CTk( )
AppTXTs = App(GUI)
AppTXTs.master.mainloop()
