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
highTdata=np.loadtxt('./highTlim.dat')

p = np.linspace(0, 10000, 10001)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)
ax1.plot(p,Zdata,c='k',linewidth=2.5,alpha=0.6,label=r'$Z^\perp_\pi$ at $\mu=0$')
#ax1.plot(Zdata2[:,0],Zdata2[:,1],c='k',linewidth=2.5,alpha=0.6)
ax1.plot(highTdata[:,0],highTdata[:,1],c='r',dashes=[1,1],linewidth=2.5,alpha=0.7,label=r'High T limit')
#ax1.plot([0,20],[0,0],c='k',dashes=(1,1))
#ax1.text(7000, -1, r'$\mu=0$', fontsize=15, color='black')
#ax1.text(10, 585, r'$(0,600)$', fontsize=12, color='red')
#ax1.text(200, 620, r'$(282,707)$', fontsize=12, color='red')
ax1.set_xscale('log')
ax1.axis([10.,10000,-6,2.])
ax1.legend(loc=0,fontsize='9',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

ax1.set_ylabel(r'$Z^{\perp}_\pi$', fontsize=13, color='black')
ax1.set_xlabel(r'$T\,[\mathrm{MeV}]$', fontsize=13, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.95, bottom=0.14, left=0.15, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./highT.pdf")