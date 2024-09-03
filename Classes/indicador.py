import tkinter as tk
from PIL import Image, ImageTk

class Indicador(tk.Frame):
    def __init__(self, parent,total,bombs, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,height=50,bg="green",border=2)

        self.label0 = tk.Label(self, text=f"{total}",bg="cyan",fg="black",font=("Arial", 16, "bold"),padx=15)
        #self.label1 = tk.Label(self, text=f"V = {bombs}",bg="white",border=1)

        image = Image.open("Images/Voltorb.png")
        image = image.resize((27, 27),Image.ADAPTIVE)  # Redimensionar si es necesario
        self.photo = ImageTk.PhotoImage(image)

        # Crear un Label con texto e imagen
        self.label1 = tk.Label(
            self, 
            text=f" {bombs}", 
            image=self.photo, 
            compound="left",
            bg="green",
            fg="white",
            font=("Arial", 16, "bold")
        )  
        # compound="left" coloca la imagen a la izquierda del texto
        #label.pack(pady=20)
        
        self.label0.pack()
        self.label1.pack()

class Marcador(tk.Frame):
    def __init__(self, parent,total,ganadas, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,height=50,bg="grey",border=2)

        self.label0 = tk.Label(self, text=f"T = {total}",border=1)
        
        self.label0.pack()
        self.label1.pack()
