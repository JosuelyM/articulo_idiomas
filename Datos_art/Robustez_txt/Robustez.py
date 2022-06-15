
# coding: utf-8

# In[1]:


from pylab import *


# In[3]:


ruta1 = "Datos/"
ruta2 = "Figuras/"


etiqueta1 = "_a.npy"
etiqueta2 = "_b.npy"
etiqueta3 = "_c.npy"
etiqueta4 = "_d.npy"
etiqueta5 = "_e.npy"

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


# In[4]:


######################
### Carga de Datos ###
######################

LB_ab_a = loadtxt(ruta1 + 'LB_ab_a', dtype=float)
LB_ac_a = loadtxt(ruta1 + 'LB_ac_a', dtype=float)
LB_ad_a = loadtxt(ruta1 + 'LB_ad_a', dtype=float)
LB_ae_a = loadtxt(ruta1 + 'LB_ae_a', dtype=float)
LB_ab_b = loadtxt(ruta1 + 'LB_ab_b', dtype=float)
LB_ac_b = loadtxt(ruta1 + 'LB_ac_b', dtype=float)
LB_ad_b = loadtxt(ruta1 + 'LB_ad_b', dtype=float)
LB_ae_b = loadtxt(ruta1 + 'LB_ae_b', dtype=float)
LB_ab_c = loadtxt(ruta1 + 'LB_ab_c', dtype=float)
LB_ac_c = loadtxt(ruta1 + 'LB_ac_c', dtype=float)
LB_ad_c = loadtxt(ruta1 + 'LB_ad_c', dtype=float)
LB_ae_c = loadtxt(ruta1 + 'LB_ae_c', dtype=float)
LB_ab_d = loadtxt(ruta1 + 'LB_ab_d', dtype=float)
LB_ac_d = loadtxt(ruta1 + 'LB_ac_d', dtype=float)
LB_ad_d = loadtxt(ruta1 + 'LB_ad_d', dtype=float)
LB_ae_d = loadtxt(ruta1 + 'LB_ae_d', dtype=float)
LB_ab_e = loadtxt(ruta1 + 'LB_ab_e', dtype=float)
LB_ac_e = loadtxt(ruta1 + 'LB_ac_e', dtype=float)
LB_ad_e = loadtxt(ruta1 + 'LB_ad_e', dtype=float)
LB_ae_e = loadtxt(ruta1 + 'LB_ae_e', dtype=float)


LA_ab_a = loadtxt(ruta1 + 'LA_ab_a', dtype=float)
LA_ac_a = loadtxt(ruta1 + 'LA_ac_a', dtype=float)
LA_ad_a = loadtxt(ruta1 + 'LA_ad_a', dtype=float)
LA_ae_a = loadtxt(ruta1 + 'LA_ae_a', dtype=float)
LA_ab_b = loadtxt(ruta1 + 'LA_ab_b', dtype=float)
LA_ac_b = loadtxt(ruta1 + 'LA_ac_b', dtype=float)
LA_ad_b = loadtxt(ruta1 + 'LA_ad_b', dtype=float)
LA_ae_b = loadtxt(ruta1 + 'LA_ae_b', dtype=float)
LA_ab_c = loadtxt(ruta1 + 'LA_ab_c', dtype=float)
LA_ac_c = loadtxt(ruta1 + 'LA_ac_c', dtype=float)
LA_ad_c = loadtxt(ruta1 + 'LA_ad_c', dtype=float)
LA_ae_c = loadtxt(ruta1 + 'LA_ae_c', dtype=float)
LA_ab_d = loadtxt(ruta1 + 'LA_ab_d', dtype=float)
LA_ac_d = loadtxt(ruta1 + 'LA_ac_d', dtype=float)
LA_ad_d = loadtxt(ruta1 + 'LA_ad_d', dtype=float)
LA_ae_d = loadtxt(ruta1 + 'LA_ae_d', dtype=float)
LA_ab_e = loadtxt(ruta1 + 'LA_ab_e', dtype=float)
LA_ac_e = loadtxt(ruta1 + 'LA_ac_e', dtype=float)
LA_ad_e = loadtxt(ruta1 + 'LA_ad_e', dtype=float)
LA_ae_e = loadtxt(ruta1 + 'LA_ae_e', dtype=float)


# In[6]:


rcParams['figure.figsize'] = [15, 15]
fig = plt.figure()

ax1  = plt.subplot2grid(shape=(3,4), loc=(0,0), colspan=2)
ax2  = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
ax3  = plt.subplot2grid(shape=(3,4), loc=(1,0), colspan=2)
ax4  = plt.subplot2grid(shape=(3,4), loc=(1,2), colspan=2)
ax5  = plt.subplot2grid(shape=(3,4), loc=(2,1), colspan=2)

ax1.plot(LB_ab_a[0], LB_ab_a[1], color = C1_FR, label = e_ab_a)
ax1.plot(LB_ac_a[0], LB_ac_a[1], color = C1_GE, label = e_ac_a)
ax1.plot(LB_ad_a[0], LB_ad_a[1], color = C1_IT, label = e_ad_a)
ax1.plot(LB_ae_a[0], LB_ae_a[1], color = C1_SP, label = e_ae_a)
ax1.plot(LB_ae_a[0], zeros(len(LB_ae_a[0]))+0.1, '--k')
#ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
ax1.set_xlim(0,100)
ax1.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax1.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax1.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax2.plot(LB_ab_b[0], LB_ab_b[1], color = C1_EN, label = e_ab_b)
ax2.plot(LB_ac_b[0], LB_ac_b[1], color = C1_GE, label = e_ac_b)
ax2.plot(LB_ad_b[0], LB_ad_b[1], color = C1_IT, label = e_ad_b)
ax2.plot(LB_ae_b[0], LB_ae_b[1], color = C1_SP, label = e_ae_b)
ax2.plot(LB_ae_a[0], zeros(len(LB_ae_a[0]))+0.1, '--k')
#ax2.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
ax2.set_xlim(0,100)
ax2.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax2.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax2.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax3.plot(LB_ab_c[0], LB_ab_c[1], color = C1_EN, label = e_ab_c)
ax3.plot(LB_ac_c[0], LB_ac_c[1], color = C1_FR, label = e_ac_c)
ax3.plot(LB_ad_c[0], LB_ad_c[1], color = C1_IT, label = e_ad_c)
ax3.plot(LB_ae_c[0], LB_ae_c[1], color = C1_SP, label = e_ae_c)
ax3.plot(LB_ae_a[0], zeros(len(LB_ae_a[0]))+0.1, '--k')
#ax3.set_yticks([0, 0.1, 0.2, 0.3])
ax3.set_xlim(0,100)
ax3.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax3.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax3.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax4.plot(LB_ab_d[0], LB_ab_d[1], color = C1_EN, label = e_ab_d)
ax4.plot(LB_ac_d[0], LB_ac_d[1], color = C1_FR, label = e_ac_d)
ax4.plot(LB_ad_d[0], LB_ad_d[1], color = C1_GE, label = e_ad_d)
ax4.plot(LB_ae_d[0], LB_ae_d[1], color = C1_SP, label = e_ae_d)
ax4.plot(LB_ae_a[0], zeros(len(LB_ae_a[0]))+0.1, '--k')
#ax4.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
ax4.set_xlim(0,100)
ax4.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax4.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax4.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax5.plot(LB_ab_e[0], LB_ab_e[1], color = C1_EN, label = e_ab_e)
ax5.plot(LB_ac_e[0], LB_ac_e[1], color = C1_FR, label = e_ac_e)
ax5.plot(LB_ad_e[0], LB_ad_e[1], color = C1_GE, label = e_ad_e)
ax5.plot(LB_ae_e[0], LB_ae_e[1], color = C1_IT, label = e_ae_e)
ax5.plot(LB_ae_a[0], zeros(len(LB_ae_a[0]))+0.1, '--k')
#ax5.set_yticks([0, 0.1, 0.2, 0.3])
ax5.set_xlim(0,100)
ax5.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax5.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax5.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

plt.tight_layout()

#fig.savefig(ruta2 +'Rp_bajos.png', bbox_inches = 'tight')


# In[9]:


rcParams['figure.figsize'] = [15, 15]
fig = plt.figure()

ax1  = plt.subplot2grid(shape=(3,4), loc=(0,0), colspan=2)
ax2  = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
ax3  = plt.subplot2grid(shape=(3,4), loc=(1,0), colspan=2)
ax4  = plt.subplot2grid(shape=(3,4), loc=(1,2), colspan=2)
ax5  = plt.subplot2grid(shape=(3,4), loc=(2,1), colspan=2)

ax1.plot(LA_ab_a[0], LA_ab_a[1], color = C1_FR, label = e_ab_a)
ax1.plot(LA_ac_a[0], LA_ac_a[1], color = C1_GE, label = e_ac_a)
ax1.plot(LA_ad_a[0], LA_ad_a[1], color = C1_IT, label = e_ad_a)
ax1.plot(LA_ae_a[0], LA_ae_a[1], color = C1_SP, label = e_ae_a)
ax1.plot(LA_ae_a[0], zeros(len(LA_ae_a[0]))+0.1, '--k')
#ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
ax1.set_xlim(0,100)
ax1.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax1.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax1.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax2.plot(LA_ab_b[0], LA_ab_b[1], color = C1_EN, label = e_ab_b)
ax2.plot(LA_ac_b[0], LA_ac_b[1], color = C1_GE, label = e_ac_b)
ax2.plot(LA_ad_b[0], LA_ad_b[1], color = C1_IT, label = e_ad_b)
ax2.plot(LA_ae_b[0], LA_ae_b[1], color = C1_SP, label = e_ae_b)
ax2.plot(LA_ae_a[0], zeros(len(LA_ae_a[0]))+0.1, '--k')
#ax2.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
ax2.set_xlim(0,100)
ax2.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax2.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax2.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax3.plot(LA_ab_c[0], LA_ab_c[1], color = C1_EN, label = e_ab_c)
ax3.plot(LA_ac_c[0], LA_ac_c[1], color = C1_FR, label = e_ac_c)
ax3.plot(LA_ad_c[0], LA_ad_c[1], color = C1_IT, label = e_ad_c)
ax3.plot(LA_ae_c[0], LA_ae_c[1], color = C1_SP, label = e_ae_c)
ax3.plot(LA_ae_a[0], zeros(len(LA_ae_a[0]))+0.1, '--k')
#ax3.set_yticks([0, 0.1, 0.2, 0.3])
ax3.set_xlim(0,100)
ax3.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax3.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax3.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax4.plot(LA_ab_d[0], LA_ab_d[1], color = C1_EN, label = e_ab_d)
ax4.plot(LA_ac_d[0], LA_ac_d[1], color = C1_FR, label = e_ac_d)
ax4.plot(LA_ad_d[0], LA_ad_d[1], color = C1_GE, label = e_ad_d)
ax4.plot(LA_ae_d[0], LA_ae_d[1], color = C1_SP, label = e_ae_d)
ax4.plot(LA_ae_a[0], zeros(len(LA_ae_a[0]))+0.1, '--k')
#ax4.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
ax4.set_xlim(0,100)
ax4.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax4.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax4.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

ax5.plot(LA_ab_e[0], LA_ab_e[1], color = C1_EN, label = e_ab_e)
ax5.plot(LA_ac_e[0], LA_ac_e[1], color = C1_FR, label = e_ac_e)
ax5.plot(LA_ad_e[0], LA_ad_e[1], color = C1_GE, label = e_ad_e)
ax5.plot(LA_ae_e[0], LA_ae_e[1], color = C1_IT, label = e_ae_e)
ax5.plot(LA_ae_a[0], zeros(len(LA_ae_a[0]))+0.1, '--k')
#ax5.set_yticks([0, 0.1, 0.2, 0.3])
ax5.set_xlim(0,100)
ax5.set_xlabel(r'$R_{p}$', fontsize= 23, fontweight = "bold")
ax5.set_ylabel(r'$< D > $', rotation=90, fontsize= 23, fontweight = "bold", position=(0.9,0.53))
ax5.legend(loc=0, ncol=2, frameon=False, handlelength=0.5)

plt.tight_layout()

#fig.savefig(ruta2 +'Rp_altos.png', bbox_inches = 'tight')

