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
ZT10_norm=np.loadtxt('./Zpsi_normal/T10/Zpsi.dat')
ZT10_moat=np.loadtxt('./Zpsi_moat/T10/Zpsi.dat')
ZT30_norm=np.loadtxt('./Zpsi_normal/T30/Zpsi.dat')
ZT30_moat=np.loadtxt('./Zpsi_moat/T30/Zpsi.dat')
ZT50_norm=np.loadtxt('./Zpsi_normal/T50/Zpsi.dat')
ZT50_moat=np.loadtxt('./Zpsi_moat/T50/Zpsi.dat')
mu=np.arange(5, 405, 5)
#print(mu)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(mu[1:60], ZT10_norm[1:60],color='k',linewidth=3.,alpha=0.6,label=r'$T=10\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(mu[60:80], ZT10_norm[60:80],color='k',linewidth=3.,alpha=0.6) 
ax1.plot(mu[1:60], ZT10_moat[1:60],color='k',dashes=[2.,0.5],linewidth=3.,alpha=0.6,label=r'$T=10\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(mu[60:80], ZT10_moat[60:80],color='k',dashes=[2.,0.5],linewidth=3.,alpha=0.6) 

ax1.plot(mu[1:59], ZT30_norm[1:59],color='g',linewidth=3.,alpha=0.6,label=r'$T=30\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(mu[59:80], ZT30_norm[59:80],color='g',linewidth=3.,alpha=0.6) 
ax1.plot(mu[1:59], ZT30_moat[1:59],color='g',dashes=[2.,0.5],linewidth=3.,alpha=0.6,label=r'$T=30\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(mu[59:80], ZT30_moat[59:80],color='g',dashes=[2.,0.5],linewidth=3.,alpha=0.6) 

ax1.plot(mu, ZT50_norm,color='m',linewidth=3.,alpha=0.6,label=r'$T=50\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(mu, ZT50_moat,color='m',dashes=[2.,0.5],linewidth=3.,alpha=0.6,label=r'$T=50\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 

#ax1.plot([0,600], [1,1],alpha=0.8,dashes=(0.5,0.5)) 
ax1.set_ylabel(r'$Z^\perp_q(0)$', fontsize=13, color='black')
ax1.set_xlabel(r'$\mu\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.legend(loc=2,fontsize='6.5',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
ax1.axis([0,400,1.17,1.6])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./Zpsi.pdf")


