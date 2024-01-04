from tkinter import *
import tkinter as tk
from customtkinter import *
import math
 
class Principal(tk.Tk):
     def __init__(self):
        super().__init__()
        self.title("Cálculo de Placa de Base - Ver. 1.0")
        #self.geometry("800x860+250+100")

        #Organização dos frames--------------------------------------
        #Menu superior
        self.menu_sup = Criar_Menu(self)
        #Frame de botões abaixo do menu
        self.frm_botoes = Frame_Botoes(self)
        self.frm_botoes.grid(row = 0, column = 0, columnspan= 2)
        #Frame de desenho da placa de base
        self.frm_desenho = Frame_Desenho_PB(self)
        self.frm_desenho.grid(row=1, column=0, columnspan= 2)
        #Frame resultados
        self.frm_result = Frame_Resultados(self)
        self.frm_result.grid(row=2, column = 0)
        #Frame esforços
        self.frm_esforcos = Frame_Esforcos(self)
        self.frm_esforcos.grid(row=2, column = 1)
        
class Frame_Desenho_PB(tk.Frame):
     def __init__(self, master = None, frame_height=300, frame_width=600):
        super().__init__(master, height = frame_height, width=frame_width, bg="lightblue")
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents
        label1 = CTkLabel(self, text = "FRAME DESENHO")
        label1.pack()
        

class Frame_Resultados(tk.Frame):    
     def __init__(self, master = None,  frame_height=400, frame_width=300):
        super().__init__(master, height = frame_height, width=frame_width)
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents
        self.criando_widgets()
    
     def criando_widgets(self):
        self.radio_var = IntVar()

        #Label
        label1 = CTkLabel(self, text = "RESULTADOS", text_color='blue')
        label1.grid(row = 0, column = 0, columnspan = 2)

        #Radiobutton
        rad1 = tk.Radiobutton(self, text= 'Simplificado', command=self.evento_radiobutton, variable= self.radio_var, value=1)
        rad1.grid(row = 1, column = 0 )
        rad2 = tk.Radiobutton(self, text= 'Completo', command=self.evento_radiobutton, variable= self.radio_var, value=2)
        rad2.grid(row = 1, column = 1)
        rad1.select()

        #TextBox
        txt_resul = CTkTextbox(self, height=380, width= 270)
        txt_resul.grid( row = 2, column = 0, columnspan = 2)

     def evento_radiobutton():
         pass

class Frame_Esforcos(tk.Frame):
     def __init__(self, master = None,  frame_height=400, frame_width=300):
        super().__init__(master, height = frame_height, width=frame_width, bg="lightgreen")
        self.pack_propagate(False)  # Prevent frame from adjusting to its contents
        label1 = CTkLabel(self, text = "FRAME ESFORÇOS")
        label1.pack()

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
         frame_esf = Menu_Esforcos(self)

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

class Menu_Materiais(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)

class Menu_Geometria(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)

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
          self.editar.add_command(label= 'Chumbadores')
          self.editar.add_command(label = 'Critérios')
          self.menubar.add_cascade(label = "Editar", menu = self.editar)
          self.root.config(menu = self.menubar)
          #Utilitários
          self.uti = tk.Menu(self.menubar, tearoff=0)
          self.uti.add_command(label = "Exportar Memorial")
          self.menubar.add_cascade(label = "Utilitários", menu =self.uti)
          self.root.config(menu = self.menubar)
          #Sobre
          self.sobre = tk.Menu(self.menubar, tearoff=0)
          self.menubar.add_cascade(label = "Sobre", menu = self.sobre)
          self.root.config(menu = self.menubar)

     def abrir_menu(self):
          filedialog.askopenfilename(
               initialdir="/",
               title="Abrir arquivo",
               filetypes=( "Todos os arquivos", "*.*"))

     def salvar_menu(self):
          pass

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