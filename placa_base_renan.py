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
        #Menu Lateral
        self.menu_lateral = Frame_Menu_Lateral(self)
        self.menu_lateral.grid(row=0, column= 0)
        #Frame resultados
        self.frm_result = Frame_Resultados(self)
        self.frm_result.grid(row=0, column = 1)
        #Frame Botões
        self.frm_botoes = Frame_Botoes(self)
        self.frm_botoes.grid(row=1, column = 1)
        #Frame Explicação
        self.frm_exp = Frame_Explicacao(self)
        self.frm_exp.grid(row = 2, column = 0, pady = 5, columnspan = 2, sticky = 'w')


class Frame_Menu_Lateral(tk.Frame):
     def __init__(self, master = None):
        super().__init__(master)
        #Variaveis globais
        self.check_var = IntVar()
        self.radio_tipo_var = IntVar()
        self.radio_var_n1 = IntVar()
        self.radio_var_n2 = IntVar()

        def muda_status_botao_a2():
            pass

        def evento_radiobutton():
            pass

        def n1():
            pass

        def n2():
            pass

        #Label tipo de placa
        lab_tipo_placa = tk.LabelFrame(self, text='Vinculação da placa')
        lab_tipo_placa.grid(row= 0, column= 0, padx = 5, sticky= 'ew')
        rad_art = tk.Radiobutton(lab_tipo_placa, text= 'Articulada', command=evento_radiobutton, variable= self.radio_tipo_var, value=1)
        rad_art.grid(row = 0, column = 0)
        rad_eng = tk.Radiobutton(lab_tipo_placa, text= 'Engastada', command=evento_radiobutton, variable= self.radio_tipo_var, value=2)
        rad_eng.grid(row = 0, column = 1)
        rad_art.select()

        #Label geometria placa engastada

        #Label geometria placa articulada
        lab_pb_art = tk.LabelFrame(self, text='Placa de base articulada')
        lab_pb_art.grid(row= 1, column= 0, padx = 5, sticky= 'ew')

        self.label_d = tk.Label(lab_pb_art, text = "d", width= 15, anchor='w')
        self.label_d.grid(row = 1, column = 0, stick = 'w', padx = 15)
        
        self.entry_d = ttk.Entry(lab_pb_art, width=8)
        self.entry_d.grid(row = 1, column = 1, pady =5)

        self.label_mm1 = tk.Label(lab_pb_art, text = 'mm')
        self.label_mm1.grid(row = 1, column = 2, padx = 10)


        self.label_bf = tk.Label(lab_pb_art, text = 'bf', width= 15, anchor='w')  
        self.label_bf.grid(row = 2, column = 0,  stick = 'w', padx = 15)

        self.entry_bf = ttk.Entry(lab_pb_art, width=8)
        self.entry_bf.grid(row = 2, column = 1, pady = 5)

        self.label_mm2 = tk.Label(lab_pb_art, text = 'mm')
        self.label_mm2.grid(row = 2, column = 2, padx = 10)

        self.label_d_chum = tk.Label(lab_pb_art, text = "Diâmetro dos \nchumbadores", anchor='w', width=15)   
        self.label_d_chum.grid(row = 3, column = 0, stick = 'w', padx = 15)


        self.cbm_dia1 = ttk.Combobox(lab_pb_art, values=['6,3', '8,0', '9,52', '12,7', '16,0', '19,1', '22,2', '25,4', '31,8', '41,3'], width = 1)
        self.cbm_dia1.grid(row = 3, column = 1, padx = 10, pady = 5)

        self.label_mm3 = tk.Label(lab_pb_art, text = 'mm')
        self.label_mm3.grid(row = 3, column = 2, padx = 10)



        #Label Esforços
        lab_esf = tk.LabelFrame(self, text='Esforços')
        lab_esf.grid(row= 2, column= 0, padx = 5, sticky= 'ew')
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
        lab_aco_pb.grid(row= 3, column= 0, padx = 5, sticky= 'ew')
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
        lab_aco_chumb.grid(row= 4, column= 0, padx = 5, sticky= 'ew')
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
        lab_concreto.grid(row= 5, column= 0, padx = 5, sticky= 'ew')
        self.label_fck = tk.Label(lab_concreto, text = "Fck", anchor='w', width= 15)
        self.label_fck.grid(row = 0, column = 0, stick = 'w', padx = 15)
        self.entry_fck = ttk.Entry(lab_concreto, width=8)
        self.entry_fck.grid(row = 0, column = 1, pady = 5)
        self.entry_fck.insert(0,'25')
        self.label_mm13 = tk.Label(lab_concreto, text = 'MPa')
        self.label_mm13.grid(row = 0, column = 2, padx = 10, sticky = 'w')
        self.label_a2 = tk.Label(lab_concreto, text = "Área da base", anchor='w', width= 15)
        self.label_a2.grid(row = 1, column = 0, stick = 'w', padx = 15)
        self.entry_a2concr = ttk.Entry(lab_concreto, width=8)
        self.entry_a2concr.grid(row = 1, column = 1, pady = 5)
        self.label_mm14 = tk.Label(lab_concreto, text = 'cm2')
        self.label_mm14.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.check1 = tk.Checkbutton(lab_concreto, text= 'Usar mesma área da placa base', variable= self.check_var, command= muda_status_botao_a2)
        self.check1.grid(row = 2, column = 0, columnspan = 3, pady = 10, padx = 10)

        #Label parâmetros chumbadores tracionados
        #n1
        lab_carac_chumb = tk.LabelFrame(self, text='Chumbadores tracionados')
        lab_carac_chumb.grid(row= 6, column= 0, padx = 5, sticky= 'ew')
        self.label_n1_pb = tk.Label(lab_carac_chumb, text=chr(951) + '1 - Rugosidade da barra', anchor='w', fg='blue')
        self.label_n1_pb.grid(row = 0, column = 1, pady = 5, stick = 'w')
        self.radio_n1_1 = tk.Radiobutton(lab_carac_chumb, text= 'Barras lisas (= 1,0)', command=n1, variable= self.radio_var_n1, value=1 )
        self.radio_n1_1.grid(row = 1, column = 1, pady = 5, stick = 'w')
        self.radio_n1_2 = tk.Radiobutton(lab_carac_chumb, text= 'Barras entalhadas (= 1,4)', command=n1, variable= self.radio_var_n1, value=2)
        self.radio_n1_2.grid(row = 2, column = 1, pady = 5, stick = 'w')
        self.radio_n1_3 = tk.Radiobutton(lab_carac_chumb, text= 'Barras nervuradas (= 2,25)', command=n1, variable= self.radio_var_n1, value=3)
        self.radio_n1_3.grid(row = 3, column = 1, pady = 5, stick = 'w')
        self.radio_n1_3.select()
        #n2
        self.label_n1_pb = tk.Label(lab_carac_chumb, text=chr(951) + '2 - Posição da barra na peça', anchor='w', fg='blue')
        self.label_n1_pb.grid(row = 4, column = 1, pady = 5, stick = 'w')
        self.radio_n1_1 = tk.Radiobutton(lab_carac_chumb, text= 'Boa aderência (= 1,0)', command=n2, variable= self.radio_var_n2, value=1 )
        self.radio_n1_1.grid(row = 5, column = 1, pady = 5, stick = 'w')
        self.radio_n1_2 = tk.Radiobutton(lab_carac_chumb, text= 'Má aderência (= 0,7)', command=n2, variable= self.radio_var_n2, value=2)
        self.radio_n1_2.grid(row = 6, column = 1, pady = 5, stick = 'w')
        self.radio_n1_1.select()


 

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
