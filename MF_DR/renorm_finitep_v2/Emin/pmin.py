#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl

mpl.style.use('classic')

# Data for plotting
#T=np.loadtxt('Tem1/buffer/TMeV.dat')
pmin=np.loadtxt('./pmin.dat')
pf=np.loadtxt('./pF.dat')
T=np.loadtxt('./T1.dat')
pmin[0]=217.613
pmin[1]=217.613

pminT0=np.loadtxt('./pminT0.dat')
pfT0=np.loadtxt('./pFT0.dat')
mu=np.arange(301, 451, 1)
####################################
pfT02=np.loadtxt('./pFT0_mu2.dat')
Ethermal=np.loadtxt('./Ethermal.dat')
psthermal=np.loadtxt('./ps_thermal.dat')

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(121)
ax1.plot(T,pmin/pf,'b-',linewidth=2.5,alpha=0.6,label=r'$\mu=320\,\mathrm{MeV}$')
ax1.plot([-10,100],[0.695,0.695],'k',dashes=[2,1],linewidth=1,alpha=0.3)
#ax1.text(221,1.2,r'$\mu=290\,\mathrm{MeV}$',fontsize=10)
ax1.axis([0,40,0.,1.2])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$p_{\mathrm{min}}/p_{\mathrm{F}}$', fontsize=14, color='black')

#ax1.legend(loc=0,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(8)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

ax1=fig.add_subplot(122)
ax1.plot(mu,pminT0/pfT0-10,'b-',linewidth=2.5,alpha=0.6,label=r'$\mu=320\,\mathrm{MeV}$')
ax1.plot(mu,pminT0/pfT0,'r-',linewidth=2.5,alpha=0.6,label=r'$T=0$')
ax1.plot([-10,1000],[0.695,0.695],'k',dashes=[2,1],linewidth=1,alpha=0.3)
ax1.axis([301,450,0.,1.2])

ax1.set_xlabel('$\mu\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_yticklabels([])
ax1.legend(loc=0,fontsize=12,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(8)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.13, right=0.95, hspace=0.35,wspace=0.)

fig.savefig("pmin.pdf")
##################################################################
fig=plt.figure(figsize=(4.5, 3.5))

ax1=fig.add_subplot(111)
ax1.plot(psthermal,Ethermal[0]/10**5,'-',c='#073068',linewidth=2.5,alpha=0.8,label=r'$\mu=302\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[1]/10**5,'-',c='#206FB6',linewidth=2.5,alpha=0.8,label=r'$\mu=322\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[2]/10**5,'-',c='#6BADD7',linewidth=2.5,alpha=0.8,label=r'$\mu=342\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[3]/10**5,'-',c='#C5DAEE',linewidth=2.5,alpha=0.8,label=r'$\mu=362\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[4]/10**5,'-',c='#FDDFD0',linewidth=2.5,alpha=0.8,label=r'$\mu=382\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[5]/10**5,'-',c='#FC9171',linewidth=2.5,alpha=0.8,label=r'$\mu=402\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[6]/10**5,'-',c='#EE3B2A',linewidth=2.5,alpha=0.8,label=r'$\mu=422\,\mathrm{MeV}$')
ax1.plot(psthermal,Ethermal[7]/10**5,'-',c='#A60E16',linewidth=2.5,alpha=0.8,label=r'$\mu=442\,\mathrm{MeV}$')

ax1.plot([2*pfT02[0],2*pfT02[0]],[-2.9,10],dashes=[2,1],c='#073068',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[1],2*pfT02[1]],[-4.2,10],dashes=[2,1],c='#206FB6',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[2],2*pfT02[2]],[-5,10],dashes=[2,1],c='#6BADD7',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[3],2*pfT02[3]],[-5.8,10],dashes=[2,1],c='#C5DAEE',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[4],2*pfT02[4]],[-6.3,10],dashes=[2,1],c='#FDDFD0',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[5],2*pfT02[5]],[-7.2,10],dashes=[2,1],c='#FC9171',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[6],2*pfT02[6]],[-8,10],dashes=[2,1],c='#EE3B2A',linewidth=1,alpha=0.6)
ax1.plot([2*pfT02[7],2*pfT02[7]],[-8.7,10],dashes=[2,1],c='#A60E16',linewidth=1,alpha=0.6)

ax1.axis([0,1000,-1*10,0])

ax1.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\Pi^\pi_{\mathrm{thermal}}(\mathbf{p},\mu)-\Pi^\pi_{\mathrm{thermal}}(\mathbf{p}=0,\mu)\,[ \times 10^5\,\mathrm{MeV}]$', fontsize=10, color='black')
ax1.legend(loc=0,fontsize=8.5,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.15, right=0.95, hspace=0.35,wspace=0.)

fig.savefig("Ethermal.pdf")