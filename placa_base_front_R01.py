import tkinter as tk
import customtkinter
from tkinter import *
from customtkinter import *

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cálculo de Placa de Base")
    
        self.bnt1 =CTkButton(self, text='Esforços', command=self.abre_esforcos)
        self.bnt1.pack(side=LEFT, padx=5, pady=10)
        self.bnt2 =CTkButton(self, text='Materiais')
        self.bnt2.pack(side=LEFT, padx=5, pady=10)
        self.bnt3 =CTkButton(self, text='Placa Base')
        self.bnt3.pack(side=LEFT, padx=5, pady=10)

        self.axial = DoubleVar()
        self.label = tk.Label(self, textvariable=self.axial)
        self.label.pack()

    def abre_esforcos(self):
        toplevel = Esforcos(self)

    def atualiza_esforcos(self, new_value):
        self.var_from_toplevel.set(new_value)

class Esforcos(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Esforços")

        lbl_for_axial = CTkLabel(self, text='Força axial (kN)')
        lbl_for_axial.pack(padx=5, pady=5)
        txt_forca = CTkEntry(self, width=60)
        txt_forca.pack(padx=5, pady=5)

        btn_pass = CTkButton(self, text= "Ok", corner_radius=32, border_width=2, border_color='white', command=self.passa_valores)
        btn_pass.pack(side=BOTTOM, fill='y')

    def passa_valores(self):
        passa_axial = self.txt_forca.get()
        self.master.atualiza_esforcos(passa_axial)
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
