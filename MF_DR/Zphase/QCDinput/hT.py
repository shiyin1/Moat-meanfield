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
hQCD=np.loadtxt('./mub0/buffer/h.dat')
hQCD2=np.loadtxt('./mub600/buffer/h.dat')
hmodel=np.loadtxt('./hdata1.dat')

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.plot(hQCD/hQCD[0],dashes=[1,0],c='#08306b',linewidth=2.5,alpha=0.8,label=r'fRG-QCD (2019) $\mu=0$')
#ax1.plot(hQCD2/hQCD2[0],dashes=[1,1],c='#08306b',linewidth=2.5,alpha=0.8,label=r'fRG-QCD (2019)')
ax1.plot(hmodel[0]/hmodel[0,0],dashes=[1,0],c='#a50f15',linewidth=2.5,alpha=0.8,label=r'one-loop $\mu=0$',zorder=1)
#ax1.plot(hmodel[39]/hmodel[0,0],dashes=[1,0],c='#a50f15',linewidth=2.5,alpha=0.5,label=r'one-loop $\mu=200\,\mathrm{MeV}$',zorder=1)
#ax1.plot(hmodel[69]/hmodel[0,0],dashes=[1,0],c='#a50f15',linewidth=2.5,alpha=0.2,label=r'one-loop $\mu=350\,\mathrm{MeV}$',zorder=1)
ax1.plot([0,250],[1,1],dashes=[3,2],c='r',linewidth=2.5,alpha=0.8,label=r'Mean-field QM',zorder=0)

miloc=plt.MultipleLocator(10000)
ax1.xaxis.set_minor_locator(miloc)
ax1.grid(which='major')
#ax1.plot(k2,hbare2,'-',c='b',linewidth=2,label=r'$h_{k=UV}=50$')
#ax1.plot(k3,hbare3,'-',c='r',linewidth=2,label=r'$h_{k=UV}=100$')
#ax1.plot(k4,hbare4,'-',c='g',linewidth=2,label=r'$h_{k=UV}=150$')
#ax1.plot(k5,hbare5,'-',c='m',linewidth=2,label=r'$h_{k=UV}=200$')

#ax1.text(220,1.25,'$\Lambda=700\,\mathrm{MeV}$')
ax1.axis([1,250,0.4,1.2])
#ax1.set_xscale('log')
#ax1.set_yscale('log')
#ax1.set_yticks([5000,10000,15000,20000,25000,30000,35000,40000])
#ax1.set_yticklabels([r'5',r'10',r'15',r'20',r'25',r'30',r'35',r'40'],rotation=0,fontsize=7)
ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$h(T,\mu)/h(T=0,\mu=0)$', fontsize=14, color='black')

ax1.legend(loc=3,fontsize=9.5,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

#plt.axes([0.245, 0.23, 0.29, 0.27]) 
#plt.plot(k1,hbare1,'-',c='k',linewidth=1)
#plt.plot(k2,hbare2,'-',c='b',linewidth=1)
#plt.plot(k3,hbare3,'-',c='r',linewidth=1)
#plt.plot(k4,hbare4,'-',c='g',linewidth=1)
#plt.plot(k5,hbare5,'-',c='m',linewidth=1)
#plt.yscale('log')
#plt.xticks(fontsize=5)
#plt.yticks(fontsize=5)
#plt.axis([0.,20000.,1.,1.e5])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)



fig.subplots_adjust(top=0.9, bottom=0.135, left=0.15, right=0.95, hspace=0.35,wspace=0.35)

fig.savefig("hTv2.pdf")
