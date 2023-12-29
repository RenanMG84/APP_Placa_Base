from tkinter import *
from calc_placa_base import *
import customtkinter
from customtkinter import *

MainWindow = customtkinter.CTk()
MainWindow.title("Cálculo de Placa de Base")
MainWindow.geometry("1000x755+250+100")



#ESFORÇOS
Frame1 = CTkFrame(MainWindow, border_width= 2)
Frame1.place(x = 0 , y = 0)
label_tit1 = CTkLabel(Frame1, text = "ESFORÇOS")
label_tit1.pack(pady = 10)
label_for = CTkLabel(Frame1, text = "Força Axial (kN)")
label_for.pack()
entry_axi = CTkEntry(Frame1, width=60)
entry_axi.pack(pady = (0, 5))
label_cor = CTkLabel(Frame1, text = "Força Cortante (kN)")
label_cor.pack()
entry_cor = CTkEntry(Frame1, width=60)
entry_cor.pack(pady = (0, 5))
label_mom = CTkLabel(Frame1, text = "Momento Fletor (kN*m)")
label_mom.pack(padx = 10)
entry_mom = CTkEntry(Frame1, width=60)
entry_mom.pack(pady = (0, 10))

#CONCRETO
Frame2 = CTkFrame(MainWindow, border_width= 2, width = 200)
Frame2.place(x = 200, y = 0)
label_tit2 = CTkLabel(Frame2, text = "CONCRETO")
label_tit2.pack(pady = 10)
label_for = CTkLabel(Frame2, text = "Fck do concreto (MPa)")
label_for.pack()
entry_fck = CTkEntry(Frame2, width=60)
entry_fck.pack()
label_a2 = CTkLabel(Frame2, text = "Área da base do concreto (cm2)")
label_a2.pack(padx = 10)
entry_fck = CTkEntry(Frame2, width=60)
entry_fck.pack(pady = (0, 10))

#AÇO DA PLACA BASE 
Frame3 = CTkFrame(MainWindow, border_width= 2)
Frame3.place(x = 400, y = 0)
label_tit3 = CTkLabel(Frame3, text = "AÇO DA PLACA BASE")
label_tit3.pack(padx = 10, pady = 10)
label_fy_pb = CTkLabel(Frame3, text = "Fy (MPa)")
label_fy_pb.pack()
entry_fy_pb = CTkEntry(Frame3, width=60)
entry_fy_pb.pack()
label_fu_pb = CTkLabel(Frame3, text = "Fu (MPa)")
label_fu_pb.pack()
entry_fu_pb = CTkEntry(Frame3, width=60)
entry_fu_pb.pack(pady = (0, 10))

#AÇO DO CHUMBADOR
Frame4 = CTkFrame(MainWindow, border_width= 2)
Frame4.place(x = 600, y = 0)
label_tit4 = CTkLabel(Frame4, text = "AÇO DO CHUMBADOR")
label_tit4.pack(padx = 10, pady = 10)
label_fy_chum = CTkLabel(Frame4, text = "Fy (MPa)")
label_fy_chum.pack()
entry_fy_chum = CTkEntry(Frame4, width=60)
entry_fy_chum.pack()
label_fu_chum = CTkLabel(Frame4, text = "Fu (MPa)")
label_fu_chum.pack()
entry_fu_chum = CTkEntry(Frame4, width=60)
entry_fu_chum.pack(pady = (0, 10))



#PLACA DE BASE
Frame5 = CTkFrame(MainWindow, width= 200, height=250, border_width= 2)
Frame5.place(x=800, y = 0)
label_tit5 = CTkLabel(Frame5, text = "PLACA DE BASE")
label_tit5.pack(padx = 10, pady = 10)
label_a1 = CTkLabel(Frame5, text = "a1 (mm)")
label_a1.pack()
entry_a1 = CTkEntry(Frame5, width=60)
entry_a1.pack()
label_a2 = CTkLabel(Frame5, text = "a2 (mm)")
label_a2.pack()
entry_a2 = CTkEntry(Frame5, width=60)
entry_a2.pack()
label_d = CTkLabel(Frame5, text = "Altura do perfil (d) (mm)")
label_d.pack(pady = 5)
entry_d = CTkEntry(Frame5, width=60)
entry_d.pack()
label_a3 = CTkLabel(Frame5, text = "a3 (mm)")
label_a3.pack()
entry_a3 = CTkEntry(Frame5, width=60)
entry_a3.pack()
label_e = CTkLabel(Frame5, text = "E (mm)")
label_e.pack()
entry_e = CTkEntry(Frame5, width=60)
entry_e.pack()

#FRAME 2 --------------------------------------------------------------------------------------
#Frame50= customtkinter.CTkFrame(MainWindow)
#Frame2.pack(side='left')
#label2 = CTkLabel(Frame50, text="AQUI VAI O DESENHO DA PLACA DE BASE").pack()
#label3 = CTkLabel(Frame50, text="AQUI VAI O MEMORIAL DE CÁLCULO").pack()

MainWindow.mainloop()
