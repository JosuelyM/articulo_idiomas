from pylab import *
from scipy.stats import norm
from scipy import integrate

ruta1 = "/home/josue/Proyecto/DI_1740-2009-10K/Metodo_1/Articulo/DiversityK/Conjuntos/"
ruta2 = "/home/josue/Proyecto/DI_1740-2009-10K/Metodo_1/Articulo/DiversityK/Conjuntos/datos_sigmoide/"

etiqueta = '_a.npy'

#orden idiomas
I1 = "EN"
I2 = "FR"
I3 = "GE"
I4 = "IT"
I5 = "SP"

#etiquetas
et_ab = I1 +"-"+ I2
et_ac = I1 +"-"+ I3
et_ad = I1 +"-"+ I4
et_ae = I1 +"-"+ I5

#funciones
def my_r2(obs, esp):
    mu = mean(obs)
    a = 0
    b = 0
    for k in range(0,len(obs)):
        a += (obs[k]-esp[k])**2
        b += (obs[k]-mu)**2
    r2 = 1- (a/b)
    return round(r2,2)

def sigmoide_ms(diversidad, mu, sigma):
    K = arange(0,len(diversidad))+1
    val = []
    def fsig(x):
        c = 1 /(sigma*sqrt(2*pi)) 
        y = exp( (-(x-mu)**2) / (2* sigma**2) ) 
        return y*c
    for i in range(0,len(K)):
        k = K[i]
        if log10(k) == 0:
            b = log10(2)/2
        elif log10(k) >0:
            b = log10(k)
        res = integrate.quad(fsig, -inf, b)
        val.append(res[0])
    return K, val

def busca_ms(DK):
    MU = linspace(0.1, 3, 20)
    SG = linspace(0.1, 3, 20)
    OP = []
    for i in range(0,len(MU)):
        mu1 = MU[i]
        for j in range(0,len(SG)):
            sg1 = SG[j]
            sigmoide = sigmoide_ms(DK, mu1, sg1)
            r2 = my_r2(DK, sigmoide[1])
            op = [r2, mu1, sg1]
            OP.append(op)
    Medio = max(OP)
    mu2 = round(Medio[1],3)
    sg2 = round(Medio[2],3)
    MU2 = linspace(mu2-0.2, mu2+0.2, 75)
    SG2 = linspace(sg2-0.2, sg2+0.2, 75)
    OP2 = []
    for i in range(0,len(MU2)):
        mu1 = MU2[i]
        for j in range(0,len(SG2)):
            sg1 = SG2[j]
            sigmoide = sigmoide_ms(DK, mu1, sg1)
            r2 = my_r2(DK, sigmoide[1])
            op2 = [r2, mu1, sg1]
            OP2.append(op2)
    Medio2 = max(OP2)
    return round(Medio2[1],4), round(Medio2[2],4), round(Medio2[0],4)

#Conjuntos
DM_ab = load(ruta1 + 'DM_ab' + etiqueta ).tolist()
DM_ac = load(ruta1 + 'DM_ac' + etiqueta ).tolist()
DM_ad = load(ruta1 + 'DM_ad' + etiqueta ).tolist()
DM_ae = load(ruta1 + 'DM_ae' + etiqueta ).tolist()

#Aplicar
MS_ab = busca_ms(DM_ab)
MS_ac = busca_ms(DM_ac)
MS_ad = busca_ms(DM_ad)
MS_ae = busca_ms(DM_ae)

M1 = [et_ab, MS_ab[0], MS_ab[1], MS_ab[2]]
M2 = [et_ac, MS_ac[0], MS_ac[1], MS_ac[2]]
M3 = [et_ad, MS_ad[0], MS_ad[1], MS_ad[2]]
M4 = [et_ae, MS_ae[0], MS_ae[1], MS_ae[2]]

DSG = [M1, M2, M3, M4]
savetxt(ruta2 + 'DSG_'+I1, DSG, fmt="%s")