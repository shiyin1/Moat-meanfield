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
mub400T10MSbarVS=np.loadtxt('./mu400T10_MSbpVS.dat')
mub400T10MSbar=np.loadtxt('./mu400T10_MSb.dat')
p = np.linspace(-1000, 1000, 201)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)
levels = np.linspace(0, 1.95, 100)
contour_filled = ax1.contourf(p/1000,p/1000,mub400T10MSbarVS.T/10**6, levels=levels, cmap='viridis', vmin=0, vmax=1.95)
contour        = ax1.contour(p/1000,p/1000,mub400T10MSbarVS.T/10**6, levels=levels, linewidths=0.2, colors='white')
cbar = fig.colorbar(contour_filled, ax=ax1, pad=0.02)
cbar.ax.tick_params(labelsize=8, direction='in', length=6, width=1)
cbar.set_label(r'$\Sigma_\pi(\bf{p})\,[\mathrm{GeV}^2]$', fontsize=13,rotation=270,labelpad=20)
#ax1.plot([0,0],[40.4,1000],color='white',linestyle='-')
#ax1.plot([0,0],[-40.4,-1000],color='white',linestyle='-')
#ax1.scatter([282],[705],c='pink',marker='o',edgecolors='none',zorder=10)
#ax1.scatter([-282],[705],c='pink',marker='o',edgecolors='none',zorder=10)
#ax1.scatter([282],[-705],c='pink',marker='o',edgecolors='none',zorder=10)
#ax1.scatter([-282],[-705],c='pink',marker='o',edgecolors='none',zorder=10)
ax1.plot([0,0],[39.2296/1000,1000],color='c',linestyle='-',linewidth=2)
ax1.plot([0,0],[-39.2296/1000,-1000],color='c',linestyle='-',linewidth=2)
ax1.scatter([0],[39.2296/1000],c='red',marker='o',edgecolors='none',zorder=10)
ax1.scatter([0],[-39.2296/1000],c='red',marker='o',edgecolors='none',zorder=10)
ax1.scatter([799.038/1000],[0],c='b',marker='o',edgecolors='none',zorder=10)
ax1.scatter([-799.038/1000],[0],c='b',marker='o',edgecolors='none',zorder=10)

ax1.set_title(r'$\mu=400\,\mathrm{MeV}\,\,T=10\,\mathrm{MeV}$', fontsize=12, color='black', loc='center')
ax1.axis([-1000/1000,1000/1000,-1000/1000,1000/1000])

ax1.set_xlabel(r'$\mathrm{Re}\,\,|\bf{p}|\,[\mathrm{GeV}]$', fontsize=13, color='black')
ax1.set_ylabel(r'$\mathrm{Im}\,\,|\bf{p}|\,[\mathrm{GeV}]$', fontsize=13, color='black')
for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.94, bottom=0.13, left=0.147, right=0.94, hspace=0.33,wspace=0.2)

fig.savefig("./mu400T10_MSbarVS.pdf")
########################################################################
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=plt.subplot(1,1,1)
levels = np.linspace(0, 2.5, 100)
contour_filled = ax1.contourf(p/1000,p/1000,mub400T10MSbar.T/10**6, levels=levels, cmap='viridis', vmin=0, vmax=2.5)
contour        = ax1.contour(p/1000,p/1000,mub400T10MSbar.T/10**6, levels=levels, linewidths=0.2, colors='white')
cbar = fig.colorbar(contour_filled, ax=ax1, pad=0.02)
cbar.ax.tick_params(labelsize=8, direction='in', length=6, width=1)
cbar.set_label(r'$\Sigma_\pi(\bf{p})\,[\mathrm{GeV}^2]$', fontsize=13,rotation=270,labelpad=20)
ax1.plot([0,0],[39.2296/1000,1000],color='c',linestyle='-',linewidth=2)
ax1.plot([0,0],[-39.2296/1000,-1000],color='c',linestyle='-',linewidth=2)
ax1.scatter([0],[39.2296/1000],c='red',marker='o',edgecolors='none',zorder=10)
ax1.scatter([0],[-39.2296/1000],c='red',marker='o',edgecolors='none',zorder=10)
ax1.scatter([799.038/1000],[0],c='b',marker='o',edgecolors='none',zorder=10)
ax1.scatter([-799.038/1000],[0],c='b',marker='o',edgecolors='none',zorder=10)

ax1.set_title(r'$\mu=400\,\mathrm{MeV}\,\,T=10\,\mathrm{MeV}$', fontsize=12, color='black', loc='center')
ax1.set_xlabel(r'$\mathrm{Re}\,\,|\bf{p}|\,[\mathrm{GeV}]$', fontsize=13, color='black')
ax1.set_ylabel(r'$\mathrm{Im}\,\,|\bf{p}|\,[\mathrm{GeV}]$', fontsize=13, color='black')
ax1.axis([-1000/1000,1000/1000,-1000/1000,1000/1000])

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.94, bottom=0.13, left=0.147, right=0.94, hspace=0.33,wspace=0.2)

fig.savefig("./mu400T10_MSbar.pdf")