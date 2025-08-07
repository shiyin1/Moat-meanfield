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
#pmin=np.concatenate((pmin1[0:24],pmin2))
#T=np.concatenate((T1[0:24],T2))
#sigma=np.loadtxt('./sigmamu320T.dat')
#mf2=6.5**2*sigma**2/2./2.
#pfermi=(320.**2-mf2)**0.5
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(T,pmin/pf,'b-',linewidth=2.5,alpha=0.6,label=r'$\mu=320\,\mathrm{MeV}$')
#ax1.text(221,1.2,r'$\mu=290\,\mathrm{MeV}$',fontsize=10)
ax1.axis([0,40,0.55,0.75])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$p_{\mathrm{min}}/p_{\mathrm{F}}$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.13, right=0.95, hspace=0.35,wspace=0.35)

fig.savefig("pmin.pdf")
