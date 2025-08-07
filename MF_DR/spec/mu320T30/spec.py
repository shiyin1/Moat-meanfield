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
#spec=np.loadtxt('./spec.dat')
Re1=np.loadtxt('./RedataT30mu320.dat')
Im1=np.loadtxt('./ImdataT30mu320.dat')
Im1=Im1[0:101,0:121]
spec=np.loadtxt('./spec.dat')
spec1 = np.where((spec < 1.45/10**6), np.nan, spec)
omega=np.arange(1, 602, 5)
ps=np.arange(1,502,5)
#spec[spec <= 0] = np.nan 
#speclog=np.log10(spec)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1,projection='3d')
xnew, ynew = np.meshgrid(omega, ps)
vnorm = mpl.colors.Normalize(vmin=0, vmax=1.5)
vnorm1 = mpl.colors.Normalize(vmin=0., vmax=2.)
plt.rcParams['font.size'] = 7
im=ax1.plot_surface(xnew, ynew, spec*10**6, rstride=1, cstride=1, cmap="rainbow",edgecolor=(0,0,0,0.3), antialiased=True,linewidth=0.2,norm=vnorm) 
im2=ax1.plot_surface(xnew, ynew, spec1*10**6, rstride=1, cstride=1, cmap="gray",edgecolor=(0,0,0,0.3), antialiased=True,linewidth=0.2,norm=vnorm1) 
ax1.set_ylabel(r'$\mathbf{p}\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.set_xlabel(r'$\omega\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.zaxis.set_rotate_label(False)
ax1.set_zlabel(r'$\rho_{\pi}(\omega,\mathbf{p})\,[\mathrm{MeV}^2\times10^6]$', fontsize=13, color='black', rotation=90)
ax1.view_init(elev=40,azim=235)
ax1.set_xlim([0, 601])
ax1.set_ylim([0, 501])
ax1.set_zlim([0, 1.5])
#ax1.set_zscale('log')
#ax1.legend(loc=0,fontsize='8',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
#ax1.set_xticks([0,50,100,150,200])
#ax1.set_xticklabels(['0','50','100','150','200'],rotation=0,fontsize=7)
#ax1.set_yticks([0,100,200,300,400])
#ax1.set_yticklabels(['0','100','200','300','400'],rotation=0,fontsize=7)
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(7)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(7)
for label in ax1.zaxis.get_ticklabels():
    label.set_fontsize(7)

fig.subplots_adjust(top=1., bottom=0.07, left=0.1, right=0.99, hspace=0.33,wspace=0.2)

fig.savefig("./spec_mu320_T30.pdf")


