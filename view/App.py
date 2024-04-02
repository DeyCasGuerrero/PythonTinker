import tkinter as tk
from model.calculadora import Calculadora
from controller.calcular import Calcular

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("CALCULAR PROMEDIO")
        self.geometry("800x400")
        self.config(bg="#fff")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.frames()
        self.calculo = Calculadora()
        self.promedio = Calcular()

    def frames(self):
        self.label = tk.Label(self, text="CALCULA TU PROMEDIO ", bg="#000", fg="#fff",font=("Arial", 15), padx=20)
        self.label.grid(row=0, column=0, sticky="nsew")

        frame1 = tk.Frame(self, width=700, height=200, bd=5, relief="solid", bg="white")
        frame1.grid(row=1, column=0, padx=20, pady=(20, 10))  # Ajuste del pady para frame1

        boton = tk.Button(frame1, text="Subir", width=20, height=1, bg="#2ecc71", fg="#fff", border="5", cursor="hand2", command=self.calcular_promedio)
        boton.grid(row=0, column=0, sticky="nsew")

        

        self.entry = tk.Entry(frame1, width=50)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        frame2 = tk.Frame(self, width=500, height=100, bd=5, relief="solid", bg="white")
        frame2.grid(row=2, column=0, pady=(10, 20)) 

        botonLimpiar = tk.Button(frame1, text="Eliminar", width=20, height=1, bg="#2ecc71", fg="#fff", border="5", cursor="hand2", command=self.eliminar)
        botonLimpiar.grid(row=1, column=0, sticky="nsew")
        

        self.output_label = tk.Label(frame2, text="", bg="white", width=20, font=("Arial", 10), fg= "black")
        self.output_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

    def calcular_promedio(self):
        try:
            valor = float(self.entry.get())  
            self.calculo.setNumero(valor)
            getnumero=self.calculo.getNumero()
            self.promedio.agregar(getnumero, True)
            resultado=self.promedio.promedio()
            
            self.output_label.config(text=resultado)
             
        except ValueError:
            self.output_label.config(text="Error: Ingresa un valor numérico válido")

    def eliminar(self):
        valor = 0
        self.calculo.setNumero(valor)
        getnumero=self.calculo.getNumero()
        print("Valor ingresado: ", getnumero)
        self.promedio.agregar(getnumero, False)
        self.output_label.config(text=0)  