import tkinter as tk
from PIL import ImageTk, Image
import random as rng

from Classes.casilla import Casilla
from Classes.indicador import Indicador

class Frame:
    def __init__(self):
        self.ventana = tk.Tk()
        self.rows, self.cols = 5, 5
        self.CasillasFrame = tk.Frame(self.ventana)
        self.CasillasFrame.grid(row=0, column=0, padx=20, pady=20)
        self.values = []
        self.slots = []
        self.icons = []
        self.positions = []
        self.cargado = False
        
    def show(self):        
        print("iniciando bucle")
        self.ventana.title("Gira Voltorb")
        icono = tk.PhotoImage(file="Images/Voltorb.png")
        self.ventana.iconphoto(True,icono)
        ancho_pantalla = self.ventana.winfo_screenwidth() #método para obtener Ancho
        alto_pantalla = self.ventana.winfo_screenheight() #método para obtener Alto
        # Calcular las coordenadas para centrar la ventana
        ancho_ventana = 600
        alto_ventana = 600
        posicion_x = (ancho_pantalla - ancho_ventana) // 2 
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establecer el tamaño y la posición de la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

        # Dimensiones de la matriz
        
        # Cargar las imágenes de los íconos
        self.slots = self.NewGame()
        self.draw_matrix()

        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.mainloop()
        
    def NewGame(self):
        print("Nueva partida")
        self.cargado = False
        slots = []
        self.values = []
        ratio = [0,0,0,0,1,1,1,1,1,1,1,1,1,2,3]
        for i in range(0, self.rows * self.cols):
            n = rng.choice(ratio)        
            slot = Casilla(valor=n)
            slots.append(slot)
            self.values.append(n)
        return slots
    
    def draw_matrix(self):
        def suma_ejes(matriz):
            # Sumar cada fila
            suma_filas = [sum(fila) for fila in matriz]
            # Sumar cada columna
            suma_columnas = [sum(fila[i] for fila in matriz) for i in range(len(matriz[0]))]
            return suma_filas, suma_columnas        
        
        def cuenta_voltorb(matriz):
            # Sumar cada fila
            ceros_filas = [fila.count(0) for fila in matriz]
            # Contar ceros en cada columna
            ceros_columnas = [sum(1 for fila in matriz if fila[i] == 0) for i in range(len(matriz[0]))]
            return ceros_filas, ceros_columnas

        """Redibuja la matriz de íconos en el Frame"""
        
        for widget in self.CasillasFrame.winfo_children():
            if(widget.winfo_class() != "Frame"):
                widget.destroy()  # Limpiar los widgets anteriores 
        
        
        #print(f"largo children = {len(self.CasillasFrame.winfo_children())}")
        #print(f"largo icons = {len(self.positions)}")
        
        self.icons = []
        valuesMatx = []
        self.positions = []
        for i in range(self.rows):
            valuesMatx.append([])
            for j in range(self.cols):
                img = self.GetImage(i * self.cols + j)
                img = img.resize((50, 50), Image.ADAPTIVE)  # Redimensionar la imagen
                icon = ImageTk.PhotoImage(img)
                self.icons.append(icon)
                label = tk.Label(self.CasillasFrame, image=self.icons[i * self.cols + j],bg="blue")
                label.bind("<Button-1>",lambda event,pos = (i * self.cols + j):self.update(event,pos))
                label.grid(row=i, column=j, padx=10, pady=10)
                self.positions.append(label)
                valuesMatx[i].append(self.values[i * self.cols + j])

        if not self.cargado:
            valuesX, valuesY = suma_ejes(valuesMatx)
            voltorbX, voltorbY = cuenta_voltorb(valuesMatx)
            for i in range(self.rows):
                for j in range(self.cols):#valuesMatx[n][m] j
                    labelX = Indicador(self.CasillasFrame,total=valuesY[j],bombs=voltorbY[j])#tk.Label(self.CasillasFrame,bg="red",text=f"{valuesY[j]}")
                    labelX.grid(row=self.rows,column=j, padx=10, pady=10)
                labelY = Indicador(self.CasillasFrame,total=valuesX[i],bombs=voltorbX[i])#tk.Label(self.CasillasFrame,bg="green",text=f"{valuesX[i]}")
                labelY.grid(row=i,column=self.cols, padx=10, pady=10)
            self.cargado = True
        
        
    def update(self,event,pos):
        self.slots[pos].voltear()
        imgroute = f"Images/values/{self.slots[pos].valor}.png"
        
        img = Image.open(imgroute)
        img = img.resize((50, 50), Image.ADAPTIVE)  # Redimensionar la imagen
        icon = ImageTk.PhotoImage(img)
        self.icons[pos] = icon
        self.positions[pos].config(image=self.icons[pos])
    
    def GetImage(self,pos):
        imgroute = "Images/SuperBall.png"
        if self.slots[pos].volteado:
            imgroute = f"Images/values/{self.slots[pos].valor}.png"
        else:
            imgroute = f'Images/SuperBall.png'
        return Image.open(imgroute)