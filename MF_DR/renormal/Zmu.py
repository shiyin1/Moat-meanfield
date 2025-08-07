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
Zdata=np.loadtxt('./Zdata.dat')
mu0=Zdata[0]
mu100=Zdata[19]
mu200=Zdata[39]
mu250=Zdata[49]
mu290=Zdata[57]
mu300=Zdata[59]
mu320=Zdata[63]
mu380=Zdata[75]
T=np.arange(0,300)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.scatter(T,mu0,color=[0,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=0$')
ax1.scatter(T,mu100,color=[1/7,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=100\,\mathrm{MeV}$')
ax1.scatter(T,mu200,color=[2/7,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=200\,\mathrm{MeV}$')
ax1.scatter(T,mu250,color=[3/7,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=250\,\mathrm{MeV}$')
ax1.scatter(T,mu290,color=[4/7,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=290\,\mathrm{MeV}$')
ax1.scatter(T,mu300,color=[5/7,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=300\,\mathrm{MeV}$')
ax1.scatter(T,mu320,color=[6/7,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=320\,\mathrm{MeV}$')
ax1.scatter(T,mu380,color=[1,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=380\,\mathrm{MeV}$')
ax1.plot([0,300],[0.,0.],color='k',dashes=[1,1],alpha=0.2)


ax1.axis([0,300,-0.55,1.5])

ax1.set_xlabel(r'$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$Z^\perp_\pi(0)$', fontsize=14, color='black')

ax1.legend(loc=(-0.03,0.78),fontsize=8,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1,ncol=3)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.15, right=0.95, hspace=0.35, wspace=0.35)

fig.savefig("Zmu.pdf")
