import random as rng
import tkinter as tk
from PIL import Image, ImageTk


class Indicador(tk.Frame):
    def __init__(self, parent,total,bombs, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,height=50,bg="blue")

        self.label0 = tk.Label(self, text=f"T = {total}",bg="red")
        self.label1 = tk.Label(self, text=f"V = {bombs}",bg="white")
        
        self.label0.pack()
        self.label1.pack()

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")

        # Instanciar y colocar los componentes en la ventana principal
        componente1 = Indicador(self,bombs=2,total=3)
        componente1.pack(side="top", fill="x", padx=10, pady=10)
        label = tk.Label(self,text="HOLLA XD")
        label.pack()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()