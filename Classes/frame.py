import tkinter as tk
from PIL import ImageTk, Image
import random as rng
from tkinter import messagebox,simpledialog
import sys
import time
from Classes.casilla import Casilla
from Classes.indicador import Indicador

class Frame:
    def __init__(self):

        self.fichasGanadas = 1
        while True:
            self.fichasInGame = simpledialog.askinteger("Apuesta","¿Cuantas fichas deseas apostar?",initialvalue=0)
            if self.fichasInGame != None:
                if self.fichasInGame > self.fichasGanadas:
                    messagebox.showinfo("Espera","No puedes apostar mas fichas de las que tienes")
                elif self.fichasInGame == 0:
                    messagebox.showinfo("Espera","Debes apostar almenos una ficha")
                else:
                    break
            else:
                sys.exit()

        
        self.fichasGanadas = self.fichasGanadas - self.fichasInGame
        self.fichasMeta = 1

        self.ventana = tk.Tk()
        self.ventana.config(bg="blue")
        self.rows, self.cols = 5, 5
        
        self.TopFrame = tk.Frame(self.ventana,bg="blue")
        self.TopFrame.grid(row=0, column=0, padx=20, pady=10)

        self.MarcadorFrame = tk.Frame(self.TopFrame,bg="cyan")
        self.MarcadorFrame.grid(row=0,column=0)

        self.CasillasFrame = tk.Frame(self.ventana)
        self.CasillasFrame.config(bg="blue")
        self.CasillasFrame.grid(row=0, column=1, padx=20, pady=20)
        
        #self.BottomFrame = tk.Frame(self.ventana)
        #self.BottomFrame.grid(row=1, column=0, padx=20, pady=10)

        self.values = []
        self.slots = []
        self.icons = []
        self.positions = []
        self.cargado = False

        
        self.marcadorGanadas = tk.Label(self.MarcadorFrame, text=f"{self.fichasGanadas}",bg="cyan",fg="black",font=("Arial", 16, "bold"))
        self.marcadorInGame = tk.Label(self.MarcadorFrame, text=f"{self.fichasInGame}",bg="cyan",fg="black",font=("Arial", 16, "bold"))
        self.boton = tk.Label(self.TopFrame, text="Abandonar",pady=10,padx=40,bg="red",fg="white",font=("Arial", 18, "bold"))

        self.win = False


    def show(self):        
        print("iniciando bucle")
        self.ventana.title("Gira Voltorb")
        icono = tk.PhotoImage(file="Images/Voltorb.png")
        self.ventana.iconphoto(True,icono)
        ancho_pantalla = self.ventana.winfo_screenwidth() #método para obtener Ancho
        alto_pantalla = self.ventana.winfo_screenheight() #método para obtener Alto
        # Calcular las coordenadas para centrar la ventana
        ancho_ventana = 900
        alto_ventana = 600
        posicion_x = (ancho_pantalla - ancho_ventana) // 2 
        posicion_y = (alto_pantalla - alto_ventana) // 2

        # Establecer el tamaño y la posición de la ventana
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
        self.ventana.resizable(False, False)
        # Dimensiones de la matriz
        
        # Cargar las imágenes de los íconos
        self.slots = self.NewGame()
        self.CalcMeta()
        self.draw_matrix()
        """Marcador"""
        tk.Label(self.MarcadorFrame, text="Fichas ganadas",fg="black",bg="cyan",font=("Arial", 18, "bold")).grid(row=0, column=0,padx=10)
        tk.Label(self.MarcadorFrame, text="Fichas en juego",fg="black",bg="cyan",font=("Arial", 18, "bold")).grid(row=2, column=0,padx=10)
        self.marcadorGanadas.grid(row=1, column=0)
        self.marcadorInGame.grid(row=3, column=0)
        
        
        """Botones"""
        
        self.boton.grid(row=5, column=0)

        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)

        self.ventana.mainloop()
        
    def NewGame(self):
        print("Nueva partida")
        self.cargado = False
        slots = []
        self.values = []
        ratio = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,3]
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

    
        valuesX, valuesY = suma_ejes(valuesMatx)
        voltorbX, voltorbY = cuenta_voltorb(valuesMatx)
        for i in range(self.rows):
            for j in range(self.cols):#valuesMatx[n][m] j
                labelX = Indicador(self.CasillasFrame,total=valuesY[j],bombs=voltorbY[j])#tk.Label(self.CasillasFrame,bg="red",text=f"{valuesY[j]}")
                labelX.grid(row=self.rows,column=j, padx=10, pady=10)
            labelY = Indicador(self.CasillasFrame,total=valuesX[i],bombs=voltorbX[i])#tk.Label(self.CasillasFrame,bg="green",text=f"{valuesX[i]}")
            labelY.grid(row=i,column=self.cols, padx=10, pady=10)
        
        
        
    def update(self,event,pos):
        self.slots[pos].voltear()
        imgroute = f"Images/values/{self.slots[pos].valor}.png"
        
        self.fichasInGame = self.fichasInGame * self.slots[pos].valor

        self.marcadorInGame.config(text=f"{self.fichasInGame}")

        img = Image.open(imgroute)
        img = img.resize((50, 50), Image.ADAPTIVE)  # Redimensionar la imagen
        icon = ImageTk.PhotoImage(img)
        self.icons[pos] = icon
        self.positions[pos].config(image=self.icons[pos])
        print(self.fichasInGame,self.fichasMeta)
        if(self.fichasInGame == self.fichasMeta):
            print("Has Ganado")
            self.fichasGanadas = self.fichasInGame
            self.marcadorGanadas.config(text=f"{self.fichasGanadas}")
            continuar = messagebox.askyesno("Felicidades","¡¡¡HAS GANADO!!!\n¿Deseas continuar?")
            if continuar:
                self.reset()
            else:
                sys.exit()
        elif self.fichasInGame == 0:
                print("GAME OVER")
                continuar = messagebox.askyesno("Lastima","has peridido\n¿Deseas continuar?")
                if continuar:
                    if self.fichasGanadas == 0:
                        self.fichasGanadas = 1
                        self.marcadorGanadas.config(text=f"{self.fichasGanadas}")
                        messagebox.showinfo("","Has recibido una ficha para continuar")
                    self.reset()
                else:
                    sys.exit()

    
    def GetImage(self,pos):
        imgroute = "Images/SuperBall.png"
        if self.slots[pos].volteado:
            imgroute = f"Images/values/{self.slots[pos].valor}.png"
        else:
            imgroute = f'Images/SuperBall.png'
        return Image.open(imgroute)
    
    def CalcMeta(self):
        self.fichasMeta = 1
        for c in self.slots:
            if c.valor != 0:
                self.fichasMeta = self.fichasMeta * c.valor

    def reset(self):
        while True:
            self.fichasInGame = simpledialog.askinteger("Apuesta","¿Cuantas fichas deseas apostar?")
            if self.fichasInGame > self.fichasGanadas:
                messagebox.askquestion("Espera","No puedes apostar mas fichas de las que tienes")
            elif self.fichasInGame == 0:
                messagebox.askquestion("Espera","Debes apostar almenos una ficha")
            else:
                break
        self.fichasGanadas = self.fichasGanadas - self.fichasInGame
        self.marcadorGanadas.config(text=f"{self.fichasGanadas}")
        self.marcadorInGame.config(text=f"{self.fichasInGame}")
        self.slots = self.NewGame()
        self.CalcMeta()
        self.draw_matrix()
