import customtkinter
from tkinter import *
from customtkinter import *
from tkinter import *

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode('light')
        #VARIÁVEIS GLOBAIS
        #esforços
        f_axial = 0.0
        f_cort = 0.0
        mom_flet = 0.0
        #concreto
        fck = 20
        #Material placa base
        fy_pb=250
        fu_pb=400
        #Chumbador
        fy_chumb = 250
        fu_chumb = 400
        #FUNÇÕES
        #FRAME SUPERIOR COM BOTÕES-----------------------------------
        frame1 = CTkFrame(Main)
        frame1.grid(row=0, column=0, sticky=W)
        bnt1 =CTkButton(frame1, text='Esforços')
        bnt1.pack(side=LEFT, padx=5, pady=10)
        bnt2 =CTkButton(frame1, text='Materiais')
        bnt2.pack(side=LEFT, padx=5, pady=10)
        bnt3 =CTkButton(frame1, text='Placa Base')
        bnt3.pack(side=LEFT, padx=5, pady=10)
        #FRAMES INTERMEDIÁRIOS ------------------------------------
        frame3 = CTkFrame(Main)
        frame3.grid(row=1, column=0)
        lbl_res = CTkLabel(frame3, text = 'Resultados')
        lbl_res.pack(side=TOP)
        txt_res = CTkTextbox(frame3, border_color='black', border_width=2, width=400, height=500)
        txt_res.pack(padx=5)
        #FRAME CALCULAR------ -------------------------------------
        frame4 = CTkFrame(Main)
        frame4.grid(row=2, column=0)
        btn_calc = CTkButton(frame4, text='Calcular')
        btn_calc.pack(side=LEFT, padx=10, pady=10)
        btn_exp = CTkButton(frame4, text='Gerar relatório')
        btn_exp.pack(side=LEFT, padx=10, pady=10)
        frame5 = CTkFrame(Main)
        frame5.grid(row=3, column=0)
        lbl_cred = CTkLabel(frame5, text = 'Aplicativo desenvolvido por Eng. Renan M. Guimarães \n email: renanguimaraes@live.com', font=('Calibri', 10))
        lbl_cred.pack(pady=10)

class Frm_Esforcos(customtkinter.CTkToplevel):
    def __init__(self, master, f_axial, f_cort, mom_fle):
        super().__init__(master)
        lbl_axial = CTkLabel(self, text='Força Axial (kN)')
        lbl_axial.grid(row=0, column=0, padx=10, pady=5)
        self.ent_axial = CTkEntry(self, width=60)
        self.ent_axial.grid(row=1, column=0, padx=10, pady=2)
        self.ent_axial.set(f_axial)
        lbl_cort = CTkLabel(self, text='Força Cortante (kN)')
        lbl_cort.grid(row=0, column=1, padx=10, pady=5)
        self.ent_cort = CTkEntry(self, width=60)
        self.ent_cort.set(f_cort)
        self.ent_cort.grid(row=1, column=1, padx=10, pady=2)
        lbl_mom = CTkLabel(self, text='Momento Fletor (kN*m)')
        lbl_mom.grid(row=0, column=2, padx=10, pady=5)
        self.ent_mom = CTkEntry(self, width=60)
        self.ent_mom.set(mom_fle)
        self.ent_mom.grid(row=1, column=2, padx=10, pady=2)
        btn_ok = CTkButton(self, text='OK', command=self.transf_esf)
        btn_ok.grid(row=2, column=1, pady=10)
    def transf_esf(self):
        f_axial = self.ent_axial.get()
        f_cort = self.ent_cort.get()
        mom_fle = self.ent_mom.get()
    

#abre janela materiais
def frm_materiais():
    frame_mat = CTkToplevel(Main)
    lbl_conc = CTkLabel(frame_mat, text='Características do concreto')
    lbl_conc.grid(row=0, column=0, columnspan=2)
    lbl_fck = CTkLabel(frame_mat, text='Fck (MPa)')
    lbl_fck.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
    ent_fck = CTkEntry(frame_mat, width=60, textvariable=str_conc)
    ent_fck.insert(1, fck)
    ent_fck.grid(row=2, column=0, padx=10, pady=2, columnspan=2)
    lbl_aco = CTkLabel(frame_mat, text='Características do aço da placa de base')
    lbl_aco.grid(row=3, column=0, columnspan=2)
    lbl_fy_pla = CTkLabel(frame_mat, text='Fy (MPa)')
    lbl_fy_pla.grid(row=4, column=0, padx=10, pady=5)
    ent_fy_pla = CTkEntry(frame_mat, width=60, textvariable=str_fy_pb)
    ent_fy_pla.insert(1, fy_pb)
    ent_fy_pla.grid(row=5, column=0, padx=10, pady=2)
    lbl_fu_pla = CTkLabel(frame_mat, text='Fu (MPa)')
    lbl_fu_pla.grid(row=4, column=1, padx=10, pady=5)
    ent_fu_pla = CTkEntry(frame_mat, width=60, textvariable=str_fu_pb)
    ent_fu_pla.insert(1, fu_pb)
    ent_fu_pla.grid(row=5, column=1, padx=10, pady=2)
    lbl_chumb = CTkLabel(frame_mat, text='Características do aço do chumbador')
    lbl_chumb.grid(row=6, column=0, columnspan=2)
    lbl_fy_chumb = CTkLabel(frame_mat, text='Fy (MPa)')
    lbl_fy_chumb.grid(row=7, column=0, padx=10, pady=5)
    ent_fy_chumb = CTkEntry(frame_mat, width=60, textvariable=str_fy_chumb)
    ent_fy_chumb.insert(1, fy_chumb)
    ent_fy_chumb.grid(row=8, column=0, padx=10, pady=2)
    lbl_fu_chumb = CTkLabel(frame_mat, text='Fu (MPa)')
    lbl_fu_chumb.grid(row=7, column=1, padx=10, pady=5)
    ent_fu_chumb = CTkEntry(frame_mat, width=60, textvariable= str_fu_chumb)
    ent_fu_chumb.insert(1, fu_chumb)
    ent_fu_chumb.grid(row=8, column=1, padx=10, pady=2)
 
app = Main()
app.mainloop()