class Large_Exc():
    def __init__(self):
        pass

class Placa_Base():
    #Variáveis
    momento = 1
    axial = 1
    cortante = 1
    b = 1 #largura da placa
    l = 1 #comprimento da placa
    a2 = 1 #area do concreto
    fck = 1
    fy_pb = 1 #fy da placa de base
    fu_pb = 1 #fu da placa de base
    fy_chumb = 1 #fy do chumbador
    fu_chumb = 1 #fu do chumbador
    d_chumb = 1 #diâmetro do chumbador
    d_perfil = 1 #comprimento do perfil
    bf_perfil = 1 #mesa do perfil 

    #Funções----------------------------------------------------------------------------------------------------------------------
    def __init__(self, momento, axial, cortante, b, l, a2, fck, fy_pb, fu_pb, fy_chumb, fu_chumb, d_chumb, d_perfil, bf_perfil):
        self.momento = momento
        self.axial = axial
        self.cortante = cortante
        self.b = b
        self.l = l

    
    #verificar as dimensões da placa a1, a2, d , se batem com L
    def dim_min_placa(d_chumb, d_perfil, bf_perfil, b, l):
        a1 = 1.6 * d_chumb
        a2 = 1.6 * d_chumb
        l_min = 2 * a1 + 2 * a2 + d_perfil
        if l < l_min:
            l = l_min
        b_min = bf_perfil + 20 #em milímetros !!
        if b < b_min:
            b = b_min    
    
    def verifica_exc(mom, ax, l):
        exc = mom/ax
        ecri = l/3 #calcula excentricidade critica
        if exc >= ecri:
            return('large')
        else:
            return('small')

    #calcula placa com grande excentricidade
    def large(mom, ax, l, d_chumb, d_perfil, bf_perfil, b,):
        dim_min_placa(d_chumb, d_perfil, bf_perfil, b, l)
        print('')

    #calcula placa com pequena excentricidade
    def small():
        print('')

    #------------------------------------------------------------------------------------------------------------------------------------

    #Início do código
    

    excentricidade = verifica_exc(momento, axial , l )
    if excentricidade == 'large':
        large(momento, axial, l)
    else:
        small()



