#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
#from scipy.interpolate import spline
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties
import pylab as pl

mpl.style.use('classic')
# Data for plotting
Zdata_in=np.loadtxt('./Zdata.dat')
Zdata_trans=Zdata_in.T
Zdata1=Zdata_trans[:,0:57]
Zdata3=Zdata_trans[:,61:80]
Zdata_in2=np.loadtxt('./Zdatap2.dat')
Zdata_trans2=Zdata_in2.T
Zdata2=Zdata_trans2
T=np.arange(1, 301, 1)
mu=np.arange(5, 405, 5)
mu2=np.arange(289, 310, 1)
# Create figure
fig=plt.figure(figsize=(4.56, 3))
####################################################################################################
# Create figure
ax2=fig.add_subplot(111)
im=ax2.imshow(Zdata1, cmap=plt.get_cmap('RdYlGn'),interpolation='nearest',extent=[5,280,300,1],vmin=-1,vmax=1,aspect=1,zorder=2)
im2=ax2.imshow(Zdata2, cmap=plt.get_cmap('RdYlGn'),interpolation='nearest',extent=[280,310,300,1],vmin=-1,vmax=1,aspect=1,zorder=2)
im3=ax2.imshow(Zdata3, cmap=plt.get_cmap('RdYlGn'),interpolation='nearest',extent=[310,400,300,1],vmin=-1,vmax=1,aspect=1,zorder=2)
vnorm = mpl.colors.Normalize(vmin=-1, vmax=1)
plt.rcParams['font.size'] = 7
cbar=plt.colorbar(im,fraction=0.031, pad=0.04,norm=vnorm)
#X1, Y1 = np.meshgrid(mu, T)
#contours1 = plt.contour(X1, Y1, Zdata_trans, colors='k',levels=[0.])
#X2, Y2 = np.meshgrid(mu2, T)
#contours2 = plt.contour(X2, Y2, Zdata2, colors='k',levels=[0.])
#X3, Y3 = np.meshgrid(mu[61:80], T)
#contours3 = plt.contour(X3, Y3, Zdata3, colors='k',levels=[0.])
#cbar.set_label(r'$Z^\perp_\pi(M=500\mathrm{MeV})$', rotation=0,fontsize=9)
plt.scatter(292,30,color='k',marker='o',s=10,label=r'CEP',zorder=3)
plt.axis([0.,400.,0.,300.])
ax2.set_title(r'$M=300\,\mathrm{MeV}$',loc='center')
ax2.set_xlabel('$\mu\,[\mathrm{MeV}]$', fontsize=10, color='black')
ax2.set_ylabel(r'$T\,[\mathrm{MeV}]$', fontsize=10, color='black')
for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(8)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(8)

ax2.legend(loc=0,fontsize=6,frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

fig.subplots_adjust(top=0.85, bottom=0.15, left=-0.85, right=0.94, hspace=0.1,
                    wspace=0.1)


fig.savefig("phase1.pdf",dpi=300,transparent=True)