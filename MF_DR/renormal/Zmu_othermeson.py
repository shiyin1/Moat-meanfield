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
#Zdata=np.loadtxt('./Zdata.dat')
Zsigmadata=np.loadtxt('../Zsigma_T50_mu.dat')
Zetadata=np.loadtxt('../Zeta_T50_mu.dat')
Zrhodata=np.loadtxt('../Zrho_T50_mu.dat')
Za1data=np.loadtxt('../Za1_T50_mu.dat')
#Zpi=Zdata.T[50]

mu=np.arange(0,500,5)

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(mu,Zetadata,color=[0,0,0],alpha=0.3,linewidth=2,label=r'$\pi$')
ax1.scatter(mu,Zsigmadata,color=[0.5,0,0],s=10,alpha=0.7,edgecolors='none',label=r'$\sigma$')
ax1.scatter(mu,Zetadata,color=[0,0.5,0],s=10,alpha=0.7,edgecolors='none',label=r'$\eta$')
ax1.scatter(mu,Zrhodata,color=[0,0,0.5],s=10,alpha=0.7,edgecolors='none',label=r'$\rho$')
ax1.scatter(mu,Za1data,color=[0,0.5,0.5],s=10,alpha=0.7,edgecolors='none',label=r'$a_1$')
ax1.plot([0,550],[0.,0.],color='k',dashes=[1,1],alpha=0.2)
ax1.text(50,-0.5,r'$T=50\,\mathrm{MeV}$',fontsize=12)
ax1.axis([0,500,-1.,5.])

ax1.set_xlabel('$\mu\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$Z^\perp(0)$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=9,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

plt.axes([0.21, 0.6, 0.29, 0.27]) 
plt.scatter(mu,Zsigmadata-(Zsigmadata[99]-Zetadata[99]),color=[0.5,0,0],s=10,alpha=0.7,edgecolors='none',label=r'$\sigma$')
plt.scatter(mu,Zetadata,color=[0,0.5,0],s=10,alpha=0.7,edgecolors='none',label=r'$\eta$')
plt.scatter(mu,Zrhodata,color=[0,0,0.5],s=10,alpha=0.7,edgecolors='none',label=r'$\rho$')
plt.scatter(mu,Za1data-(Za1data[99]-Zrhodata[99]),color=[0,0.5,0.5],s=10,alpha=0.7,edgecolors='none',label=r'$a_1$')
plt.plot([0,550],[0.,0.],color='k',dashes=[1,1],alpha=0.2)
#y=range(-0.25,2.3,0.5)
#x=range(0,300,50)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.axis([0.,500.,-1,1.5])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.14, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("Zmu_othermeson.pdf")