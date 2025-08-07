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
ZsT10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/Zqs.dat')
ZsT10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/Zqs.dat')
ZsT10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/Zqs.dat')
ZsT10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/Zqs.dat')

Z0T10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/Zq0.dat')
Z0T10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/Zq0.dat')
Z0T10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/Zq0.dat')
Z0T10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/Zq0.dat')

mfT10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/mf.dat')
mfT10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/mf.dat')
mfT10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/mf.dat')
mfT10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/mf.dat')

ps=np.arange(1, 2000, 10)
#print(mu)
# Create figure
fig=plt.figure(figsize=(3.5, 6.))
#fig=plt.figure()
ax1=fig.add_subplot(311)
ax1.plot(ps, ZsT10mu5_norm,color='b',linewidth=2.,alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=5\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(ps, ZsT10mu5_moat,color='k',linewidth=2.,dashes=(2.5,1.),alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=5\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(ps, ZsT10mu400_norm,color='g',linewidth=2.,alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=400\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(ps, ZsT10mu400_moat,color='r',linewidth=2.,dashes=(2.5,1.),alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=400\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
#ax1.plot([0,600], [1,1],alpha=0.8,dashes=(0.5,0.5)) 
ax1.set_ylabel(r'$Z^\perp_q(|\mathbf{p}|)$', fontsize=13, color='black')
#ax1.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.legend(loc=(0.02,0.5),fontsize='6.1',frameon=False,shadow=False,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
ax1.axis([0,2000,1.05,1.65])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)
ax1.set_xticklabels([])
###################################################
ax2=fig.add_subplot(312)
ax2.plot(ps, Z0T10mu5_norm,color='b',linewidth=2.,alpha=0.7) 
ax2.plot(ps, Z0T10mu5_moat,color='k',linewidth=2.,dashes=(2.5,1.),alpha=0.7) 
ax2.plot(ps, Z0T10mu400_norm,color='g',linewidth=2.,alpha=0.7) 
ax2.plot(ps, Z0T10mu400_moat,color='r',linewidth=2.,dashes=(2.5,1.),alpha=0.7) 
ax2.set_ylabel(r'$Z^\|_q(|\mathbf{p}|)$', fontsize=13, color='black')
#ax2.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax2.axis([0,2000,1.05,1.65])

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)
ax2.set_xticklabels([])
###################################################
ax3=fig.add_subplot(313)
ax3.plot(ps, mfT10mu5_norm/mfT10mu5_norm[0],color='b',linewidth=2.,alpha=0.7) 
ax3.plot(ps, mfT10mu5_moat/mfT10mu5_moat[0],color='k',linewidth=2.,dashes=(2.5,1.),alpha=0.7) 
ax3.plot(ps, mfT10mu400_norm/mfT10mu400_norm[0],color='g',linewidth=2.,alpha=0.7) 
ax3.plot(ps, mfT10mu400_moat/mfT10mu400_moat[0],color='r',linewidth=2.,dashes=(2.5,1.),alpha=0.7) 
ax3.set_ylabel(r'$m_f(|\mathbf{p}|)/m_f(0)$', fontsize=13, color='black')
ax3.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax3.axis([0,2000,0.6,1.15])

for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.95, bottom=0.1, left=0.2, right=0.92, hspace=0.,wspace=0.2)

fig.savefig("./Zpsi_3parts.pdf")


