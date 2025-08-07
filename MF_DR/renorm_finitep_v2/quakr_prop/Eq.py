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
Z0T10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/Zq0.dat')
Z0T10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/Zq0.dat')
Z0T10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/Zq0.dat')
Z0T10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/Zq0.dat')

ZsT10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/Zqs.dat')
ZsT10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/Zqs.dat')
ZsT10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/Zqs.dat')
ZsT10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/Zqs.dat')

mfT10mu5_norm=np.loadtxt('./Sigma_normal/T10mu5/mf.dat')
mfT10mu5_moat=np.loadtxt('./Sigma_moat/T10mu5/mf.dat')
mfT10mu400_norm=np.loadtxt('./Sigma_normal/T10mu400/mf.dat')
mfT10mu400_moat=np.loadtxt('./Sigma_moat/T10mu400/mf.dat')

ps=np.arange(1, 2000, 10)

EqT10mu5_norm=  (ZsT10mu5_norm/Z0T10mu5_norm*ps**2+mfT10mu5_norm/Z0T10mu5_norm)
EqT10mu5_moat=  (ZsT10mu5_moat/Z0T10mu5_moat*ps**2+mfT10mu5_moat/Z0T10mu5_moat)
EqT10mu400_norm=(ZsT10mu400_norm/Z0T10mu400_norm*ps**2+mfT10mu400_norm/Z0T10mu400_norm)
EqT10mu400_moat=(ZsT10mu400_moat/Z0T10mu400_moat*ps**2+mfT10mu400_moat/Z0T10mu400_moat)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(ps, EqT10mu5_norm/EqT10mu5_norm[0]/10000,color='b',linewidth=3.,alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=5\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(ps, EqT10mu5_moat/EqT10mu5_moat[0]/10000,color='k',linewidth=3.,dashes=(2.5,1.),alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=5\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(ps, EqT10mu400_norm/EqT10mu400_norm[0]/10000,color='g',linewidth=3.,alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=400\,\mathrm{MeV}\,\,E_\pi=\sqrt{q^2+m^2_{\pi,\mathrm{1-loop}}}$') 
ax1.plot(ps, EqT10mu400_moat/EqT10mu400_moat[0]/10000,color='r',linewidth=3.,dashes=(2.5,1.1,1),alpha=0.7,label=r'$T=10\,\mathrm{MeV}\,\,\mu=400\,\mathrm{MeV}\,\,E_\pi=\sqrt{Z^{\perp}_{\pi,\mathrm{1-loop}}q^2+m^2_{\pi,\mathrm{1-loop}}}$') 

ax1.set_ylabel(r'$\Sigma_q(\mathbf{p}^2)/\Sigma_q(0)\,[\times\,10^4]$', fontsize=13, color='black')
ax1.set_xlabel(r'$\mathbf{p}\,[\mathrm{MeV}]$', fontsize=13, color='black')
ax1.legend(loc=0,fontsize='7',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)
ax1.axis([0,1000,0,4.2])
#ax1.set_yticks([0.94,0.96,0.98,1.00,1.02],[r'0.94',r'0.96',r'0.98',r'1.00',r'1.02'])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.15, left=0.13, right=0.95, hspace=0.33,wspace=0.2)

fig.savefig("./Eq_quark.pdf")