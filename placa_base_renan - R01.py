import math

#Calculo de placas de base de acordo com Fakury

class Calc_Placa_Base():
    #entradas em kN, kNm e MPa
    def __init__(self, nsd, vsd, msd, fck, fy_pb, fu_pb, fy_chumb, fu_chumb, d_chumb, d, bf, tf, tw, num_chumb, a1, a2, hpb, bpb, hbl, bbl):
        self.nsd = nsd #kN
        self.vsd = vsd #kN
        self.msd = msd #kNm
        self.fck = fck #MPa
        self.fy_pb = fy_pb #MPa
        self.fu_pb = fu_pb #MPa
        self.fy_chumb = fy_chumb #MPa
        self.fu_chumb = fu_chumb #MPa
        self.d_chumb = d_chumb #mm
        self.d = d #mm
        self.bf = bf #mm
        self.tf = tf #mm
        self.tw = tw #mm
        self.res = 0 
        self.a1 = a1 #mm
        self.a2 = a2 #mm
        self.hpb = hpb #mm
        self.bpb = bpb #mm
        self.hbl = hbl #cm
        self.bbl = bbl #cm
        self.num_chumb = num_chumb #num total de chumbadores
        self.diam = [6.35, 8.0, 12.7, 15.9, 19.1, 22.2, 25.4, 31.8, 41.3, 44.5, 50.8] #diametros comerciais de chapas  

        def peq(hpb, e, nsd, bpb):
            y = hpb - 2 * e # cm
            sigmacsd = nsd / (y * bpb) #kN/cm2
            ftrd = 0 
            ftsd = 0 
            return  [y, sigmacsd, ftrd, ftsd]
        
        def grd(hpb, a1, a2, nsd, e, bpb, sigmacrd, d_chumb,num_chumb, fy_chumb, fu_chumb, fck, hbl, han,
                bbl):
            ht = (hpb / 2.0) - a1 #cm
            delta = math.pow((ht + (hpb / 2.0)), 2.0) - ((2 * nsd * ( e + ht)) / (bpb * sigmacrd)) #cm2
            if delta < 0:
                print("Delta menor que 0")
                return
            y = ht + (hpb /2.0) - math.sqrt(delta) #cm
            ftsd = sigmacrd * y * bpb - nsd # kN
            achumb = (math.pi * math.pow(d_chumb, 2.0)) / 4.0 #cm2
            #Escoamento da seção bruta dos chumbadores
            ftrdy = ((num_chumb / 2) * achumb * fy_chumb) / 1.10 #kN
            #Ruptura da parte roscada dos chumbadores
            ftrdu = ((num_chumb / 2) * 0.75 * achumb * fu_chumb) / 1.35 #kN
            #Arrancamento do chumbador
            ftrdac = (8 * (num_chumb / 2) *1.7 * achumb * fck) / 1.4 #kN
            #Ruptura do cone de concreto
            c1 = min(((hbl / 2.0) - ht), 1.5 * han)
            c2 = min(((bbl - bpb + 2 * a1) / 2.0), 1.5 * han)
            c3 = min(ht, 1.5 * han)
            c4 = min(a2, 3 * han)
            arc = 2* (c2 + (c4 / 2.0))*(c1 + c3) + ((num_chumb / 2.0) - 2.0) * c4 * (c1 + c3) #cm2
            ftrdrc = (0.08 * arc * math.sqrt(fck)) / (1.4 * math.pow(han, 1/3)) # kN
            ftrd = min(ftrdy, ftrdu, ftrdac, ftrdrc)
            #tensão solicitante no concreto
            sigmacsd = sigmacrd
            return [y, sigmacsd, ftrd, ftsd, ftrdy, ftrdu, ftrdac, ftrdrc]

       #DISPOSIÇÕES CONSTRUTIVAS
        #self.a1 = 2 * d_chumb #mm
        #self.a1 = math.ceil(self.a1 / 5.0) * 5.0 #arredonda a1 e aproxima para o próximo número múltiplo de 5
        
        #define o comprimento mínimo da Hpb da placa
        #self.hpb = self.d + 4 * self.a1 #mm
        #self.hpb = math.ceil(self.hpb / 5.0) * 5.0 #arredonda hpb e aproxima para o próximo número múltiplo de 5

        #define o comprimento mínimo da Bpb da placa
        #self.bpb = self.bf + 20 #mm
        #self.bpb = math.ceil(self.bpb / 5.0) * 5.0 #arredonda hpb e aproxima para o próximo número múltiplo de 5

        #self.a2 = (self.bpb - 2*self.a1) /  ((num_chumb / 2) - 1) #mm

        self.a3 = self.hpb - 2 * self.a1 #mm

        #PROFUNDIDADE MÍNIMA DE ANCORAGEM
        self.han = 12*d_chumb #mm
        self.han = math.ceil(self.han / 5.0) * 5.0 #arredonda hpb e aproxima para o próximo número múltiplo de 5

        #DIMENSÕES MÍNIMAS DO BLOCO DE FNDAÇÃO
        #Dimensão Hbl
        #self.hbl = self.hpb + 11* self.d_chumb #mm
        #self.hbl = math.ceil(self.hbl / 5.0) * 5.0
        #Dimensão Bbl
        #self.bbl = self.bpb + 11* self.d_chumb #mm
        #self.bbl = math.ceil(self.bbl / 5.0) * 5.0
        #altura do bloco "Zbl"
        self.zbl = 0 #mm
        if self.hbl >= self.han + 200:
            self.zbl = self.hbl
        else:
            self.zbl = self.han + 200

        #Conversão de unidades para os cálculos abaixo
        self.fck = self.fck / 10 #kN/cm2
        self.fy_pb = self.fy_pb / 10 #kN/cm2
        self.fu_pb = self.fu_pb / 10 #kN/cm2
        self.fy_chumb = self.fy_chumb / 10 #kN/cm2
        self.fu_chumb = self.fu_chumb / 10 #kN/cm2
        self.msd = self.msd * 100 #kN*cm
        self.hpb = self.hpb / 10 #cm
        self.bpb = self.bpb / 10 #cm
        self.a1 = self.a1 / 10 #cm
        self.a2 = self.a2 / 10 #cm
        self.han = self.han /10 #cm
        self.d_chumb = self.d_chumb / 10 #cm
        self.d = self.d /10 #cm
        self.bf = self.bf / 10 #cm

        #TENSÃO RESISTENTE DO CONCRETO
        self.sigmacrd = self.fck / ( 1.4 * 1.4) #kN/cm2

        #EXCENTRICIDADE DA PLACA
        self.e = (self.msd / self.nsd) #cm
        self.ecrit = 0.5 * (self.hpb - (self.nsd / (self.bpb * self.sigmacrd))) #cm
     
        #calcula os parâmetros para pequenas ou grandes excentricidades
        if self.e <= self.ecrit:
            self.res = peq(self.hpb, self.e, self.nsd, self.bpb)
        else:
            self.res = grd(self.hpb, self.a1, self.a2, self.nsd, self.e, self.bpb, self.sigmacrd, self.d_chumb,self.num_chumb, 
                           self.fy_chumb, self.fu_chumb, self.fck, self.hbl, self.han, self.bbl)

        if self.e <= self.ecrit:
            self.y = self.res[0] #cm
            self.sigmacsd = self.res[1] #kN/cm2
            self.ftrd = self.res[2] #kN
            self.ftsd = self.res[3] #kN
        else:
            self.y = self.res[0] #cm
            self.sigmacsd = self.res[1] #kN/cm2
            self.ftrd = self.res[2] #kN
            self.ftsd = self.res[3] #kN
            self.ftrdy = self.res[4] #kN
            self.ftrdu = self.res[5] #kN
            self.ftrdac = self.res[6] #kN
            self.ftrdrc = self.res[7] #kN

        #VERIFICAÇÕES NA PLACA DE BASE
        #Momento fletor provocado pela compressão no concreto
        self.m1 = (self.hpb - 0.95 * self.d) / 2.0 #cm
        self.m2 = (self.bpb - 0.8 * self.bf) / 2.0 #cm
        self.m3 = math.sqrt(self.d * self.bf) / 4.0 #cm
        self.m = max(self.m1, self.m2, self.m3) #cm
        if self.y < self.m1:
            self.m = math.sqrt(2 * self.y * self.m1 - math.pow(self.y, 2.0)) #cm
        self.mpbcsd = self.sigmacsd * math.pow(self.m, 2.0) / 2.0 #kN
        #Momento fletor provocado pela tração nos chumbadores
        self.pi = min((num_chumb / 2.0) * (2 * self.a1 + self.d_chumb), self.bpb) #cm
        self.mpbtsd = self.ftsd * self.a1 /self.pi #kN
        #Momento fletor solicitante final
        self.msdch = max(self.mpbcsd, self.mpbtsd) #kN
        #Espessura mínima da placa
        self.tpb = math.sqrt((self.msdch * 4 * 1.10) / self.fy_pb)  #cm
        self.tpb = self.tpb * 10.0 #mm
        if self.tpb <= 6.35:
            self.tpb = 6.35
        elif self.tpb > 6.35 and self.tpb <= 8.00:
            self.tpb = 8.00
        elif self.tpb > 8.00 and self.tpb <= 9.52:
            self.tpb = 9.52
        elif self.tpb > 9.52 and self.tpb <= 12.7:
            self.tpb = 12.7
        elif self.tpb > 12.7 and self.tpb <= 15.9:
            self.tpb = 15.9
        elif self.tpb > 15.9 and self.tpb <= 19.1:
            self.tpb = 19.1
        elif self.tpb > 19.1 and self.tpb <= 22.2:
            self.tpb = 22.2
        elif self.tpb > 22.2 and self.tpb <= 25.4:
            self.tpb = 25.4
        elif self.tpb > 25.4 and self.tpb <= 31.8:
            self.tpb = 31.8
        elif self.tpb > 31.8 and self.tpb <= 41.3:
            self.tpb = 41.3      
        elif self.tpb > 41.3 and self.tpb <= 44.5:
            self.tpb = 44.5
        elif self.tpb > 44.5 and self.tpb <= 50.8:
            self.tpb = 50.8
        elif self.tpb > 50.8 and self.tpb <= 57.2:
            self.tpb = 57.2
        else:
            self.tpb = 999999
        #Momento fletor resistente da placa de base
        self.tpb = self.tpb / 10.0 #cm
        self.mpbrd = (math.pow(self.tpb, 2.0) * self.fy_pb ) / (4 * 1.10) #kN
        
        #VERIFICAÇÃO DA FORÇA CORTANTE NOS CHUMBADORES
        self.achumb = (math.pi * math.pow(self.d_chumb, 2.0)) / 4.0 #cm2
        #Força cortante resistente do fuste do chumbador
        self.fvrdi = (0.4 * self.achumb * self.fu_chumb) / 1.35
        self.alpha = (1.18 * self.tpb * self.fu_chumb) / (self.d_chumb * self.fy_chumb)
        #Força cortante resistente do bloco
        self.vchrd1 = 5 * math.pow(d_chumb, 2.0) * self.sigmacrd * num_chumb #kN
        #Força cortante resistente para chumbadores tracionados
        self.vchrdi1 = (0.8 / (1 + math.pow(self.alpha, 2.0))) * (math.sqrt((1 + math.pow(self.alpha, 2.0))* (math.pow(self.fvrdi, 2.0)) - math.pow((0.533* self.ftsd / (num_chumb /2.0)), 2.0) ) - self.alpha * ((0.533* self.ftsd) / (self.num_chumb / 2.0))) #kN
        #Força cortante resistente para chumbadores comprimidos
        self.vchrdi2 = (0.8 / (1 + math.pow(self.alpha, 2.0))) * (math.sqrt((1 + math.pow(self.alpha, 2.0))* (math.pow(self.fvrdi, 2.0)))) #kN
        #Força cortante total
        self.vchtot = (self.num_chumb / 2.0) * self.vchrdi1 + (self.num_chumb / 2.0) * self.vchrdi2 #kN
        #Força cortante resistente final
        self.vchrd = min(self.vchtot, self.vchrd1)

        #RESULTADOS
        '''
        print("Disposições construtivas:")
        print(f"A1: {(self.a1 * 10):.0f} mm")
        print(f"A2: {(self.a2):.0f} mm")
        print(f"Comprimento Hpb: {self.hpb * 10:.0f} mm")
        print(f"Comprimento Bpb: {self.bpb* 10:.0f} mm")
        print("")
        print(f"Excentricidade da placa: {self.e:.2f} cm")
        print(f"Excentricidade crítica: {self.ecrit:.2f} cm")
        print(f"Comprimento de ancoragem: {self.han:.2f} cm")
        print(f"Dimensão Hbl do bloco: {self.hbl:.2f} cm")
        print(f"Dimensão Bbl do bloco: {self.bbl:.2f} cm")
        print(f"Altura do bloco: {self.zbl:.2f} cm")
        print(f"Tensão resiste no concreto: {self.sigmacrd:.2f} kN/cm2")
        print(f"Tensão solicitante no concreto: {self.sigmacsd:.2f} kN/cm2")
        print(f"Momento fletor resistente da placa: {self.mpbrd:.2f} kN*cm/cm")
        print(f"Momento fletor solicitante na placa: {self.msdch:.2f} kN*cm/cm")
        print(f"Espessura da placa: {(self.tpb * 10):.2f} mm")
        print(f"Força cortante resistente do chumbador: {self.vchrd:.2f} kN")
        print(f"Força cortante solicitante no chumbador: {self.vsd:.2f} kN")
        print(f"Força de tração solicitante no chumbador: {self.ftsd:.2f} kN")
        print(f"Força de tração resistente dos chumbador: {self.ftrd:.2f} kN")
        if self.e > self.ecrit:
            print(f"Escoamento da seção bruta dos chumbadores:  {self.ftrdy:.2f} kN")
            print(f"Ruptura da parte roscada dos chumbadores:  {self.ftrdu:.2f} kN")
            print(f"Arrancamento do chumbador:  {self.ftrdac:.2f} kN")
            print(f"Ruptura do cone de concreto:  {self.ftrdrc:.2f} kN")
        '''

        if self.vsd > self.vchrd:
            print("NÃO PASSOU NA VERIFICAÇÃO A CORTANTE")
        if self.ftsd > self.ftrd:
            print("NÃO PASSOU NA VERIFICAÇÃO A TRAÇÃO")
        if self.msdch > self.mpbrd:
            print("NÃO PASSOU NA VERIFICAÇÃO A MOMENTO")
        if self.sigmacsd > self.sigmacrd:
            print("NÃO PASSOU NA VERIFICAÇÃO A TENSÃO NO CONCRETO")

                #nsd, vsd, msd, fck, fy_pb, fu_pb, fy_chumb, fu_chumb, d_chumb, d, bf, tf, tw, num_chumb
#Calc_Placa_Base(25, 15, 30, 20, 250, 400, 250, 400, 19.1, 152, 152, 10, 5.8, 4)


# Initialize an empty list to store the numbers from each line
comb_list = []

# Open the file in read mode
with open('comb.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line into a list of numbers (assuming numbers are separated by spaces)
        numbers = [float(num) for num in line.split()]
        
        # Append the list of numbers to the main list
        comb_list.append(numbers)

# Print the list of lists containing the numbers from each line
print(comb_list[0][5])

# Initialize a variable to store the maximum number
max_vsd = None
max_msd = None
num_interations = 0
espessura = 1 

        
for numbers in comb_list:
    nsd = numbers[2]
    num_interations += 1

    # Get the first two numbers from the list
    first_number = numbers[0]
    second_number = numbers[1]
    
    # Compare the first two numbers
    if first_number > second_number:
        max_vsd = first_number
    else:
        max_vsd = second_number
    
 
    fourth_number, fifth_number = numbers[3], numbers[4]
        
        # Compare the fourth and fifth numbers
    if fourth_number > fifth_number:
        max_msd = fourth_number
    else:
        max_msd = fifth_number

    print(f'Combinação: {num_interations:.2f}')

    d_chumb = 25.4 #mm
    d = 203 #mm
    bf = 203 #mm
    tf = 10.70 #mm
    tw = 10.50 #mm
    num_chumb = 4
    a1 = 55 #mm
    a2 = 106 #mm
    hpb = 430 #mm
    bpb = 250 #mm
    hbl = 100 #cm
    bbl = 100 #cm

    Calcular_pb = Calc_Placa_Base(nsd, max_vsd, max_msd, 20, 250, 400, 250, 400, d_chumb, d, bf, tf, tw, num_chumb, a1, a2, hpb, bpb, hbl, bbl)
                                    #nsd, vsd, msd, fck, fy_pb, fu_pb, fy_chumb, fu_chumb, d_chumb, d, bf, tf, tw, num_chumb, a1, a2, hpb, bpb, hbl, bbl
    if Calcular_pb.tpb > espessura:
        espessura = Calcular_pb.tpb 

print(espessura)    