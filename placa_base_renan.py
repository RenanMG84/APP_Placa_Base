import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

class Principal(tk.Tk):
     def __init__(self):
        super().__init__()
        self.title("Cálculo de placas de base - Ver. 1.0")
        self.geometry("+600+100")

        #Organização dos frames--------------------------------------
        #Frame Menu Lateral
        self.menu_lateral = Frame_Menu_Lateral(self)
        self.menu_lateral.grid(row=0, column= 0, sticky='n')
        #Frame Menu Lateral 2
        self.menu_lateral2 = Frame_Menu_Lateral2(self)
        self.menu_lateral2.grid(row=0, column= 1, sticky='n')
        #Frame Menu Lateral 3
        self.menu_lateral3 = Frame_Menu_Lateral3(self)
        self.menu_lateral3.grid(row=0, column= 2, sticky='n')
        #Frame resultados
        self.frm_result = Frame_Resultados(self)
        self.frm_result.grid(row=0, column = 3)
        #Frame Botões
        self.frm_botoes = Frame_Botoes(self)
        self.frm_botoes.grid(row=1, column = 1)
        #Frame Explicação
        self.frm_exp = Frame_Explicacao(self)
        self.frm_exp.grid(row = 2, column = 0, pady = 5, columnspan = 4, sticky = 'w')


class Frame_Menu_Lateral(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        #Variaveis globais
        self.check_var = IntVar()

        #Label Esforços
        lab_esf = tk.LabelFrame(self, text='Esforços')
        lab_esf.grid(row= 0, column= 0, padx = 5, sticky= 'n')
        label_for = tk.Label(lab_esf, text = "Força Axial", width= 15, anchor='w')
        label_for.grid(row = 1, column = 0, stick = 'w', padx = 15)
        entry_axi = ttk.Entry(lab_esf, width=8)
        entry_axi.grid(row = 1, column = 1, pady = 5)
        label_mm10 = tk.Label(lab_esf, text = 'kN')
        label_mm10.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        label_cor = tk.Label(lab_esf, text = "Força Cortante", width= 15, anchor='w')
        label_cor.grid(row = 2, column = 0, stick = 'w', padx = 15)
        entry_cor = ttk.Entry(lab_esf, width=8)
        entry_cor.grid(row = 2, column = 1, pady = 5)
        label_mm11 = tk.Label(lab_esf, text = 'kN')
        label_mm11.grid(row = 2, column = 2, padx = 10, sticky = 'w')
        label_mom = tk.Label(lab_esf, text = "Momento Fletor", width= 15, anchor='w')
        label_mom.grid(row = 3, column = 0, stick = 'w', padx = 15)
        entry_mom = ttk.Entry(lab_esf, width=8)
        entry_mom.grid(row = 3, column = 1, pady = (5, 10))
        label_mm12 = tk.Label(lab_esf, text = 'kN*m')
        label_mm12.grid(row = 3, column = 2, padx = 10)

        #Label materiais placa de base
        lab_aco_pb = tk.LabelFrame(self, text='Aço da placa de base')
        lab_aco_pb.grid(row= 1, column= 0, padx = 5, sticky= 'ewn')
        self.label_fy_pb = tk.Label(lab_aco_pb, text = "Fy",  anchor='w', width= 15)
        self.label_fy_pb.grid(row = 1, column = 0, padx = 15, sticky='w')
        self.entry_fy_pb = ttk.Entry(lab_aco_pb, width=8)
        self.entry_fy_pb.grid(row = 1, column = 1, pady = 5, sticky='ew')
        self.entry_fy_pb.insert(0,'250')
        self.label_mm15 = tk.Label(lab_aco_pb, text = 'MPa')
        self.label_mm15.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.label_fu_pb = tk.Label(lab_aco_pb, text = "Fu",anchor='w', width= 15)
        self.label_fu_pb.grid(row = 2, column = 0, padx = 15, sticky='w')
        self.entry_fu_pb = ttk.Entry(lab_aco_pb, width=8)
        self.entry_fu_pb.grid(row = 2, column = 1, pady = 5, sticky='ew')
        self.entry_fu_pb.insert(0,'400')
        self.label_mm15 = tk.Label(lab_aco_pb, text = 'MPa')
        self.label_mm15.grid(row = 2, column = 2, padx = 10, sticky = 'w')

        #Label materiais chumbador
        lab_aco_chumb = tk.LabelFrame(self, text='Aço dos chumbadores')
        lab_aco_chumb.grid(row= 2, column= 0, padx = 5, sticky= 'ewn')
        self.label_fy_pb = tk.Label(lab_aco_chumb, text = "Fy", anchor='w', width= 15)
        self.label_fy_pb.grid(row = 1, column = 0, padx = 15, sticky='w')
        self.entry_fy_pb = ttk.Entry(lab_aco_chumb, width=8)
        self.entry_fy_pb.grid(row = 1, column = 1, pady = 5, sticky='ew')
        self.entry_fy_pb.insert(0,'250')
        self.label_mm15 = tk.Label(lab_aco_chumb, text = 'MPa')
        self.label_mm15.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.label_fu_pb = tk.Label(lab_aco_chumb, text = "Fu", anchor='w', width= 15)
        self.label_fu_pb.grid(row = 2, column = 0, padx = 15, sticky='w')
        self.entry_fu_pb = ttk.Entry(lab_aco_chumb, width=8)
        self.entry_fu_pb.grid(row = 2, column = 1, pady = 5, sticky='ew')
        self.entry_fu_pb.insert(0,'400')
        self.label_mm15 = tk.Label(lab_aco_chumb, text = 'MPa')
        self.label_mm15.grid(row = 2, column = 2, padx = 10, sticky = 'w')

        #Label concreto
        lab_concreto = tk.LabelFrame(self, text='Concreto')
        lab_concreto.grid(row= 3, column= 0, padx = 5, sticky= 'ewn')
        self.label_fck = tk.Label(lab_concreto, text = "Fck", anchor='w', width= 15)
        self.label_fck.grid(row = 0, column = 0, stick = 'w', padx = 15)
        self.entry_fck = ttk.Entry(lab_concreto, width=8)
        self.entry_fck.grid(row = 0, column = 1, pady = 5)
        self.entry_fck.insert(0,'25')
        self.label_mm13 = tk.Label(lab_concreto, text = 'MPa')
        self.label_mm13.grid(row = 0, column = 2, padx = 10, sticky = 'w')
        self.label_a2 = tk.Label(lab_concreto, text = "Área da base\n de concreto", anchor='w', width= 15)
        self.label_a2.grid(row = 1, column = 0, stick = 'w', padx = 15)
        self.entry_a2concr = ttk.Entry(lab_concreto, width=8)
        self.entry_a2concr.grid(row = 1, column = 1, pady = 5)
        self.label_mm14 = tk.Label(lab_concreto, text = 'cm2')
        self.label_mm14.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.check1 = tk.Checkbutton(lab_concreto, text= 'Usar mesma área da placa base', variable= self.check_var, command= self.muda_status_botao_a2)
        self.check1.grid(row = 2, column = 0, columnspan = 3, pady = 10, padx = 10)

    def muda_status_botao_a2(self):
        if self.check_var.get() == 1: 
            self.entry_a2concr.configure(state = 'disabled')
            self.entry_a2concr.delete(0, 'end')
        else:
            self.entry_a2concr.configure(state = 'normal')
        



class Frame_Menu_Lateral2(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.radio_tipo_var = IntVar()


        #Label tipo de placa
        self.lab_tipo_placa = tk.LabelFrame(self, text='Vinculação da placa')
        self.lab_tipo_placa.grid(row= 0, column= 0, padx = 5, sticky= 'ew')
        self.rad_art = tk.Radiobutton(self.lab_tipo_placa, text= 'Articulada', command=self.tipo_vinculo, variable= self.radio_tipo_var, value=1)
        self.rad_art.grid(row = 0, column = 0)
        self.rad_eng = tk.Radiobutton(self.lab_tipo_placa, text= 'Engastada', command=self.tipo_vinculo, variable= self.radio_tipo_var, value=2)
        self.rad_eng.grid(row = 0, column = 1)
        self.rad_eng.select()

        #Label geometria placa engastada
        self.lab_pb_eng = tk.LabelFrame(self, text='Placa de base engastada')
        self.lab_pb_eng.grid(row= 1, column= 0, padx = 5, sticky= 'ew')
        #d
        self.label_d = tk.Label(self.lab_pb_eng, text = "d", width= 15, anchor='w')
        self.label_d.grid(row = 1, column = 0, stick = 'w', padx = 15)
        self.entry_d = ttk.Entry(self.lab_pb_eng, width=8)
        self.entry_d.grid(row = 1, column = 1, pady =5)
        self.label_mm1 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm1.grid(row = 1, column = 2, padx = 10)
        #bf
        self.label_bf = tk.Label(self.lab_pb_eng, text = 'bf', width= 15, anchor='w')  
        self.label_bf.grid(row = 2, column = 0,  stick = 'w', padx = 15)
        self.entry_bf = ttk.Entry(self.lab_pb_eng, width=8)
        self.entry_bf.grid(row = 2, column = 1, pady = 5)
        self.label_mm2 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm2.grid(row = 2, column = 2, padx = 10)
        #a1
        self.label_a1 = tk.Label(self.lab_pb_eng, text = 'a1', width= 15, anchor='w')  
        self.label_a1.grid(row = 3, column = 0,  stick = 'w', padx = 15)
        self.entry_a1 = ttk.Entry(self.lab_pb_eng, width=8)
        self.entry_a1.grid(row = 3, column = 1, pady = 5)
        self.label_mm2 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm2.grid(row = 3, column = 2, padx = 10)
        #a2
        self.label_a2 = tk.Label(self.lab_pb_eng, text = 'a2', width= 15, anchor='w')  
        self.label_a2.grid(row = 4, column = 0,  stick = 'w', padx = 15)
        self.entry_a2 = ttk.Entry(self.lab_pb_eng, width=8)
        self.entry_a2.grid(row = 4, column = 1, pady = 5)
        self.label_mm2 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm2.grid(row = 4, column = 2, padx = 10)
        #a3
        self.label_a3 = tk.Label(self.lab_pb_eng, text = 'a3', width= 15, anchor='w')  
        self.label_a3.grid(row = 5, column = 0,  stick = 'w', padx = 15)
        self.entry_a3 = ttk.Entry(self.lab_pb_eng, width=8)
        self.entry_a3.grid(row = 5, column = 1, pady = 5)
        self.label_mm2 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm2.grid(row = 5, column = 2, padx = 10)
        #e
        self.label_e = tk.Label(self.lab_pb_eng, text = 'e', width= 15, anchor='w')  
        self.label_e.grid(row = 6, column = 0,  stick = 'w', padx = 15)
        self.entry_e = ttk.Entry(self.lab_pb_eng, width=8)
        self.entry_e.grid(row = 6, column = 1, pady = 5)
        self.label_mm2 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm2.grid(row = 6, column = 2, padx = 10)
        #combobox
        self.label_d_chum = tk.Label(self.lab_pb_eng, text = "Diâmetro dos \nchumbadores", anchor='w', width=15)   
        self.label_d_chum.grid(row = 7, column = 0, stick = 'w', padx = 15)
        self.cbm_dia1 = ttk.Combobox(self.lab_pb_eng, values=['6,3', '8,0', '9,52', '12,7', '16,0', '19,1', '22,2', '25,4', '31,8', '41,3'], width = 5)
        self.cbm_dia1.grid(row = 7, column = 1, padx = 10, pady = 5)
        self.label_mm3 = tk.Label(self.lab_pb_eng, text = 'mm')
        self.label_mm3.grid(row = 7, column = 2, padx = 10)

        #Label geometria placa articulada
        self.lab_pb_art = tk.LabelFrame(self, text='Placa de base articulada')
        self.label_d = tk.Label(self.lab_pb_art, text = "d", width= 15, anchor='w')
        self.label_d.grid(row = 1, column = 0, stick = 'w', padx = 15)
        self.entry_d_art = ttk.Entry(self.lab_pb_art, width=8)
        self.entry_d_art.grid(row = 1, column = 1, pady =5)
        self.label_mm1 = tk.Label(self.lab_pb_art, text = 'mm')
        self.label_mm1.grid(row = 1, column = 2, padx = 10)
        self.label_bf = tk.Label(self.lab_pb_art, text = 'bf', width= 15, anchor='w')  
        self.label_bf.grid(row = 2, column = 0,  stick = 'w', padx = 15)
        self.entry_bf_art = ttk.Entry(self.lab_pb_art, width=8)
        self.entry_bf_art.grid(row = 2, column = 1, pady = 5)
        self.label_mm2 = tk.Label(self.lab_pb_art, text = 'mm')
        self.label_mm2.grid(row = 2, column = 2, padx = 10)
        self.label_d_chum = tk.Label(self.lab_pb_art, text = "Diâmetro dos \nchumbadores", anchor='w', width=15)   
        self.label_d_chum.grid(row = 3, column = 0, stick = 'w', padx = 15)
        self.cbm_dia1_art = ttk.Combobox(self.lab_pb_art, values=['6,3', '8,0', '9,52', '12,7', '16,0', '19,1', '22,2', '25,4', '31,8', '41,3'], width = 5)
        self.cbm_dia1_art.grid(row = 3, column = 1, padx = 10, pady = 5)
        self.label_mm3 = tk.Label(self.lab_pb_art, text = 'mm')
        self.label_mm3.grid(row = 3, column = 2, padx = 10)
        self.btn_ref = ttk.Button(self.lab_pb_art, text='Desenho de Referência')
        self.btn_ref.grid(row = 4, column= 0, stick = 'w', padx = 15, pady= 5 )


    
    def tipo_vinculo(self):
        if self.radio_tipo_var.get() == 1:
            self.lab_pb_art.grid(row= 1, column= 0, padx = 5, sticky= 'ew')
            self.lab_pb_eng.grid_forget()
        else:
            self.lab_pb_art.grid_forget()
            self.lab_pb_eng.grid(row= 1, column= 0, padx = 5, sticky= 'ew')


 
class Frame_Menu_Lateral3(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.radio_var_n1 = IntVar()
        self.radio_var_n2 = IntVar()
        #Label parâmetros chumbadores tracionados
        #n1
        lab_carac_chumb = tk.LabelFrame(self, text='Chumbadores tracionados')
        lab_carac_chumb.grid(row= 0, column= 0, padx = 5, sticky= 'ew')
        self.label_n1_pb = tk.Label(lab_carac_chumb, text=chr(951) + '1 - Rugosidade da barra', anchor='w', fg='blue')
        self.label_n1_pb.grid(row = 0, column = 1, pady = 5, stick = 'w')
        self.radio_n1_1 = tk.Radiobutton(lab_carac_chumb, text= 'Barras lisas (= 1,0)', command=self.n1, variable= self.radio_var_n1, value=1 )
        self.radio_n1_1.grid(row = 1, column = 1, pady = 5, stick = 'w')
        self.radio_n1_2 = tk.Radiobutton(lab_carac_chumb, text= 'Barras entalhadas (= 1,4)', command=self.n1, variable= self.radio_var_n1, value=2)
        self.radio_n1_2.grid(row = 2, column = 1, pady = 5, stick = 'w')
        self.radio_n1_3 = tk.Radiobutton(lab_carac_chumb, text= 'Barras nervuradas (= 2,25)', command=self.n1, variable= self.radio_var_n1, value=3)
        self.radio_n1_3.grid(row = 3, column = 1, pady = 5, stick = 'w')
        self.radio_n1_3.select()
        #n2
        self.label_n1_pb = tk.Label(lab_carac_chumb, text=chr(951) + '2 - Posição da barra na peça', anchor='w', fg='blue')
        self.label_n1_pb.grid(row = 4, column = 1, pady = 5, stick = 'w')
        self.radio_n1_1 = tk.Radiobutton(lab_carac_chumb, text= 'Boa aderência (= 1,0)', command=self.n2, variable= self.radio_var_n2, value=1 )
        self.radio_n1_1.grid(row = 5, column = 1, pady = 5, stick = 'w')
        self.radio_n1_2 = tk.Radiobutton(lab_carac_chumb, text= 'Má aderência (= 0,7)', command=self.n2, variable= self.radio_var_n2, value=2)
        self.radio_n1_2.grid(row = 6, column = 1, pady = 5, stick = 'w')
        self.radio_n1_1.select()

        #Label parâmetros chumbadores construtivos
        #n1
        self.lab_carac_chumb = tk.LabelFrame(self, text='Chumbadores construtivos')
        self.lab_carac_chumb.grid(row= 1, column= 0, padx = 5, sticky= 'ew')
        self.label_min = tk.Label(self.lab_carac_chumb, text = "Compr. mínimo", width= 15, anchor='w')
        self.label_min.grid(row = 2, column = 0, stick = 'w', padx = 15)
        self.entry_min = ttk.Entry(self.lab_carac_chumb , width=8)
        self.entry_min.grid(row = 2, column = 1, pady =5)
        self.label_mm1 = tk.Label(self.lab_carac_chumb , text = chr(966))
        self.label_mm1.grid(row = 2, column = 2, padx = 10)

        
    def n1(self):
        pass

    def n2(self):
        pass


class Frame_Explicacao(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        label_ex = tk.Label(self, text= 'Aqui vai a explicação do entry', anchor= 'w')
        label_ex.pack(padx = 5)
    

class Frame_Resultados(tk.Frame):
     def __init__(self, master = None,  frame_height=400, frame_width=400):
        super().__init__(master, height = frame_height, width=frame_width)
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents

        #TextBox
        txt_resul = tk.Text(self, height=350, width= 350)
        txt_resul.pack()

class Frame_Botoes(tk.Frame):
     def __init__(self, master = None):
        super().__init__(master)

def main():
    app = Principal()
    app.mainloop()

if __name__ == "__main__":
    main()
