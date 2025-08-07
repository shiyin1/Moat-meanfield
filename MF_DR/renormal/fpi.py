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
sigmadata=np.loadtxt('./M300.dat')
mu0=sigmadata[0:299]
mu100=sigmadata[300:599]
mu200=sigmadata[600:899]
mu250=sigmadata[900:1199]
mu290=sigmadata[1200:1499]
mu300=sigmadata[1500:1799]
T=np.arange(1,300)

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.scatter(T,mu0,color=[0,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=0$')
ax1.scatter(T,mu100,color=[0.2,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=100\,\mathrm{MeV}$')
ax1.scatter(T,mu200,color=[0.4,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=200\,\mathrm{MeV}$')
ax1.scatter(T,mu250,color=[0.6,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=250\,\mathrm{MeV}$')
ax1.scatter(T,mu290,color=[0.8,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=290\,\mathrm{MeV}$')
ax1.scatter(T,mu300,color=[1,0,0],s=10,alpha=0.6,edgecolors='none',label=r'$\mu=300\,\mathrm{MeV}$')

ax1.axis([0,300,0,95])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$\sigma_0\,[\mathrm{MeV}]$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=9,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.12, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("sigma.pdf")
