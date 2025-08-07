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
Re1=np.loadtxt('./Ep.dat')
print(Re1.shape)
Re=Re1#[0:180,0:40]
mu=np.arange(280, 325, 5)
ps=np.arange(1.,10*60,10)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(ps, Re[0]/Re[0,0],alpha=1,label=r'$\mu=280\,\mathrm{MeV}$') 
ax1.plot(ps, Re[8]/Re[8,0],alpha=1,label=r'$\mu=320\,\mathrm{MeV}$') 
ax1.plot([0,600], [1,1],alpha=0.8,dashes=(0.5,0.5)) 
ax1.set_ylabel(r'$E_\pi(\mathrm{p})/E_\pi(0)$', fontsize=13, color='black')
ax1.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.legend(loc=0,fontsize='10',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
ax1.axis([0,600,0.9,2])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.15, left=0.15, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./gammapion_T30.pdf")


