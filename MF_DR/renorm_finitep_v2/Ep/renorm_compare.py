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
v1=np.loadtxt('./renormv1.dat')
v2=np.loadtxt('./renormv2.dat')
ps=np.loadtxt('./ps.dat')

# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)

ax1.plot(ps, v1/10**6,color='k',alpha=0.6,linewidth=2,label=r'$\overline{MS}$') 
ax1.plot(ps, v2/10**6,color='b',alpha=0.6,linewidth=2,label=r'$\overline{MS}+\mathrm{Vacuum\,\,Subtraction}$') 
ax1.plot([0,2000],[0,0],dashes=[1,1],color='k',alpha=0.2,linewidth=1) 
ax1.text(100, 1.8, r'$\mu=400\,\mathrm{MeV},\,T=10\,\mathrm{MeV}$', fontsize=12, color='k')

ax1.set_ylabel(r'$\Sigma_\pi(0,|\mathbf{p}|)\,[\times 10^6\,\mathrm{MeV}^2]$', fontsize=13, color='black')
ax1.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=13, color='black')

ax1.legend(loc=0,fontsize='10',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

ax1.axis([0,1500,-3*10**5/10**6,3*10**6/10**6])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.13, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./renorm_compare.pdf")