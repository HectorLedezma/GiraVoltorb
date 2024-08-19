import tkinter as tk
from PIL import Image, ImageTk

class Indicador(tk.Frame):
    def __init__(self, parent,total,bombs, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,height=50,bg="blue",border=2)

        self.label0 = tk.Label(self, text=f"T = {total}",bg="red",fg="white",border=1)
        self.label1 = tk.Label(self, text=f"V = {bombs}",bg="white",border=1)
        
        self.label0.pack()
        self.label1.pack()

class Marcador(tk.Frame):
    def __init__(self, parent,total,ganadas, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,height=50,bg="grey",border=2)

        self.label0 = tk.Label(self, text=f"T = {total}",border=1)
        
        self.label0.pack()
        self.label1.pack()
