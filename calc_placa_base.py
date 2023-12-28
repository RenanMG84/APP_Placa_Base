import math


#unidades = sempre usar kN e cm para cálculo! Converter as unidades apenas na apresentação dos resultados
class Calc_Placa_Base_Souza():
    def __init__(self, momento, axial, cortante, b, l, a2_conc, fck, fy_pb, fu_pb, fy_chumb, fu_chumb, d_chumb, d, bf, tf, vinculo_pb):
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
        self.tf = tf
        self.vinculo_pb = vinculo_pb   

    #FUNÇÕES--------------------------------------------------------------------------------------     

    #Calcula placa de base rotulada
    def calc_pb_rot(self):
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
       
    #Calcula placa base engastada - Pede a função específica para cada tipo 
    def calc_pb_eng(self):
        pass

    #calcula placa com pequena excentricidade
    def pb_eng_peq():
        pass

    #calcula placa com media excentricidade
    def pb_eng_med(mom, ax, l, d_chumb, d_perfil, bf_perfil, b,):
        pass
    #calcula placa com grande excentricidade
    def pb_eng_gra(mom, ax, l, d_chumb, d_perfil, bf_perfil, b,):
        pass

    #calcula chumbador p/ placa de base articulada
    def chumb_art():
        pass

    #calcula chumbador p/ placa de base engastada
    def chumb_eng():
        pass
"""""
    #chama a função "rotulado" ou "engastado"
    if self.vinculo_pb == "rotulado":
        calc_pb_rot()
    else:
        calc_pb_eng() """

placa = Calc_Placa_Base_Souza(0.0, 705, 100, 0, 0, 720, 2, 25, 40, 25, 40, 1.25, 25, 17, 1.25, "rotulado")
placa.calc_pb_rot()





    

    

    