#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl

mpl.style.use('classic')

# Data for plotting
#T=np.loadtxt('Tem1/buffer/TMeV.dat')
sigma=np.loadtxt('./sigma5.dat')
print(sigma**0.5)
# Create figure
fig=plt.figure(figsize=(4.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(sigma**0.5,'b-',linewidth=1.5,alpha=0.6,label=r'$M=300\,\mathrm{MeV}$')
#ax1.axis([0,200,0,500])

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel('$Z^\perp_{\pi}(0)$', fontsize=14, color='black')

ax1.legend(loc=0,fontsize=10,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,scatterpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

fig.subplots_adjust(top=0.9, bottom=0.14, left=0.13, right=0.95, hspace=0.35,
                    wspace=0.35)

fig.savefig("ZM.pdf")
