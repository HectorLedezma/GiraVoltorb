import random as rng
import tkinter as tk
from PIL import Image, ImageTk


class Indicador(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label0 = tk.Label(self, text="Componente 1")
        self.label1 = tk.Label(self, text="Componente 1")
        
        self.label0.pack()
        self.label1.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Matriz de Íconos")

componente1 = Indicador(root)
componente1.pack(side="top", fill="x", padx=10, pady=10)
# Dimensiones de la matriz
rows, cols = 5, 5

# Cargar las imágenes de los íconos
icons = []
for i in range(0, rows * cols + 1):
    # Reemplaza 'icon_path' con la ruta de tu imagen
    ratio = [0,0,0,0,1,1,1,1,1,1,1,1,1,2,3]
    n = rng.choice(ratio)
    img = Image.open(f'Images/values/{n}.png')
    img = img.resize((50, 50), Image.ADAPTIVE)  # Redimensionar la imagen
    icon = ImageTk.PhotoImage(img)
    icons.append(icon)

# Colocar los íconos en la matriz
for i in range(rows):
    for j in range(cols):
        label = tk.Label(root, image=icons[i * cols + j],bg='blue')
        label.grid(row=i, column=j, padx=10, pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
