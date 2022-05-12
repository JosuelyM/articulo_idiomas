from pylab import *

ruta1 = "Datos/"
ruta2 = "Figuras/"

e1 = "EN"
e2 = "FR"
e3 = "GE"
e4 = "IT"
e5 = "SP"

e_ab_a = e1 + '-' + e2
e_ac_a = e1 + '-' + e3
e_ad_a = e1 + '-' + e4
e_ae_a = e1 + '-' + e5

e_ab_b = e2 + '-' + e1
e_ac_b = e2 + '-' + e3
e_ad_b = e2 + '-' + e4
e_ae_b = e2 + '-' + e5

e_ab_c = e3 + '-' + e1
e_ac_c = e3 + '-' + e2
e_ad_c = e3 + '-' + e4
e_ae_c = e3 + '-' + e5

e_ab_d = e4 + '-' + e1
e_ac_d = e4 + '-' + e2
e_ad_d = e4 + '-' + e3
e_ae_d = e4 + '-' + e5

e_ab_e = e5 + '-' + e1
e_ac_e = e5 + '-' + e2
e_ad_e = e5 + '-' + e3
e_ae_e = e5 + '-' + e4

C1_EN = [0, 0.52, 0.67]
C2_EN = [0.470, 0.733, 0.807]

C1_FR = [1, 0.46, 0]
C2_FR = [1, 0.8, 0.36]

C1_GE = [0.53, 0, 0.7]
C2_GE = [0.541, 0.541, 0.717]

C1_IT = [0.19, 0.51, 0.02]
C2_IT = [0.384, 0.662, 0.239]

C1_SP = [0.64, 0, 0]
C2_SP = [1, 0.160, 0.160]

### Carga de Datos ####

#Ley de Zipf para los idiomas
ZL_A = loadtxt(ruta1 +'ZL_A', dtype=float)
ZL_B = loadtxt(ruta1 +'ZL_B', dtype=float)
ZL_C = loadtxt(ruta1 +'ZL_C', dtype=float)
ZL_D = loadtxt(ruta1 +'ZL_D', dtype=float)
ZL_E = loadtxt(ruta1 +'ZL_E', dtype=float)

#Ubicacion de las palabras migrantes dentro del idioma receptor
ZLM_ab_a = loadtxt(ruta1 +'ZLM_ab_a', dtype=float)
ZLM_ac_a = loadtxt(ruta1 +'ZLM_ac_a', dtype=float)
ZLM_ad_a = loadtxt(ruta1 +'ZLM_ad_a', dtype=float)
ZLM_ae_a = loadtxt(ruta1 +'ZLM_ae_a', dtype=float)
ZLM_ab_b = loadtxt(ruta1 +'ZLM_ab_b', dtype=float)
ZLM_ac_b = loadtxt(ruta1 +'ZLM_ac_b', dtype=float)
ZLM_ad_b = loadtxt(ruta1 +'ZLM_ad_b', dtype=float)
ZLM_ae_b = loadtxt(ruta1 +'ZLM_ae_b', dtype=float)
ZLM_ab_c = loadtxt(ruta1 +'ZLM_ab_c', dtype=float)
ZLM_ac_c = loadtxt(ruta1 +'ZLM_ac_c', dtype=float)
ZLM_ad_c = loadtxt(ruta1 +'ZLM_ad_c', dtype=float)
ZLM_ae_c = loadtxt(ruta1 +'ZLM_ae_c', dtype=float)
ZLM_ab_d = loadtxt(ruta1 +'ZLM_ab_d', dtype=float)
ZLM_ac_d = loadtxt(ruta1 +'ZLM_ac_d', dtype=float)
ZLM_ad_d = loadtxt(ruta1 +'ZLM_ad_d', dtype=float)
ZLM_ae_d = loadtxt(ruta1 +'ZLM_ae_d', dtype=float)
ZLM_ab_e = loadtxt(ruta1 +'ZLM_ab_e', dtype=float)
ZLM_ac_e = loadtxt(ruta1 +'ZLM_ac_e', dtype=float)
ZLM_ad_e = loadtxt(ruta1 +'ZLM_ad_e', dtype=float)
ZLM_ae_e = loadtxt(ruta1 +'ZLM_ae_e', dtype=float)

#Ley de Zipf para cada pareja de idiomas origen-receptor
ZM_ab_a = loadtxt(ruta1 +'ZM_ab_a', dtype=float)
ZM_ac_a = loadtxt(ruta1 +'ZM_ac_a', dtype=float)
ZM_ad_a = loadtxt(ruta1 +'ZM_ad_a', dtype=float)
ZM_ae_a = loadtxt(ruta1 +'ZM_ae_a', dtype=float)
ZM_ab_b = loadtxt(ruta1 +'ZM_ab_b', dtype=float)
ZM_ac_b = loadtxt(ruta1 +'ZM_ac_b', dtype=float)
ZM_ad_b = loadtxt(ruta1 +'ZM_ad_b', dtype=float)
ZM_ae_b = loadtxt(ruta1 +'ZM_ae_b', dtype=float)
ZM_ab_c = loadtxt(ruta1 +'ZM_ab_c', dtype=float)
ZM_ac_c = loadtxt(ruta1 +'ZM_ac_c', dtype=float)
ZM_ad_c = loadtxt(ruta1 +'ZM_ad_c', dtype=float)
ZM_ae_c = loadtxt(ruta1 +'ZM_ae_c', dtype=float)
ZM_ab_d = loadtxt(ruta1 +'ZM_ab_d', dtype=float)
ZM_ac_d = loadtxt(ruta1 +'ZM_ac_d', dtype=float)
ZM_ad_d = loadtxt(ruta1 +'ZM_ad_d', dtype=float)
ZM_ae_d = loadtxt(ruta1 +'ZM_ae_d', dtype=float)
ZM_ab_e = loadtxt(ruta1 +'ZM_ab_e', dtype=float)
ZM_ac_e = loadtxt(ruta1 +'ZM_ac_e', dtype=float)
ZM_ad_e = loadtxt(ruta1 +'ZM_ad_e', dtype=float)
ZM_ae_e = loadtxt(ruta1 +'ZM_ae_e', dtype=float)

#Tamanofiguras

rcParams['figure.figsize'] = [15, 15]
rcParams['font.size'] = 18
rcParams['axes.labelsize'] = 18

fig = plt.figure()

ax1  = plt.subplot2grid(shape=(3,4), loc=(0,0), colspan=2)
ax2  = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
ax3  = plt.subplot2grid(shape=(3,4), loc=(1,0), colspan=2)
ax4  = plt.subplot2grid(shape=(3,4), loc=(1,2), colspan=2)
ax5  = plt.subplot2grid(shape=(3,4), loc=(2,1), colspan=2)

ax1.plot(ZL_A[0],    ZL_A[1],          color = C1_EN, label = e1)
ax1.plot(ZLM_ab_b[0],ZLM_ab_b[1], 'o', color = C1_FR, label = e2)
ax1.plot(ZLM_ab_c[0],ZLM_ab_c[1], 'o', color = C1_GE, label = e3)
ax1.plot(ZLM_ab_d[0],ZLM_ab_d[1], 'o', color = C1_IT, label = e4)
ax1.plot(ZLM_ab_e[0],ZLM_ab_e[1], 'o', color = C1_SP, label = e5)
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.axis('equal')
ax1.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax1.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax2.plot(ZL_B[0],    ZL_B[1],          color = C1_FR, label = e2)
ax2.plot(ZLM_ab_a[0],ZLM_ab_a[1], 'o', color = C1_EN, label = e1)
ax2.plot(ZLM_ac_c[0],ZLM_ac_c[1], 'o', color = C1_GE, label = e3)
ax2.plot(ZLM_ac_d[0],ZLM_ac_d[1], 'o', color = C1_IT, label = e4)
ax2.plot(ZLM_ac_e[0],ZLM_ac_e[1], 'o', color = C1_SP, label = e5)
ax2.set_xscale('log')
ax2.set_yscale('log')
#ax2.axis('equal')
ax2.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax3.plot(ZL_C[0],    ZL_C[1],          color = C1_GE, label = e3)
ax3.plot(ZLM_ac_a[0],ZLM_ac_a[1], 'o', color = C1_EN, label = e1)
ax3.plot(ZLM_ac_b[0],ZLM_ac_b[1], 'o', color = C1_FR, label = e2)
ax3.plot(ZLM_ad_d[0],ZLM_ad_d[1], 'o', color = C1_IT, label = e4)
ax3.plot(ZLM_ad_e[0],ZLM_ad_e[1], 'o', color = C1_SP, label = e5)
ax3.set_xscale('log')
ax3.set_yscale('log')
#ax3.axis('equal')
ax3.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax3.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax4.plot(ZL_D[0],    ZL_D[1],          color = C1_IT, label = e4)
ax4.plot(ZLM_ad_a[0],ZLM_ad_a[1], 'o', color = C1_EN, label = e2)
ax4.plot(ZLM_ad_b[0],ZLM_ad_b[1], 'o', color = C1_FR, label = e2)
ax4.plot(ZLM_ad_c[0],ZLM_ad_c[1], 'o', color = C1_GE, label = e3)
ax4.plot(ZLM_ae_e[0],ZLM_ae_e[1], 'o', color = C1_SP, label = e5)
ax4.set_xscale('log')
ax4.set_yscale('log')
#ax4.axis('equal')
ax4.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax5.plot(ZL_E[0],    ZL_E[1],          color = C1_SP, label = e5)
ax5.plot(ZLM_ae_a[0],ZLM_ae_a[1], 'o', color = C1_EN, label = e1)
ax5.plot(ZLM_ae_b[0],ZLM_ae_b[1], 'o', color = C1_FR, label = e2)
ax5.plot(ZLM_ae_c[0],ZLM_ae_c[1], 'o', color = C1_GE, label = e3)
ax5.plot(ZLM_ae_d[0],ZLM_ae_d[1], 'o', color = C1_IT, label = e4)
ax5.set_xscale('log')
ax5.set_yscale('log')
#ax5.axis('equal')
ax5.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax5.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

plt.tight_layout()

#fig.savefig(ruta2 +'ZL_todos.png', bbox_inches = 'tight')

fig = plt.figure()

ax1  = plt.subplot2grid(shape=(3,4), loc=(0,0), colspan=2)
ax2  = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
ax3  = plt.subplot2grid(shape=(3,4), loc=(1,0), colspan=2)
ax4  = plt.subplot2grid(shape=(3,4), loc=(1,2), colspan=2)
ax5  = plt.subplot2grid(shape=(3,4), loc=(2,1), colspan=2)

ax1.plot(ZM_ab_b[0], ZM_ab_b[1], color = C1_FR, label = e_ab_b)
ax1.plot(ZM_ab_c[0], ZM_ab_c[1], color = C1_GE, label = e_ab_c)
ax1.plot(ZM_ab_d[0], ZM_ab_d[1], color = C1_IT, label = e_ab_d)
ax1.plot(ZM_ab_e[0], ZM_ab_e[1], color = C1_SP, label = e_ab_e)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax1.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax2.plot(ZM_ab_a[0], ZM_ab_a[1], color = C1_EN, label = e_ab_a)
ax2.plot(ZM_ac_c[0], ZM_ac_c[1], color = C1_GE, label = e_ac_c)
ax2.plot(ZM_ac_d[0], ZM_ac_d[1], color = C1_IT, label = e_ac_d)
ax2.plot(ZM_ac_e[0], ZM_ac_e[1], color = C1_SP, label = e_ac_e)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax3.plot(ZM_ac_a[0], ZM_ac_a[1], color = C1_EN, label = e_ac_a)
ax3.plot(ZM_ac_b[0], ZM_ac_b[1], color = C1_FR, label = e_ac_b)
ax3.plot(ZM_ad_d[0], ZM_ad_d[1], color = C1_IT, label = e_ad_d)
ax3.plot(ZM_ad_e[0], ZM_ad_e[1], color = C1_SP, label = e_ad_e)
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax3.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax4.plot(ZM_ad_a[0], ZM_ad_a[1], color = C1_EN, label = e_ad_a)
ax4.plot(ZM_ad_b[0], ZM_ad_b[1], color = C1_FR, label = e_ad_b)
ax4.plot(ZM_ad_c[0], ZM_ad_c[1], color = C1_GE, label = e_ad_c)
ax4.plot(ZM_ae_e[0], ZM_ae_e[1], color = C1_SP, label = e_ae_e)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax5.plot(ZM_ae_a[0], ZM_ae_a[1], color = C1_EN, label = e_ae_a)
ax5.plot(ZM_ae_b[0], ZM_ae_b[1], color = C1_FR, label = e_ae_b)
ax5.plot(ZM_ae_c[0], ZM_ae_c[1], color = C1_GE, label = e_ae_c)
ax5.plot(ZM_ae_d[0], ZM_ae_d[1], color = C1_IT, label = e_ae_d)
ax5.set_xscale('log')
ax5.set_yscale('log')
ax5.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax5.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

plt.tight_layout()

#fig.savefig(ruta2 +'ZL_receptor.png', bbox_inches = 'tight')

fig = plt.figure()

ax1  = plt.subplot2grid(shape=(3,4), loc=(0,0), colspan=2)
ax2  = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
ax3  = plt.subplot2grid(shape=(3,4), loc=(1,0), colspan=2)
ax4  = plt.subplot2grid(shape=(3,4), loc=(1,2), colspan=2)
ax5  = plt.subplot2grid(shape=(3,4), loc=(2,1), colspan=2)

ax1.plot(ZM_ab_a[0], ZM_ab_a[1], color = C1_FR, label = e_ab_a)
ax1.plot(ZM_ac_a[0], ZM_ac_a[1], color = C1_GE, label = e_ac_a)
ax1.plot(ZM_ad_a[0], ZM_ad_a[1], color = C1_IT, label = e_ad_a)
ax1.plot(ZM_ae_a[0], ZM_ae_a[1], color = C1_SP, label = e_ae_a)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax1.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax2.plot(ZM_ab_b[0], ZM_ab_b[1], color = C1_EN, label = e_ab_b)
ax2.plot(ZM_ac_b[0], ZM_ac_b[1], color = C1_GE, label = e_ac_b)
ax2.plot(ZM_ad_b[0], ZM_ad_b[1], color = C1_IT, label = e_ad_b)
ax2.plot(ZM_ae_b[0], ZM_ae_b[1], color = C1_SP, label = e_ae_b)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax3.plot(ZM_ab_c[0], ZM_ab_c[1], color = C1_EN, label = e_ab_c)
ax3.plot(ZM_ac_c[0], ZM_ac_c[1], color = C1_FR, label = e_ac_c)
ax3.plot(ZM_ad_c[0], ZM_ad_c[1], color = C1_IT, label = e_ad_c)
ax3.plot(ZM_ae_c[0], ZM_ae_c[1], color = C1_SP, label = e_ae_c)
ax3.set_xscale('log')
ax3.set_yscale('log')
ax3.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax3.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax4.plot(ZM_ab_d[0], ZM_ab_d[1], color = C1_EN, label = e_ab_d)
ax4.plot(ZM_ac_d[0], ZM_ac_d[1], color = C1_FR, label = e_ac_d)
ax4.plot(ZM_ad_d[0], ZM_ad_d[1], color = C1_GE, label = e_ad_d)
ax4.plot(ZM_ae_d[0], ZM_ae_d[1], color = C1_SP, label = e_ae_d)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax5.plot(ZM_ab_e[0], ZM_ab_e[1], color = C1_EN, label = e_ab_e)
ax5.plot(ZM_ac_e[0], ZM_ac_e[1], color = C1_FR, label = e_ac_e)
ax5.plot(ZM_ad_e[0], ZM_ad_e[1], color = C1_GE, label = e_ad_e)
ax5.plot(ZM_ae_e[0], ZM_ae_e[1], color = C1_IT, label = e_ae_e)
ax5.set_xscale('log')
ax5.set_yscale('log')
ax5.set_ylabel(r'$f\,(k)$', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax5.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

plt.tight_layout()

#fig.savefig(ruta2 +'ZL_origen.png', bbox_inches = 'tight')