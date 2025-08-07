#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
from scipy.interpolate import make_interp_spline
from matplotlib.ticker import FuncFormatter
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.cm as cm 
from matplotlib.font_manager import FontProperties
import pylab as pl

mpl.style.use('classic')
# Data for plotting
Vrmu400T0data=np.loadtxt('./Vrmu400T0.dat')
Vrmu301T0data=np.loadtxt('./Vrmu301T0.dat')
Vrmu290T0data=np.loadtxt('./Vrmu290T0.dat')

qFmu400=798.978/2.
qFmu301=27.7694
#print(Vrmu400T0data.T[0])
p = np.linspace(0, 1000, 201)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)
ax1.plot(Vrmu301T0data.T[0]*qFmu301,Vrmu301T0data.T[1]*10**4,c='k',linewidth=2.5,alpha=0.7,label=r'$V(r)\times\,10^4\,\mu=301\,\mathrm{MeV}\,\,T=0$')
ax1.plot(Vrmu400T0data.T[0]*qFmu400,Vrmu400T0data.T[1],c='b',linewidth=2.5,alpha=0.7,label=r'$V(r)\,\qquad\quad\,\mu=400\,\mathrm{MeV}\,\,T=0$')
ax1.plot([0,20],[0,0],c='k',dashes=(1,1))
#ax1.text(480, 650, r'$\mu=400\,\mathrm{MeV}\,\,T=0$', fontsize=12, color='black')
#ax1.text(10, 585, r'$(0,600)$', fontsize=12, color='red')
#ax1.text(200, 620, r'$(282,707)$', fontsize=12, color='red')
ax1.axis([0.,12,-1.5,3.])
ax1.legend(loc=4,fontsize='9',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

ax1.set_ylabel(r'$V(r)\,\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.set_xlabel(r'$p_F\,\,r$', fontsize=13, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

plt.axes([0.52, 0.58, 0.39, 0.32]) 
plt.plot(Vrmu290T0data.T[0],Vrmu290T0data.T[1],'r-',linewidth=1.5,alpha=0.6,label=r'$\mu=290\,\mathrm{MeV}\,\,T=0$')
#plt.text(0.03, 1.7, r'$\mu=290\,\mathrm{MeV}$', fontsize=12, color='k')
#plt.text(0.03, 1, r'$T=0$', fontsize=12, color='k')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.axis([0.01,0.1,-0.3,2.5])
plt.ylabel(r'$V(r)\,\,[\mathrm{MeV}]$', fontsize=8, color='black')
plt.xlabel(r'$r\,\,[\mathrm{MeV}^{-1}]$', fontsize=8, color='black')
plt.legend(loc=0,fontsize='7',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

fig.subplots_adjust(top=0.95, bottom=0.14, left=0.15, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./Vr.pdf")
########################################################################
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)
ax1.plot(Vrmu301T0data.T[0],Vrmu301T0data.T[1]*10**4,c='k',linewidth=2.5,alpha=0.7,label=r'$\mu=301\,\mathrm{MeV}\,\,T=0$')
#ax1.plot(Vrmu400T0data.T[0],Vrmu400T0data.T[1],c='b',linewidth=2.5,alpha=0.7,label=r'$\mu=400\,\mathrm{MeV}\,\,T=0$')
ax1.plot([0,1],[0,0],c='k',dashes=(1,1))
#ax1.text(480, 650, r'$\mu=400\,\mathrm{MeV}\,\,T=0$', fontsize=12, color='black')
#ax1.text(10, 585, r'$(0,600)$', fontsize=12, color='red')
#ax1.text(200, 620, r'$(282,707)$', fontsize=12, color='red')
ax1.axis([0.005,0.5,-0.00015*10**4,0.0003*10**4])
ax1.legend(loc=0,fontsize='10',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

ax1.set_ylabel(r'$V(r)\,\,[\times\,10^{-4}\mathrm{MeV}]$', fontsize=13, color='black')
ax1.set_xlabel(r'$r\,\,[\mathrm{MeV}^{-1}]$', fontsize=13, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.95, bottom=0.14, left=0.15, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./Vrmu301.pdf")