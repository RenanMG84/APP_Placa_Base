import tkinter as tk
import customtkinter
from tkinter import *
from customtkinter import *
from PIL import Image

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cálculo de Placa de Base")
    
        self.bnt1 =CTkButton(self, text='Esforços', command=self.abre_esforcos)
        self.bnt1.pack(side=LEFT, padx=5, pady=10)
        self.bnt2 =CTkButton(self, text='Materiais', command=self.abre_materiais)
        self.bnt2.pack(side=LEFT, padx=5, pady=10)
        self.bnt3 =CTkButton(self, text='Placa Base')
        self.bnt3.pack(side=LEFT, padx=5, pady=10)

        #Variáveis de esforços
        self.axial = StringVar()
        self.cortante = StringVar()
        self.momento = StringVar()

        #Variáveis de materiais
        self.fck = StringVar()
        self.fy_pb = StringVar()
        self.fu_pb = StringVar()
        self.fy_chumb = StringVar()
        self.fu_chumb = StringVar()

    def abre_esforcos(self):
        toplevel = Esforcos(self)

    def abre_materiais(self):
        toplevel = Materiais(self)

    def atualiza_esforcos(self, new_value_axial, new_value_cort, new_value_mom):
        self.axial.set(new_value_axial)
        self.cortante.set(new_value_cort)
        self.momento.set(new_value_mom)

    def atualiza_materiais(self, new_value_fck, new_value_fy_pb, new_value_fu_pb, new_value_fy_chumb, new_value_fu_chumb):
        self.fck.set(new_value_fck)
        self.fy_pb.set(new_value_fy_pb)
        self.fu_pb.set(new_value_fu_pb)
        self.fy_chumb.set(new_value_fy_chumb)
        self.fu_chumb.set(new_value_fu_chumb)

class Esforcos(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Esforços")
        self.geometry('250x270+500+500')

        self.lbl_for_axial = CTkLabel(self, text='Força axial (kN)')
        self.lbl_for_axial.pack(padx=5, pady=5)
        self.txt_forca = CTkEntry(self, width=60)
        self.txt_forca.insert(0, self.master.axial.get())
        self.txt_forca.pack(padx=5, pady=5)

        self.lbl_for_cort = CTkLabel(self, text='Força cortante (kN)')
        self.lbl_for_cort.pack(padx=5, pady=5)
        self.txt_cort = CTkEntry(self, width=60)
        self.txt_cort.insert(0, self.master.cortante.get())
        self.txt_cort.pack(padx=5, pady=5)

        self.lbl_for_mom = CTkLabel(self, text='Momento Fletor (kN)')
        self.lbl_for_mom.pack(padx=5, pady=5)
        self.txt_mom = CTkEntry(self, width=60)
        self.txt_mom.insert(0, self.master.momento.get())
        self.txt_mom.pack(padx=5, pady=5)

        self.btn_pass = CTkButton(self, text= "Ok", corner_radius=32, border_width=2, border_color='white', command=self.passa_valores)
        self.btn_pass.pack(side=BOTTOM, fill='y')

    def passa_valores(self):
        passa_axial = self.txt_forca.get()
        passa_cort = self.txt_cort.get()
        passa_mom = self.txt_mom.get()
        self.master.atualiza_esforcos(passa_axial, passa_cort, passa_mom)
        self.destroy()

class Materiais(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Materiais")
        #self.geometry('250x270+500+500')

        self.lbl_conc = CTkLabel(self, text='Características do concreto')
        self.lbl_conc.grid(row=0, column=0, columnspan=2)
        self.lbl_fck = CTkLabel(self, text='Fck (MPa)')
        self.lbl_fck.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
        self.ent_fck = CTkEntry(self, width=60)
        self.ent_fck .insert(0, self.master.fck.get())
        self.ent_fck.grid(row=2, column=0, padx=10, pady=2, columnspan=2)
        self.lbl_aco = CTkLabel(self, text='Características do aço da placa de base')
        self.lbl_aco.grid(row=3, column=0, columnspan=2)
        self.lbl_fy_pla = CTkLabel(self, text='Fy (MPa)')
        self.lbl_fy_pla.grid(row=4, column=0, padx=10, pady=5)
        self.ent_fy_pla = CTkEntry(self, width=60)
        self.ent_fy_pla.insert(0, self.master.fy_pb.get())
        self.ent_fy_pla.grid(row=5, column=0, padx=10, pady=2)
        self.lbl_fu_pla = CTkLabel(self, text='Fu (MPa)')
        self.lbl_fu_pla.grid(row=4, column=1, padx=10, pady=5)
        self.ent_fu_pla = CTkEntry(self, width=60)
        self.ent_fu_pla.insert(0, self.master.fu_pb.get())
        self.ent_fu_pla.grid(row=5, column=1, padx=10, pady=2)
        self.lbl_chumb = CTkLabel(self, text='Características do aço do chumbador')
        self.lbl_chumb.grid(row=6, column=0, columnspan=2)
        self.lbl_fy_chumb = CTkLabel(self, text='Fy (MPa)')
        self.lbl_fy_chumb.grid(row=7, column=0, padx=10, pady=5)
        self.ent_fy_chumb = CTkEntry(self, width=60)
        self.ent_fy_chumb.insert(0, self.master.fy_chumb.get())
        self.ent_fy_chumb.grid(row=8, column=0, padx=10, pady=2)
        self.lbl_fu_chumb = CTkLabel(self, text='Fu (MPa)')
        self.lbl_fu_chumb.grid(row=7, column=1, padx=10, pady=5)
        self.ent_fu_chumb = CTkEntry(self, width=60)
        self.ent_fu_chumb.insert(0, self.master.fu_chumb.get())
        self.ent_fu_chumb.grid(row=8, column=1, padx=10, pady=2)

        self.btn_pass = CTkButton(self, text= "Ok", corner_radius=32, border_width=2, border_color='white', command=self.passa_valores)
        self.btn_pass.grid(row=9, column=0, columnspan=2)

    def passa_valores(self):
        passa_fck = self.ent_fck.get()
        passa_fy_pb = self.ent_fy_pla.get()
        passa_fu_pb = self.ent_fu_pla.get()
        passa_fy_chumb = self.ent_fy_chumb.get()
        passa_fu_chumb = self.ent_fu_chumb.get()
        self.master.atualiza_materiais(passa_fck, passa_fy_pb, passa_fu_pb, passa_fy_chumb, passa_fu_chumb)
        self.destroy()

class PlacaBase(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Esforços")
        self.geometry('250x270+500+500')

        #Imagem da placa
        my_image = customtkinter.CTkImage(light_image=Image.open("placa2.png"), size=(30, 30))
        image_label = customtkinter.CTkLabel(self, image=my_image).pack()  # display image with a CTkLabel

        self.lbl_for_axial = CTkLabel(self, text='Força axial (kN)')
        self.lbl_for_axial.pack(padx=5, pady=5)
        self.txt_forca = CTkEntry(self, width=60)
        self.txt_forca.insert(0, self.master.axial.get())
        self.txt_forca.pack(padx=5, pady=5)

        self.lbl_for_cort = CTkLabel(self, text='Força cortante (kN)')
        self.lbl_for_cort.pack(padx=5, pady=5)
        self.txt_cort = CTkEntry(self, width=60)
        self.txt_cort.insert(0, self.master.cortante.get())
        self.txt_cort.pack(padx=5, pady=5)

        self.lbl_for_mom = CTkLabel(self, text='Momento Fletor (kN)')
        self.lbl_for_mom.pack(padx=5, pady=5)
        self.txt_mom = CTkEntry(self, width=60)
        self.txt_mom.insert(0, self.master.momento.get())
        self.txt_mom.pack(padx=5, pady=5)

        self.btn_pass = CTkButton(self, text= "Ok", corner_radius=32, border_width=2, border_color='white', command=self.passa_valores)
        self.btn_pass.pack(side=BOTTOM, fill='y')

    def passa_valores(self):
        passa_axial = self.txt_forca.get()
        passa_cort = self.txt_cort.get()
        passa_mom = self.txt_mom.get()
        self.master.atualiza_esforcos(passa_axial, passa_cort, passa_mom)
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
