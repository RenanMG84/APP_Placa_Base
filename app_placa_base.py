from tkinter import *
import tkinter as tk
from customtkinter import *
import customtkinter
import math
from PIL import Image
from tkinter import ttk
 
class Principal(tk.Tk):
     def __init__(self):
        super().__init__()
        self.title("Cálculo de Placa de Base - Ver. 1.0")
        self.geometry("+600+100")

        #Organização dos frames--------------------------------------
        #Menu superior
        self.menu_sup = Criar_Menu(self)
        #Frame de botões abaixo do menu
        self.frm_botoes = Frame_Botoes(self)
        self.frm_botoes.grid(row = 0, column = 0, columnspan= 2, padx= 5)
        #Frame de desenho da placa de base
        self.frm_desenho = Frame_Desenho_PB(self)
        self.frm_desenho.grid(row=1, column=0, columnspan= 2, pady  =2)
        #Frame resultados
        self.frm_result = Frame_Resultados(self)
        self.frm_result.grid(row=2, column = 0, sticky= 'nswe', padx = (5,0), pady = 2)
        #Frame esforços
        self.frm_esforcos = Frame_Esforcos(self)
        self.frm_esforcos.grid(row=2, column = 1, sticky= 'nswe', padx = (0, 5),pady = 2)
        
class Frame_Desenho_PB(CTkFrame):
     def __init__(self, master = None, frame_height=300, frame_width=600,  frame_border_width = 2):
        super().__init__(master, height = frame_height, width=frame_width, border_width= frame_border_width)
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents
        quadro = tk.Canvas(self, width=550, height=300)
        quadro.pack(padx = 5, pady = 10)
        

class Frame_Resultados(CTkFrame):    
     def __init__(self, master = None,  frame_height=400, frame_width=400, frame_border_width = 2):
        super().__init__(master, height = frame_height, width=frame_width, border_width= frame_border_width)
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents
        self.columnconfigure(0,weight= 1)
        self.columnconfigure(1,weight= 1)
        self.criando_widgets()
    
     def criando_widgets(self):
        self.radio_var = IntVar()

        #Label
        label1 = CTkLabel(self, text = "RESULTADOS", text_color='blue')
        label1.grid(row = 0, column = 0, pady = 2, columnspan = 2)

        #Radiobutton
        rad1 = tk.Radiobutton(self, text= 'Simplificado', command=self.evento_radiobutton, variable= self.radio_var, value=1)
        rad1.grid(row = 1, column = 0)
        rad2 = tk.Radiobutton(self, text= 'Completo', command=self.evento_radiobutton, variable= self.radio_var, value=2)
        rad2.grid(row = 1, column = 1)
        rad1.select()

        #TextBox
        txt_resul = CTkTextbox(self, height=350, width= 350)
        txt_resul.grid( row = 2, column = 0, columnspan = 2, pady = 5)

     def evento_radiobutton():
         pass

class Frame_Esforcos(CTkFrame):
     def __init__(self, master = None,  frame_height=400, frame_width=200, frame_border_width = 2):
        super().__init__(master, height = frame_height, width=frame_width, border_width= frame_border_width)
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents
        label1 = CTkLabel(self, text = "ESFORÇOS", text_color='blue')
        label1.pack(pady = 2)

class Frame_Botoes(tk.Frame):
     def __init__(self, master = None):
        super().__init__(master)
        btn_esf = CTkButton(self, text="Esforços", command= self.abrir_esf)
        btn_esf.pack(side = LEFT, padx = 5)
        btn_mat = CTkButton(self, text="Materiais", command = self.abrir_materiais)
        btn_mat.pack(side = LEFT, padx = 5)
        btn_geo = CTkButton(self, text="Geometria", command= self.abrir_geometria)
        btn_geo.pack(side = LEFT, padx = 5)
        btn_calc = CTkButton(self, text="Calcular", command= self.calcular)
        btn_calc.pack(side = LEFT, padx = 5)

     def abrir_esf(self):
         frame_esf = Menu_Esforcos_Tab(self)

     def abrir_materiais(self):
         frame_esf = Menu_Materiais(self)

     def abrir_geometria(self):
         frame_esf = Menu_Geometria(self)  
    
     def calcular(self):
         pass

class Menu_Esforcos(tk.Toplevel):
     def __init__(self, master = None):
        super().__init__(master)
        self.title("")
        self.geometry('250x200+700+300')
        Frame1 = CTkFrame(self, width = 200, border_width= 2)
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

class Menu_Esforcos_Tab(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        #FRAME 1
        self.frame1 = Frame(self)
        self.frame1.grid(row = 0, column= 0)
        self.btn_add = CTkButton(self.frame1, text = "Adicionar", command= self.adicionar)
        self.btn_add.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.btn_rem = CTkButton(self.frame1, text= 'Apagar', command= self.apagar)
        self.btn_rem.grid(row = 0, column = 1, padx = 20, pady = 10)

        #FRAME 2
        #labels
        self.frame2 = Frame(self)
        self.frame2.grid(row = 1, column= 0)
        self.label = CTkLabel(self.frame2, text= 'Combinação a ser inserida')
        self.label.grid(row = 1, column = 0)
        self.label68 = CTkLabel(self.frame2, text= 'Unid.: (kN) e (kN*m)')
        self.label68.grid(row = 2, column = 0)

        #FRAME 3
        self.frame3 = Frame(self)
        self.frame3.grid(row=2, column= 0, columnspan= 3 )
        self.label1 = CTkLabel(self.frame3, text = 'Nsd')
        self.label2 = CTkLabel(self.frame3, text = 'Vsd')
        self.label3 = CTkLabel(self.frame3, text = 'Msd')
        #grids
        self.label1.grid(row = 0, column = 0)
        self.label2.grid(row = 0, column = 1)
        self.label3.grid(row = 0, column = 2)
        #entrys
        self.ent_nsd = CTkEntry(self.frame3, width = 70)
        self.ent_vsd = CTkEntry(self.frame3, width = 70)
        self.ent_msd = CTkEntry(self.frame3, width = 70)
        #grids
        self.ent_nsd.grid(row = 1, column = 0)
        self.ent_vsd.grid(row = 1, column = 1)
        self.ent_msd.grid(row = 1, column = 2)
        
        #FRAME 4
        self.frame4 = Frame(self)
        self.frame4.grid(row=3, column= 0)
        #Treeview
        self.tree_comb = ttk.Treeview(self.frame4, columns=('1', '2', '3'), show = 'headings')
        self.tree_comb.column('1', width=70)
        self.tree_comb.column('2', width=70) 
        self.tree_comb.column('3', width=70)
        self.tree_comb.heading('1', text= 'Nsd')
        self.tree_comb.heading('2', text= 'Vsd')
        self.tree_comb.heading('3', text= 'Msd')
        self.tree_comb.pack(pady = 10)

        #FRAME 5
        self.frame5 = Frame(self)
        self.frame5.grid(row=4, column= 0)
        self.btn_ok = CTkButton(self.frame5, text = "OK")
        self.btn_ok.pack(pady = 10)


    
    def apagar(self):
       selected_item = self.tree_comb.selection()[0]
       self.tree_comb.delete(selected_item)

    def adicionar(self):
       nsd = self.ent_nsd.get()
       vsd = self.ent_vsd.get()
       msd = self.ent_msd.get()
       self.tree_comb.insert('', 'end', values= (nsd, vsd, msd))
 
       
        
  



class Menu_Materiais(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.check_var = tk.IntVar()
        self.criando_widgets()

    def criando_widgets(self):
        #Label concreto
        self.label_concreto = tk.LabelFrame(self, text='Concreto')
        self.label_concreto.grid(row = 0 , column= 0, padx = 10, pady = 5 )
        self.label_for = CTkLabel(self.label_concreto, text = "Fck")
        self.label_for.grid(row = 0, column = 0, stick = 'e', padx = 5)
        self.entry_fck = CTkEntry(self.label_concreto, width=60)
        self.entry_fck.grid(row = 0, column = 1, pady = 5)
        self.entry_fck.insert(0,'25')
        self.label_mm13 = CTkLabel(self.label_concreto, text = 'MPa')
        self.label_mm13.grid(row = 0, column = 2, padx = 10, sticky = 'w')
        self.label_a2 = CTkLabel(self.label_concreto, text = "Área da base")
        self.label_a2.grid(row = 1, column = 0, stick = 'e', padx = 5)
        self.entry_a2concr = CTkEntry(self.label_concreto, width=60)
        self.entry_a2concr.grid(row = 1, column = 1, pady = 5)
        self.label_mm14 = CTkLabel(self.label_concreto, text = 'cm2')
        self.label_mm14.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.check1 = tk.Checkbutton(self.label_concreto, text= 'Usar mesma área da placa base', variable= self.check_var, command= self.muda_status_botao_a2)
        self.check1.grid(row = 2, column = 0, columnspan = 3, pady = 10, padx = 10)
        
        #Label Aço PB
        self.label_aco_pb = tk.LabelFrame(self, text='Aço da placa de base')
        self.label_aco_pb.grid( row = 1, column= 0 , sticky= 'nsew', padx = 10, pady = 5)
        self.label_fy_pb = CTkLabel(self.label_aco_pb, text = "Fy")
        self.label_fy_pb.grid(row = 1, column = 0, padx = 5)
        self.entry_fy_pb = CTkEntry(self.label_aco_pb, width=40)
        self.entry_fy_pb.grid(row = 1, column = 1, pady = 5)
        self.entry_fy_pb.insert(0,'250')
        self.label_mm15 = CTkLabel(self.label_aco_pb, text = 'MPa')
        self.label_mm15.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.label_fu_pb = CTkLabel(self.label_aco_pb, text = "Fu")
        self.label_fu_pb.grid(row = 2, column = 0, padx = 5)
        self.entry_fu_pb = CTkEntry(self.label_aco_pb, width=40)
        self.entry_fu_pb.grid(row = 2, column = 1, pady = (5,10))
        self.entry_fu_pb.insert(0,'400')
        self.label_mm15 = CTkLabel(self.label_aco_pb, text = 'MPa')
        self.label_mm15.grid(row = 2, column = 2, padx = 10, sticky = 'w')

        #Label Aço Chumbador
        self.label_aco_chumb = tk.LabelFrame(self, text='Aço do chumbador')
        self.label_aco_chumb.grid( row = 2, column= 0 , sticky= 'nsew', padx = 10, pady = 5)
        self.label_fy_chumb = CTkLabel(self.label_aco_chumb, text = "Fy")
        self.label_fy_chumb.grid(row = 1, column = 0, stick = 'e', padx = 5)
        self.entry_fy_chumb = CTkEntry(self.label_aco_chumb, width=40)
        self.entry_fy_chumb.grid(row = 1, column = 1, pady = 5)
        self.entry_fy_chumb.insert(0,'250')
        self.label_mm15 = CTkLabel(self.label_aco_chumb, text = 'MPa')
        self.label_mm15.grid(row = 1, column = 2, padx = 10, sticky = 'w')
        self.label_fu_chumb = CTkLabel(self.label_aco_chumb, text = "Fu")
        self.label_fu_chumb.grid(row = 2, column = 0, stick = 'e', padx = 5)
        self.entry_fu_chumb = CTkEntry(self.label_aco_chumb, width=40)
        self.entry_fu_chumb.grid(row = 2, column = 1, pady = (5,10))
        self.entry_fu_chumb.insert(0,'400')
        self.label_mm15 = CTkLabel(self.label_aco_chumb, text = 'MPa')
        self.label_mm15.grid(row = 2, column = 2, padx = 10, sticky = 'w')
        self.label_mm16 = CTkLabel(self.label_aco_chumb, text = 'Diâmetro')
        self.label_mm16.grid(row = 3, column = 0,  padx = (5,0), sticky = 'e')

    def muda_status_botao_a2(self):
        if self.check_var.get() == 1: 
            self.entry_a2concr.configure(state = 'disabled', fg_color = 'gray')
            self.entry_a2concr.delete(0, 'end')
        else:
            self.entry_a2concr.configure(state = 'normal', fg_color = 'white')

class Menu_Criterios(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.radio_var_n1 = IntVar()
        self.radio_var_n2 = IntVar()
        self.title('Comprimento de ancoragem dos chumbadores')
        self.criando_widgets()
    
    def n1(self):
        pass

    def n2(self):
        pass

    def criando_widgets(self):
        #LabelFrame - n1
        self.label_n1 = tk.LabelFrame(self, text=chr(951) + '1 - Rugosidade da barra')
        self.label_n1.grid(row = 1, column= 0, padx = 10, pady = 5, sticky= 'nsew')
        #labels
        self.label_tit1 = CTkLabel(self, text= 'Comprimento de ancoragem dos chumbadores', text_color='blue', padx = 10)
        #widgets
        self.radio_n1_1 = tk.Radiobutton(self.label_n1, text= 'Barras lisas (= 1,0)', command=self.n1, variable= self.radio_var_n1, value=1 )
        self.radio_n1_2 = tk.Radiobutton(self.label_n1, text= 'Barras entalhadas (= 1,4)', command=self.n1, variable= self.radio_var_n1, value=2)
        self.radio_n1_3 = tk.Radiobutton(self.label_n1, text= 'Barras nervuradas (= 2,25)', command=self.n1, variable= self.radio_var_n1, value=3)
        self.radio_n1_3.select()
        #grids
        self.label_tit1.grid(row = 0 , column = 0, columnspan = 2) 
        self.radio_n1_1.grid(row = 1 , column= 0, sticky= 'w')
        self.radio_n1_2.grid(row = 2 , column= 0, sticky= 'w')
        self.radio_n1_3.grid(row = 3 , column= 0, sticky= 'w')

        #LabelFrame - n2
        self.label_n2 = tk.LabelFrame(self, text=chr(951) + '2 - Posição da barra na peça')
        self.label_n2.grid(row = 2, column= 0, padx = 10, pady = 5, sticky= 'nsew')
        #labels
        self.label_tit2 = CTkLabel(self, text= 'Comprimento de ancoragem dos chumbadores ', text_color='blue', padx = 10)
        #widgets
        self.radio_n2_1 = tk.Radiobutton(self.label_n2, text= 'Boa aderência (= 1,0)', command=self.n2, variable= self.radio_var_n2, value=1 )
        self.radio_n2_2 = tk.Radiobutton(self.label_n2, text= 'Má aderência (= 0,7)', command=self.n2, variable= self.radio_var_n2, value=2)
        self.radio_n2_2.select()
        #grids
        self.label_tit2.grid(row = 0 , column = 0, columnspan = 2) 
        self.radio_n2_1.grid(row = 1 , column= 0, sticky= 'w')
        self.radio_n2_2.grid(row = 2 , column= 0, sticky= 'w') 

class Menu_Geometria(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.vinculo_placa = IntVar()
        self.criando_widgets()
        self.title("Parâmetros da placa de base")
        self.grab_set()

    def alterna_frames(self):
        #Alterna entre os frames 2 e 3
        if self.vinculo_placa.get() == 2:
            self.frame3.grid(row= 2 , column= 0, sticky= 'nsew')
            self.frame2.grid_forget()
            self.my_image = customtkinter.CTkImage(light_image = Image.open("placa_eng.png"), size=(400, 400))
            self.image_label = CTkLabel(self.frame4, image= self.my_image, text='')  # display image with a CTkLabel
            self.image_label.grid(row = 6, column = 0, columnspan = 6, padx = 10, pady = (0,10))

        else:
            self.frame2.grid(row= 1 , column= 0, sticky= 'nsew')
            self.frame3.grid_forget()    
            self.my_image = customtkinter.CTkImage(light_image = Image.open("placa_art.png"), size=(400, 400))
            self.image_label = CTkLabel(self.frame4, image= self.my_image, text='')  # display image with a CTkLabel
            self.image_label.grid(row = 6, column = 0, columnspan = 6, padx = 10, pady = (0,10))

    def criando_widgets(self):
        #Frame 1 - Label Vínculo PB
        self.frame1 = tk.Frame(self)
        self.frame1.grid(row= 0 , column= 0, sticky= 'nsew')
        self.label_tip_pb1 = tk.LabelFrame(self.frame1, text='Vínculo da placa de base')
        self.label_tip_pb1.grid(row=0, column= 0 )
        self.rad_art = tk.Radiobutton(self.label_tip_pb1, text = 'Articulado', variable= self.vinculo_placa,command = self.alterna_frames, value = 1)
        self.rad_art.grid(row = 1, column = 0 )
        self.rad_eng = tk.Radiobutton(self.label_tip_pb1, text = 'Engastado', variable= self.vinculo_placa, command = self.alterna_frames, value = 2)
        self.rad_eng.grid(row = 1, column = 1 )
        self.rad_eng.select()

        #Frame 2 - Parâmetros para desenho da PB articulada
        self.frame2 = tk.Frame(self)
        #self.frame2.grid(row= 1 , column= 0)
        self.label_tip_pb2 = tk.LabelFrame(self.frame2, text='Placa de base articulada')
        self.label_tip_pb2.grid(row=0, column= 0, sticky= 'nsew')
        #Labels
        self.label_d = CTkLabel(self.label_tip_pb2, text = "d")
        self.label_mm1 = CTkLabel(self.label_tip_pb2, text = 'mm')
        self.label_mm2 = CTkLabel(self.label_tip_pb2, text = 'mm')
        self.label_mm3 = CTkLabel(self.label_tip_pb2, text = 'mm')
        self.label_mm4 = CTkLabel(self.label_tip_pb2, text = 'mm')
        self.label_l = CTkLabel(self.label_tip_pb2, text = 'L')
        self.label_b = CTkLabel(self.label_tip_pb2, text = 'B')
        self.label_bf = CTkLabel(self.label_tip_pb2, text = 'bf')
        self.label_n_chum = CTkLabel(self.label_tip_pb2, text = "Qtd. Chumbadores")     
        self.label_d_chum = CTkLabel(self.label_tip_pb2, text = "Diâmetro")     
        #Widgets
        self.entry_d = CTkEntry(self.label_tip_pb2, width=40)
        self.entry_l = CTkEntry(self.label_tip_pb2, width=40)
        self.entry_b = CTkEntry(self.label_tip_pb2, width=40)
        self.entry_bf = CTkEntry(self.label_tip_pb2, width=40)
        self.cbm_qtd_chum_art = CTkComboBox(self.label_tip_pb2, values=['2'], width = 70, state='readonly')
        self.cbm_qtd_chum_art.set('2')
        self.check_area = tk.Checkbutton(self.label_tip_pb2, text='Calcular área da placa otimizada')
        self.cbm_dia1 = CTkComboBox(self.label_tip_pb2, values=['6,3', '8,0', '9,52', '12,7', '16,0', '19,1', '22,2', '25,4', '31,8', '41,3'], width = 70)
        #Grids
        self.label_l.grid(row = 0, column = 0 , stick = 'e', padx = 10)
        self.entry_l.grid(row = 0, column = 1, pady = 5)
        self.label_b.grid(row = 0, column = 3 , stick = 'e', padx = 10)
        self.label_bf.grid(row = 1, column = 3 , stick = 'e', padx = 10)
        self.entry_b.grid(row = 0, column = 4, pady = 5)
        self.entry_bf.grid(row = 1, column = 4, pady = 5)
        self.label_d.grid(row = 1, column = 0, stick = 'e', padx = 10)
        self.entry_d.grid(row = 1, column = 1, pady = (5, 10))
        self.label_mm1.grid(row = 1, column = 2, padx = 10)
        self.label_mm2.grid(row = 0, column = 2, padx = 10)
        self.label_mm3.grid(row = 0, column = 5, padx = 10)
        self.label_mm4.grid(row = 1, column = 5, padx = 10)
        self.label_n_chum.grid(row = 2, column = 0, stick = 'e', columnspan = 3, padx = 10, pady = 4)
        self.label_d_chum.grid(row = 3, column = 0, stick = 'e', columnspan = 3, padx = 10, pady = 4)
        self.cbm_qtd_chum_art.grid(row = 2, column = 3, columnspan = 2)
        self.cbm_dia1.grid(row = 3, column = 3, columnspan = 2)
        self.check_area.grid(row= 4, column = 0, columnspan= 5)


        #Frame 3 - Parâmetros para desenho da PB engastada
        self.frame3 = tk.Frame(self)
        self.frame3.grid(row= 2 , column= 0, sticky= 'nsew')
        self.label_tip_pb3 = tk.LabelFrame(self.frame3, text='Placa de base engastada')
        self.label_tip_pb3.grid(row=0, column= 0 )
        #Labels
        self.label_a1 = CTkLabel(self.label_tip_pb3, text = "a1")
        self.label_mm1 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_mm2 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_mm3 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_mm4 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_mm5 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_mm6 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_mm7 = CTkLabel(self.label_tip_pb3, text = 'mm')
        self.label_a2 = CTkLabel(self.label_tip_pb3, text = 'a2')
        self.label_a3 = CTkLabel(self.label_tip_pb3, text = 'a3')
        self.label_bf = CTkLabel(self.label_tip_pb3, text = 'bf')
        self.label_d = CTkLabel(self.label_tip_pb3, text = 'd')
        self.label_e = CTkLabel(self.label_tip_pb3, text = 'E')
        self.label_n_chum = CTkLabel(self.label_tip_pb3, text = "Qtd. Chumbadores")
        self.label_d_chum = CTkLabel(self.label_tip_pb3, text = "Diâmetro") 
        #Widgets
        self.entry_a1 = CTkEntry(self.label_tip_pb3, width=40)
        self.entry_a2 = CTkEntry(self.label_tip_pb3, width=40)
        self.entry_a3 = CTkEntry(self.label_tip_pb3, width=40)
        self.entry_e = CTkEntry(self.label_tip_pb3, width=40)
        self.entry_bf = CTkEntry(self.label_tip_pb3, width=40)
        self.entry_d = CTkEntry(self.label_tip_pb3, width=40)
        self.cbm_qtd_chum_art = CTkComboBox(self.label_tip_pb3, values=['4','6','8','10','12'], width = 70, state='readonly')
        self.cbm_qtd_chum_art.set('4')
        self.cbm_dia2 = CTkComboBox(self.label_tip_pb3, values=['6,3', '8,0', '9,52', '12,7', '16,0', '19,1', '22,2', '25,4', '31,8', '41,3'], width = 70)
        #Grids
        self.label_a1.grid(row = 0, column = 0 , stick = 'e', padx = 10)
        self.entry_a1.grid(row = 0, column = 1, pady = 5)
        self.label_a2.grid(row = 0, column = 3 , stick = 'e', padx = 10)
        self.label_e.grid(row = 1, column = 3 , stick = 'e', padx = 10)
        self.label_bf.grid(row = 2, column = 3 , stick = 'e', padx = 10)
        self.label_d.grid(row = 2, column = 0 , stick = 'e', padx = 10)
        self.entry_bf.grid(row = 2, column = 4, pady = 5)
        self.entry_d.grid(row = 2, column = 1, pady = 5)
        self.entry_a2.grid(row = 0, column = 4, pady = 5)
        self.entry_e.grid(row = 1, column = 4, pady = 5)
        self.label_a3.grid(row = 1, column = 0, stick = 'e', padx = 10)
        self.entry_a3.grid(row = 1, column = 1, pady = (5, 10))
        self.label_mm1.grid(row = 1, column = 2, padx = 10)
        self.label_mm2.grid(row = 0, column = 2, padx = 10)
        self.label_mm3.grid(row = 0, column = 5, padx = 10)
        self.label_mm4.grid(row = 1, column = 5, padx = 10)
        self.label_mm5.grid(row = 2, column = 5, padx = 10)
        self.label_mm6.grid(row = 2, column = 5, padx = 10)
        self.label_mm7.grid(row = 2, column = 2, padx = 10)
        self.label_n_chum.grid(row = 4, column = 0, stick = 'e', columnspan = 3, padx = 10)
        self.cbm_qtd_chum_art.grid(row = 4, column = 3, columnspan = 2)
        self.cbm_dia2.grid(row = 5, column = 3, columnspan = 2)
        self.label_d_chum.grid(row = 5, column = 0, stick = 'e', columnspan = 3, padx = 10, pady = 4)

        #Frame 4 - Desenhando PB
        self.frame4 = tk.Frame(self)
        self.frame4.grid(row=3, column=0)
        self.my_image = customtkinter.CTkImage(light_image = Image.open("placa_eng.png"), size=(400, 400))
        self.image_label = CTkLabel(self.frame4, image= self.my_image, text='')  # display image with a CTkLabel
        self.image_label.grid(row = 6, column = 0, columnspan = 6, padx = 10, pady = (0,10))

    def vinculo_pb(self):
        pass

class Menu_Sobre(tk.Toplevel):
     def __init__(self, master = None):
        super().__init__(master)
        self.title("Sobre")
        label_1 = CTkLabel(self, text="Aqui vai o texto de criação do app")
        label_1.pack()

#Classe utilizada para criação do menu superior
class Criar_Menu:
    def __init__(self, root):
        self.root = root
        #cria o menu
        self.menubar = tk.Menu(self.root)
        #Arquivo
        self.arquivo = tk.Menu(self.menubar, tearoff=0)
        self.arquivo.add_command(label="Abrir", command= self.abrir_menu)
        self.arquivo.add_command(label="Salvar", command = self.salvar_menu)
        self.arquivo.add_command(label="Sair", command= self.sair_menu)
        self.menubar.add_cascade(label="Arquivo", menu= self.arquivo)
        self.root.config(menu= self.menubar)
        #Editar
        self.editar = tk.Menu(self.menubar, tearoff=0)
        self.editar.add_command(label= 'Critérios', command = self.menu_criterios)
        self.editar.add_command(label = 'Exportar memorial')
        self.menubar.add_cascade(label = "Editar", menu = self.editar)
        self.root.config(menu = self.menubar)
        #Sobre
        self.sobre = tk.Menu(self.menubar, tearoff=0)
        self.sobre.add_command(label = 'Sobre', command= self.sobre_menu)
        self.menubar.add_cascade(label = "Sobre", menu = self.sobre)
        self.root.config(menu = self.menubar)

    def abrir_menu(self):
        filedialog.askopenfilename(
            initialdir="/",
            title="Abrir arquivo",
            filetypes=( "Todos os arquivos", "*.*"))

    def salvar_menu(self):
        pass

    def menu_criterios(self):
        abre_menu_criterio = Menu_Criterios()

    def sobre_menu(self):
        abre_menu_sobre = Menu_Sobre()

    def sair_menu(self):
        self.root.destroy()

class Calc_Placa_Base_Souza():
    def __init__(self, momento, axial, cortante, b, l, a2_conc, fck, fy_pb, fu_pb, \
                 fy_chumb, fu_chumb, d_chumb, d, bf, vinculo_pb, a1_pb, qtd_chumb, \
                    neta1, neta2, neta3, alpha):
        self.momento = momento
        self.axial = axial
        self.cortante = cortante
        self.b = b
        self.l = l 
        self.a2_conc = a2_conc
        self.fck= fck
        self.fy_pb = fy_pb
        self.fu_pb = fu_pb
        self.fy_chumb = fy_chumb
        self.fu_chumb = fu_chumb
        self.d_chumb = d_chumb
        self.d = d
        self.bf = bf
        self.qtd_chumb = qtd_chumb
        self.vinculo_pb = vinculo_pb 
        self.a1_pb = a1_pb
        self.neta1 = neta1
        self.neta2 = neta2
        self.neta3 = neta3
        self.alpha = alpha
        self.diam = [0.635, 0.8, 1.27, 1.59, 1.91, 2.22, 2.54, 3.18, 4.13, 4.45] #diametros comerciais de chapas  

    #Define se a placa é rotulada ou engastada
    def define_art_eng(self):
        if self.vinculo_pb == "rotulado":
            self.pb_rot()
        else:
            self.define_pb_eng()
       
    #Define o tipo de calculo para placas engastadas
    def define_pb_eng(self):
         #calcula excentricidade da placa
        exc = self.momento / self.axial
        print(exc)
        if exc <= (self.l / 6.0):
            self.pb_eng_peq()
        elif ((self.l / 6.0) < exc) and (exc <= (self.l / 3.0)):
            self.pb_eng_med()
        elif (exc > (self.l / 3.0)):
            self.pb_eng_gra()

    #Calcula placa de base rotulada
    def pb_rot(self):
        print("rotulado")
        c = 0 #balanço interno da placa
        #determinação da área da placa de base
        a11 = (1.0 / self.a2_conc) * math.pow((self.axial / (0.5 * self.fck)), 2.0)
        a12 = self.axial / self.fck
        a13 = self.d * self.bf
        a1 = max(a11, a12, a13)
        
        #altura (H) da placa de base
        self.h = (math.sqrt(a1)) + 0.5 * (0.95 * self.d - 0.8 * self.bf)
        
        #largura B da placa de base
        self.b = a1 / self.h
        
        #arredonda os valor obtidos em h e b
        self.h = round(self.h)
        self.b = round(self.b)
        if self.h % 2.0 != 0:
            self.h = self.h + 1.0
        if self.b % 2.0 != 0:
            self.b = self.b + 1.0

        #Balanço interno C da placa
        #determinação de Ah
        ah1 = self.axial / (0.5*self.fck* math.sqrt((self.a2_conc / (self.bf * self.d))))
        ah2 = self.axial / self.fck
        ah = max(ah1, ah2)

        aux1 = math.pow((self.d + self.bf - self.tf), 2.0)
        aux2 = 4 * (ah - self.bf * self.tf)
        if aux1 <= aux2 :
            c = 0
        else:
            c = 0.25 *(self.d + self.bf - self.tf - math.sqrt(math.pow((self.d + self.bf - self.tf), 2.0) - 4.0 * (ah - self.bf*self.tf)))
        
        #Espessura da placa de base
        m = (self.h - 0.95*self.d) / 2.0
        n = (self.b - 0.8 * self.bf) / 2.0
        t1 = m * math.sqrt((2.2 * self.axial) / (self.fy_pb * self.b * self.h))
        t2 = n * math.sqrt((2.2 * self.axial) / (self.fy_pb * self.b * self.h))
        t3 = c * math.sqrt((2.2 *self.axial) / (self.fy_pb * ah))
        t = max(t1, t2, t3)
        for i in self.diam:
            if i > t:
                t = i
                break
       
    #calcula placa com pequena excentricidade
    def pb_eng_peq(self):
        print("pequena excentricidade")
        ver1 = "" #variável utilizada para verificar a condição de resistência do concreto
        a1 = self.b * self.l
        c = self.l / 2.0
        i = (self.b * math.pow((self.l), 3.0)) / 12.0
        #tensão solicitante no concreto
        fpd = (self.axial / (self.l * self.b)) + ((self.momento * c) / i)
        #tensão resistente no concreto
        sigcrd = (self.fck / (1.4*1.4))* math.sqrt((self.a2_conc/ a1))

        if fpd <= sigcrd:
            ver1 = "OK"
        else:
            ver1 = "FALHOU - Verificar a tensão máxima no concreto"

        #Espessura da placa de base
        m = (self.l - 0.95*self.d) / 2.0
        n = (self.b - 0.8 * self.bf) / 2.0
        aux = max(m, n)
        mmax = (fpd * math.pow(aux, 2.0)) / 2.0
        t = math.sqrt((4.4*mmax) / self.fy_pb)         
        for i in self.diam:
            if i > t:
                t = i
                break

        
    #calcula placa com media excentricidade
    def pb_eng_med(self):
        print("media excentricidade")
        ver1 = "" #variável utilizada para verificar a condição de resistência do concreto
        exc = self.momento / self.axial
        a1 = self.b * self.l
        y = 3*((self.l / 2.0) - exc)
        #tensão solicitante no concreto
        fpd = (2 * self.axial) / (y * self.b)
        #tensão resistente no concreto
        sigcrd = (self.fck / (1.4*1.4))* math.sqrt((self.a2_conc/ a1))

        if fpd <= sigcrd:
            ver1 = "OK"
        else:
            ver1 = "FALHOU - Verificar a tensão máxima no concreto"

        #Espessura da placa de base
        m = (self.l - 0.95*self.d) / 2.0
        n = (self.b - 0.8 * self.bf) / 2.0
        aux = max(m, n)
        mmax = (fpd * math.pow(aux, 2.0)) / 2.0
        t = math.sqrt((4.4*mmax) / self.fy_pb)
        for i in self.diam:
            if i > t:
                t = i
                break



    #calcula placa com grande excentricidade
    def pb_eng_gra(self):
        print("grande excentricidade")
        y = 0 
        a1 = self.b * self.l
        #tensão resistente no concreto
        fpd = (self.fck / (1.4*1.4))* math.sqrt((self.a2_conc/ a1))
        g = (self.l / 2.0) - self.a1_pb
        hlinha = self.l - self.a1_pb
        flinha = (fpd * self.b * hlinha) / 2.0
        y1 = (flinha + math.sqrt(math.pow(flinha, 2.0) - 4*((fpd*self.b)/6.0)*(self.axial*g + self.momento))) / ((fpd * self.b) / 3.0)
        y2 = (flinha - math.sqrt(math.pow(flinha, 2.0) - 4*((fpd*self.b)/6.0)*(self.axial*g + self.momento))) / ((fpd * self.b) / 3.0)

        if (y1 > 0) and (y1 <= self.b):
            y = y1
        else:
            y = y2

        #Espessura da placa de base
        m = (self.l - 0.95*self.d) / 2.0
        n = (self.b - 0.8 * self.bf) / 2.0
        aux = max(m, n)
        mmax = (fpd * math.pow(aux, 2.0)) / 2.0
        t = math.sqrt((4.4*mmax) / self.fy_pb)
        for i in self.diam:
            if i > t:
                t = i
                break
        
        self.chumb_eng(y, fpd)
         

    #calcula chumbador p/ placa de base articulada
    def chumb_art(self):
        print("chumbador articulado")
        #area necessária dos chumbadores
        acsnec = (1.35 * self.cortante) / (0.4 * self.fu_chumb)
        #area de um chumbador
        acs = (math.pi*math.pow(self.d_chumb, 2.0)) / 4.0
        #qtd mínima de chumbadores
        qtd_min_chumb = acsnec / acs
        #comprimento mínimo do chumbador
        l_chumb = 12 * self.d_chumb

    #calcula chumbador p/ placa de base engastada
    def chumb_eng(self, y, fpd):
        print("chumbador engastado")
        ver = ""
        self.y = y
        self.fpd = fpd

        #TRAÇÃO---------------------------------------
        #força de tração nos chumbadores
        t = ((fpd * self.b * y) / 2.0 ) - self.axial
        #area de um chumbador
        acs = (math.pi*math.pow(self.d_chumb, 2.0)) / 4.0
        #num de chumbadores do lado tracionado
        nt = self.qtd_chumb / 2.0
        #força de tração em um chumbador
        t_chumb = t / nt #kN
        #tensão em cada chumbador
        ft_chumb = t_chumb / acs #kN/cm2
        #tensão limite para os chumbadores
        ftu_lim_chumb = 0.56 * self.fu_chumb

        
        #CISALHAMENTO-------------------------------
        #força cortante em cada chumbador
        v_chumb = self.cortante / self.qtd_chumb
        #tensão em cada chumbador
        fv_chumb = v_chumb / acs
        #tensão limite em cada chumbador
        fvu_lim_chumb = 0.3 * self.fu_chumb

        
        #INTERÇÃO ENTRE OS ESFORÇOS -------------------
        itr = math.pow((ft_chumb / ftu_lim_chumb), 2.0) + math.pow((fv_chumb / fvu_lim_chumb), 2.0)

        if itr <= 1.0:
            ver = "OK"
        else:
            ver = "Chumbador não atende!"

        #COMPRIMENTO DE ANCORAGEM DO CHUMBADOR --------
        self.fck = self.fck * 10 #convertendo de kN/cm2 para MPA
        self.fy_chumb = self.fy_chumb * 10
        fctm = 0.3 * math.pow(self.fck, 0.6667)
        fctkinf = 0.7* fctm
        fctd = fctkinf / 1.4
        fbd = self.neta1 * self.neta2 * self.neta3 * fctd
        lb = ((self.d_chumb * self.fy_chumb) / 1.1) / (4 * fbd) #cm
        lbmin = 40 * self.d_chumb

        if lb < lbmin:
            lb = lbmin

        #ancoragem necessaria
        lbnec = self.alpha * lb



def main():
    app = Principal()
    app.mainloop()

if __name__ == "__main__":
    main()