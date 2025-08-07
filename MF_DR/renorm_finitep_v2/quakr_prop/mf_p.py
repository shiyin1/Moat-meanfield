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
ZsT10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/mf.dat')
ZsT10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/mf.dat')
ZsT10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/mf.dat')
ZsT10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/mf.dat')
ps=np.arange(1, 2000, 10)
#print(mu)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(ps, ZsT10mu5_norm/ZsT10mu5_norm[0],color='b',linewidth=2.,alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=5\,\mathrm{MeV}\,\,E^{\mathrm{free}}_\pi$') 
ax1.plot(ps, ZsT10mu5_moat/ZsT10mu5_moat[0],color='k',linewidth=2.,dashes=(2.5,1.),alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=5\,\mathrm{MeV}\,\,E^{\mathrm{1-loop}}_\pi$') 
ax1.plot(ps, ZsT10mu400_norm/ZsT10mu400_norm[0],color='g',linewidth=2.,alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=400\,\mathrm{MeV}\,\,E^{\mathrm{free}}_\pi$') 
ax1.plot(ps, ZsT10mu400_moat/ZsT10mu400_moat[0],color='r',linewidth=2.,dashes=(2.5,1.),alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=400\,\mathrm{MeV}\,\,E^{\mathrm{1-loop}}_\pi$') 

#ax1.plot([0,600], [1,1],alpha=0.8,dashes=(0.5,0.5)) 
ax1.set_ylabel(r'$m_f(|\mathbf{p}|)/m_f(0)$', fontsize=13, color='black')
ax1.set_xlabel(r'$|\mathbf{p}|\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.legend(loc=2,fontsize='8',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
ax1.axis([0,2000,0.68,1.25])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.15, left=0.16, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./mf_ps.pdf")


