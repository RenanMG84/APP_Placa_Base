from tkinter import *
import tkinter as tk
from calc_placa_base import *
import customtkinter
from customtkinter import *
from PIL import Image

MainWindow = customtkinter.CTk()
MainWindow.title("Cálculo de Placa de Base")
MainWindow.geometry("1000x755+250+100")

#VARIÁVEIS GLOBAIS
check_var = tk.IntVar()
radio_var = IntVar(value=0)

def muda_status_botao():
 
 if check_var.get() == 1: 
        entry_a2concr.configure(state = 'disabled', fg_color = 'gray')
        entry_a2concr.delete(0, 'end')
 else:
        entry_a2concr.configure(state = 'normal', fg_color = 'white')

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
    

#FRAMES MASTERS
FrameSUP = CTkFrame(MainWindow, border_width= 2)
FrameSUP.grid(row = 0 , column = 0, columnspan = 2)
FrameInfEsq = CTkFrame(MainWindow)
FrameInfEsq.grid(row = 1 , column = 0, sticky = 'n')
FrameInfDir = CTkFrame(MainWindow)
FrameInfDir.grid(row = 1, column =1, sticky = 'n')





#ESFORÇOS
Frame1 = CTkFrame(FrameSUP, width = 200, border_width= 2)
Frame1.pack(side = LEFT, expand = TRUE, fill = BOTH)
label_tit1 = CTkLabel(Frame1, text = "ESFORÇOS", text_color='blue')
label_tit1.grid(row = 0, column = 0, columnspan = 3, pady = 10)
label_for = CTkLabel(Frame1, text = "Força Axial")
label_for.grid(row = 1, column = 0, stick = 'e', padx = 15)
entry_axi = CTkEntry(Frame1, width=60)
entry_axi.grid(row = 1, column = 1, pady = 5)
label_mm10 = CTkLabel(Frame1, text = 'kN')
label_mm10.grid(row = 1, column = 2, padx = 10, sticky = 'w')
label_cor = CTkLabel(Frame1, text = "Força Cortante")
label_cor.grid(row = 2, column = 0, stick = 'e', padx = 15)
entry_cor = CTkEntry(Frame1, width=60)
entry_cor.grid(row = 2, column = 1, pady = 5)
label_mm11 = CTkLabel(Frame1, text = 'kN')
label_mm11.grid(row = 2, column = 2, padx = 10, sticky = 'w')
label_mom = CTkLabel(Frame1, text = "Momento Fletor")
label_mom.grid(row = 3, column = 0, stick = 'e', padx = 15)
entry_mom = CTkEntry(Frame1, width=60)
entry_mom.grid(row = 3, column = 1, pady = (5, 10))
label_mm12 = CTkLabel(Frame1, text = 'kN*m')
label_mm12.grid(row = 3, column = 2, padx = 10)

#CONCRETO
Frame2 = CTkFrame(FrameSUP, border_width= 2, width = 200)
Frame2.pack(side = LEFT, expand = TRUE, fill = BOTH)
label_tit2 = CTkLabel(Frame2, text = "CONCRETO", text_color='blue')
label_tit2.grid(row = 0, column = 0, columnspan = 3, pady = 10)
label_for = CTkLabel(Frame2, text = "Fck")
label_for.grid(row = 1, column = 0, stick = 'e', padx = 5)
entry_fck = CTkEntry(Frame2, width=60)
entry_fck.grid(row = 1, column = 1, pady = 5)
entry_fck.insert(0,'25')
label_mm13 = CTkLabel(Frame2, text = 'MPa')
label_mm13.grid(row = 1, column = 2, padx = 10, sticky = 'w')
label_a2 = CTkLabel(Frame2, text = "Área da base")
label_a2.grid(row = 2, column = 0, stick = 'e', padx = 5)
entry_a2concr = CTkEntry(Frame2, width=60)
entry_a2concr.grid(row = 2, column = 1, pady = 5)
label_mm14 = CTkLabel(Frame2, text = 'cm2')
label_mm14.grid(row = 2, column = 2, padx = 10, sticky = 'w')
check1 = CTkCheckBox(Frame2, text= 'Usar mesma área da placa base', variable= check_var, command=muda_status_botao)
check1.grid(row = 3, column = 0, columnspan = 3, pady = 10, padx = 10)

#AÇO DA PLACA BASE 
Frame3 = CTkFrame(FrameSUP, border_width= 2)
Frame3.pack(side = LEFT, expand = TRUE, fill = BOTH)
label_tit3 = CTkLabel(Frame3, text = "AÇO DA PLACA BASE", text_color='blue')
label_tit3.grid(row = 0, column = 0, columnspan = 3, pady = 10, padx = 10)
label_fy_pb = CTkLabel(Frame3, text = "Fy")
label_fy_pb.grid(row = 1, column = 0, stick = 'e', padx = 5)
entry_fy_pb = CTkEntry(Frame3, width=40)
entry_fy_pb.grid(row = 1, column = 1, pady = 5)
entry_fy_pb.insert(0,'250')
label_mm15 = CTkLabel(Frame3, text = 'MPa')
label_mm15.grid(row = 1, column = 2, padx = 10, sticky = 'w')
label_fu_pb = CTkLabel(Frame3, text = "Fu")
label_fu_pb.grid(row = 2, column = 0, stick = 'e', padx = 5)
entry_fu_pb = CTkEntry(Frame3, width=40)
entry_fu_pb.grid(row = 2, column = 1, pady = (5,10))
entry_fu_pb.insert(0,'400')
label_mm15 = CTkLabel(Frame3, text = 'MPa')
label_mm15.grid(row = 2, column = 2, padx = 10, sticky = 'w')

#AÇO DO CHUMBADOR
Frame4 = CTkFrame(FrameSUP, border_width= 2)
Frame4.pack(side = LEFT, expand = TRUE, fill = BOTH)
label_tit3 = CTkLabel(Frame4, text = "AÇO DO CHUMBADOR", text_color='blue')
label_tit3.grid(row = 0, column = 0, columnspan = 3, pady = 10, padx = 10)
label_fy_pb = CTkLabel(Frame4, text = "Fy")
label_fy_pb.grid(row = 1, column = 0, stick = 'e', padx = 5)
entry_fy_pb = CTkEntry(Frame4, width=40)
entry_fy_pb.grid(row = 1, column = 1, pady = 5)
entry_fy_pb.insert(0,'250')
label_mm15 = CTkLabel(Frame4, text = 'MPa')
label_mm15.grid(row = 1, column = 2, padx = 10, sticky = 'w')
label_fu_pb = CTkLabel(Frame4, text = "Fu")
label_fu_pb.grid(row = 2, column = 0, stick = 'e', padx = 5)
entry_fu_pb = CTkEntry(Frame4, width=40)
entry_fu_pb.grid(row = 2, column = 1, pady = (5,10))
entry_fu_pb.insert(0,'400')
label_mm15 = CTkLabel(Frame4, text = 'MPa')
label_mm15.grid(row = 2, column = 2, padx = 10, sticky = 'w')

#PLACA DE BASE
FramePB = CTkFrame(FrameInfEsq, border_width= 2)
FramePB.grid(row=1, column = 0, pady = 5, sticky = 'n')
label_tit5 = CTkLabel(FramePB, text = "PLACA DE BASE", text_color='blue')
label_tit5.grid(row = 0 , column = 0, columnspan = 6, pady = 10)
label_a1 = CTkLabel(FramePB, text = "a1")
label_a1.grid(row = 1, column = 0 , stick = 'e', padx = 10)
label_mm1 = CTkLabel(FramePB, text = 'mm')
label_mm1.grid(row = 1, column = 2, padx = 10)
entry_a1 = CTkEntry(FramePB, width=40)
entry_a1.grid(row = 1, column = 1, pady = 5)
label_a2 = CTkLabel(FramePB, text = "a2")
label_a2.grid(row = 2, column = 0, stick = 'e', padx = 10)
entry_a2 = CTkEntry(FramePB, width=40)
entry_a2.grid(row = 2, column = 1, pady = 5)
label_mm2 = CTkLabel(FramePB, text = 'mm')
label_mm2.grid(row = 2, column = 2, padx = 10)
label_d = CTkLabel(FramePB, text = "d")
label_d.grid(row = 3, column = 0, stick = 'e', padx = 10)
entry_d = CTkEntry(FramePB, width=40)
entry_d.grid(row = 3, column = 1, pady = (5, 10))
label_mm3 = CTkLabel(FramePB, text = 'mm')
label_mm3.grid(row = 3, column = 2, padx = 10)
label_a3 = CTkLabel(FramePB, text = "a3")
label_a3.grid(row = 1, column = 3, stick = 'e', padx = 10)
entry_a3 = CTkEntry(FramePB, width=40)
entry_a3.grid(row = 1, column = 4, pady = 5)
label_mm4 = CTkLabel(FramePB, text = 'mm')
label_mm4.grid(row = 1, column = 5, padx = 10)
label_e = CTkLabel(FramePB, text = "E")
label_e.grid(row = 2, column = 3, stick = 'e', padx = 10)
entry_e = CTkEntry(FramePB, width=40)
entry_e.grid(row = 2, column = 4, pady = (5, 10))
label_mm5 = CTkLabel(FramePB, text = 'mm')
label_mm5.grid(row = 2, column = 5, padx = 10)
rad_rot = CTkRadioButton(FramePB, text= 'Articulada', command=radiobutton_event, variable= radio_var, value=1)
rad_rot.grid(row = 5, column = 1, columnspan = 3, pady = 10 )
rad_eng = CTkRadioButton(FramePB, text= 'Engastada', command=radiobutton_event, variable= radio_var, value=2)
rad_eng.grid(row = 5, column = 3, columnspan = 3, pady = 10)
#IMAGEM PLACA DE BASE
my_image = customtkinter.CTkImage(light_image=Image.open("placa.png"), size=(400, 400))
image_label = customtkinter.CTkLabel(FramePB, image=my_image)  # display image with a CTkLabel
image_label.grid(row = 6, column = 0, columnspan = 6, padx = 10, pady = (0,10))

#RESULTADOS
FrameRES = CTkFrame(FrameInfDir, border_width= 2)
FrameRES.grid(row = 1, column = 1, pady = 5, sticky = 'n')
label_res = CTkLabel(FrameRES, text= 'RESULTADOS', text_color='blue')
label_res.grid(row = 0 , column = 0, columnspan = 2, pady = 10)
btn_cal = CTkButton(FrameRES, text='Calcular')
btn_cal.grid(row = 1, column = 0, pady = 5)
btn_apag = CTkButton(FrameRES, text='Apagar')
btn_apag.grid(row = 1, column = 1, pady = 5)
txt_res = CTkTextbox(FrameRES, width = 350, height= 500)
txt_res.grid(row =2, column = 0 , columnspan = 2, padx = 10, pady = (0,10))

MainWindow.mainloop()
