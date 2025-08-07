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
Re1=np.loadtxt('./gammapion.dat')
print(Re1.shape)
Re=Re1[0:180,0:40]
mu=np.arange(280, 320, 1)
ps=np.arange(3.,3*181,3)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1,projection='3d')
xnew, ynew = np.meshgrid(mu, ps)
vnorm = mpl.colors.Normalize(vmin=135**2/10**4, vmax=470**2/10**4)
plt.rcParams['font.size'] = 7
im=ax1.plot_surface(xnew, ynew, Re/10**4, rstride=3, cstride=1, cmap="rainbow",alpha=1.,edgecolor=(0,0,0,0.1), antialiased=True,linewidth=0.2,norm=vnorm) 
ax1.set_ylabel(r'$\mathbf{p}\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.set_xlabel(r'$\mu\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.zaxis.set_rotate_label(False)
ax1.set_zlabel(r'$\Sigma^{(2)}_{\pi}(\mathbf{p,\mu})\,[\mathrm{MeV}^2\times10^4]$', fontsize=13, color='black', rotation=90)
ax1.view_init(elev=10,azim=220)
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

fig.subplots_adjust(top=1.1, bottom=0., left=0.1, right=0.99, hspace=0.33,wspace=0.2)

fig.savefig("./gammapion_mu_T30.pdf")


