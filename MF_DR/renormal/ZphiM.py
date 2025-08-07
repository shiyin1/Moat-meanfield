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
ZM300=np.loadtxt('./Zmu290M300.dat')
ZM400=np.loadtxt('./Zmu290M400.dat')
ZM500=np.loadtxt('./Zmu290M500.dat')

T=np.arange(1,300)

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(ZM300,'b-',linewidth=1.5,alpha=0.6,label=r'$M=300\,\mathrm{MeV}$')
ax1.plot(ZM400,dashes=[3,2],color='orange',linewidth=1.5,alpha=0.6,label=r'$M=400\,\mathrm{MeV}$')
ax1.plot(ZM500,linestyle=(0,(3,1,1,1)),color='g',linewidth=1.5,alpha=0.6,label=r'$M=500\,\mathrm{MeV}$')
ax1.text(221,1.2,r'$\mu=290\,\mathrm{MeV}$',fontsize=10)
ax1.axis([0,300,-0.25,2.3])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$Z^\perp_{\pi}(0)$', fontsize=14, color='black')

plt.axes([0.3, 0.6, 0.29, 0.27]) 
plt.plot(ZM300-ZM300[0]+1,'b-',linewidth=1.5,alpha=0.6)
plt.plot(ZM400-ZM400[0]+1,dashes=[3,2],color='orange',linewidth=1.5,alpha=0.6)
plt.plot(ZM500-ZM500[0]+1,linestyle=(0,(3,1,1,1)),color='g',linewidth=1.5,alpha=0.6)
#y=range(-0.25,2.3,0.5)
#x=range(0,300,50)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.axis([0.,300.,-0.25,1.3])

ax1.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.13, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("ZM.pdf")
