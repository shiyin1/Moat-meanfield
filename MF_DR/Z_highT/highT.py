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
Zdata=np.loadtxt('./Zall.dat')
Zdata2=np.loadtxt('./Zall2.dat')
highTdata=np.loadtxt('./ZhighTdata.dat')

Zvac=np.loadtxt('./Zvac.dat')
Zph=np.loadtxt('./ZPH.dat')
Zca=np.loadtxt('./ZCA.dat')

Zvacmu320=np.loadtxt('./Zvacmu320.dat')
Zphmu320=np.loadtxt('./ZPHmu320.dat')
Zcamu320=np.loadtxt('./ZCAmu320.dat')

p = np.linspace(0, 10000, 10001)
Thigh = np.linspace(10, 2000, 200)

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)
ax1.plot(p,Zdata,c='k',linewidth=2.5,alpha=0.6,label=r'$Z^\perp_\pi$')

ax1.plot(Thigh[40:200],highTdata[40:200],c='r',dashes=[2,1],linewidth=2.5,alpha=0.7,label=r'Large-T limit')

ax1.plot(Thigh,Zvac,c='b',linewidth=2.5,alpha=0.5,label=r'Vacuum part')
ax1.plot(Thigh,Zca+Zvac,c='m',dashes=[3,1,1,1],linewidth=2.5,alpha=0.5,label=r'CA part')
ax1.plot(Thigh,Zph,c='g',dashes=[1,1],linewidth=2.5,alpha=0.5,label=r'PH part')
ax1.text(28,4,r'$\mu=0$',fontsize=15)

ax1.set_xscale('log')
ax1.axis([10.,2000,-5,15.])
ax1.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

ax1.set_ylabel(r'$Z^{\perp}_\pi(p=0)$', fontsize=13, color='black')
ax1.set_xlabel(r'$T\,[\mathrm{MeV}]$', fontsize=13, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.143, right=0.95, hspace=0.35, wspace=0.35)

fig.savefig("./highT.pdf")
#####################################################
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
ax1=plt.subplot(1,1,1)
ax1.plot(Thigh,Zvacmu320+Zphmu320+Zcamu320,c='k',linewidth=2.5,alpha=0.6,label=r'$Z^\perp_\pi$ at $\mu=320$ MeV')

ax1.plot(Thigh,Zvacmu320,c='b',linewidth=2.5,alpha=0.5,label=r'Vacuum part')
ax1.plot(Thigh,Zcamu320+Zvacmu320,c='m',dashes=[3,1,1,1],linewidth=2.5,alpha=0.5,label=r'CA part')
ax1.plot(Thigh,Zphmu320,c='g',dashes=[1,1],linewidth=2.5,alpha=0.5,label=r'PH part')
ax1.text(300,4,r'$\mu=320$ $\mathrm{MeV}$',fontsize=15)

ax1.set_xscale('log')
ax1.axis([10.,2000,-2,8])
#ax1.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

ax1.set_ylabel(r'$Z^{\perp}_\pi(p=0)$', fontsize=13, color='black')
ax1.set_xlabel(r'$T\,[\mathrm{MeV}]$', fontsize=13, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.143, right=0.95, hspace=0.35, wspace=0.35)

fig.savefig("./highTmu320.pdf")