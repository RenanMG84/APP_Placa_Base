import tkinter as tk
import customtkinter
from tkinter import *
from customtkinter import *
from PIL import Image
from calc_placa_base import *

MainWindow = customtkinter.CTk()
MainWindow.title("Cálculo de Placa de Base")
MainWindow.resizable='false'

#FRAME 1 --------------------------------------------------------------------------------------
Frame1 = customtkinter.CTkFrame(MainWindow)
Frame1.pack(side='left')
#ESFORÇOS
label_tit1 = CTkLabel(Frame1, text = "ESFORÇOS").grid(row=0, column= 0, columnspan=3)
label_for = CTkLabel(Frame1, text = "Força Axial (kN)").grid(row=1, column=0)
label_cor = CTkLabel(Frame1, text = "Força Cortante (kN)").grid(row=1, column=1)
label_mom = CTkLabel(Frame1, text = "Momento Fletor (kN*m)").grid(row=1, column=2)
entry_for = CTkEntry(Frame1, width=60).grid(row=2, column=0, padx=10)
entry_cor = CTkEntry(Frame1, width=60).grid(row=2, column=1, padx=10)
entry_mom = CTkEntry(Frame1, width=60).grid(row=2, column=2, padx=10)
#MATERIAIS
label_tit2 = CTkLabel(Frame1, text = "MATERIAIS").grid(row=3, column= 0, columnspan=3)
label_for = CTkLabel(Frame1, text = "Fck do concreto (MPa)").grid(row=4, column=0)
label_cor = CTkLabel(Frame1, text = "Fy placa base (MPa)").grid(row=4, column=1)
label_mom = CTkLabel(Frame1, text = "Fu placa base (MPa)").grid(row=4, column=2)
entry_fck = CTkEntry(Frame1, width=60).grid(row=5, column=0, padx=10)
entry_fy_pb = CTkEntry(Frame1, width=60).grid(row=5, column=1, padx=10)
entry_fu_pb = CTkEntry(Frame1, width=60).grid(row=5, column=2, padx=10)
label_for = CTkLabel(Frame1, text = "Fy do chumbador (MPa)").grid(row=6, column=0)
label_cor = CTkLabel(Frame1, text = "Fu do chumbador (MPa)").grid(row=6, column=1)
entry_fy_ch = CTkEntry(Frame1, width=60).grid(row=7, column=0, padx=10)
entry_fu_ch = CTkEntry(Frame1, width=60).grid(row=7, column=1, padx=10)
#PLACA DE BASE
label_tit3 = CTkLabel(Frame1, text = "PLACA DE BASE").grid(row=8, column= 0, columnspan=3)
label_a1 = CTkLabel(Frame1, text = "a1 (mm)").grid(row=9, column=0)
label_cor = CTkLabel(Frame1, text = "a2 (mm)").grid(row=9, column=1)
label_mom = CTkLabel(Frame1, text = "Altura do perfil (d) (mm)").grid(row=9, column=2)
entry_a1 = CTkEntry(Frame1, width=60).grid(row=10, column=0, padx=10)
entry_a2 = CTkEntry(Frame1, width=60).grid(row=10, column=1, padx=10)
entry_d = CTkEntry(Frame1, width=60).grid(row=10, column=2, padx=10)
label_a3 = CTkLabel(Frame1, text = "a3 (mm)").grid(row=11, column=0)
label_e = CTkLabel(Frame1, text = "E (mm)").grid(row=11, column=1)
entry_a3 = CTkEntry(Frame1, width=60).grid(row=12, column=0, padx=10)
entry_e = CTkEntry(Frame1, width=60).grid(row=12, column=1, padx=10)

#FRAME 2 --------------------------------------------------------------------------------------
Frame2 = customtkinter.CTkFrame(MainWindow)
Frame2.pack(side='left')
label2 = CTkLabel(Frame2, text="AQUI VAI O DESENHO DA PLACA DE BASE").pack()
label3 = CTkLabel(Frame2, text="AQUI VAI O MEMORIAL DE CÁLCULO").pack()

MainWindow.mainloop()
