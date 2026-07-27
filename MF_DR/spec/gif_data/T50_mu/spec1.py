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
from matplotlib.animation import FuncAnimation

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

ps_sigma=np.arange(1, 801, 20)

crossover=np.loadtxt('./crossover.dat')
firstorder=np.loadtxt('./firstorder.dat')
# 1. 确保读取了所有 20 组数据 (修改 range 为 1, 21)
data_list = []
for x in range(20, 61):
    file_name = f"./spec_data_v1/rhoT50mu{100+x*5}.dat"
    try:
        data = np.loadtxt(file_name)
        data_list.append(data)
    except Exception as e:
        print(f"读取 {file_name} 失败: {e}")
    print(x)

data_list_sigma = []
for x in range(20, 61):
    file_name = f"./sigmapi_mu_T50/sigmamu{100+x*5}.dat"
    try:
        data = np.loadtxt(file_name)
        data_list_sigma.append(data)
    except Exception as e:
        print(f"读取 {file_name} 失败: {e}")
    print(x)

# 2. 准备网格
omega = np.arange(1, 703, 2)
ps = np.arange(1, 499, 2)
xnew, ynew = np.meshgrid(omega, ps)

fig = plt.figure(figsize=(15, 4))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1])
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

vnorm = mpl.colors.Normalize(vmin=0, vmax=1.2)

def draw_static_ax2():
    # 绘制相图背景
    im1 = ax2.imshow(Zdata1, cmap='bwr', interpolation='nearest', 
                     extent=[1, 285, 1, 300], vmin=-1, vmax=1, aspect='auto', zorder=1, origin='lower')
    ax2.imshow(Zdata2, cmap='bwr', interpolation='nearest', 
               extent=[285, 310, 1, 300], vmin=-1, vmax=1, aspect='auto', zorder=1, origin='lower')
    ax2.imshow(Zdata3, cmap='bwr', interpolation='nearest', 
               extent=[310, 400, 1, 300], vmin=-1, vmax=1, aspect='auto', zorder=1, origin='lower')

    # 关键：只在外部创建一次 colorbar
    if not hasattr(draw_static_ax2, "cbar_created"):
        cbar = plt.colorbar(im1, ax=ax2, fraction=0.046, pad=0.02)
        cbar.set_label('$Z^\perp_{\pi}$', fontsize=12, labelpad=3)
        draw_static_ax2.cbar_created = True

# 3. 定义更新函数
def update(frame):
    ax1.cla()  # 必须清除，否则多层表面会重叠导致变黑
    
    # 数据预处理（根据你的逻辑处理每一帧数据）
    current_raw = data_list[frame]
    threshold=25/10**7
    threshold2=-0.3/10**7
    spec_frame = np.where((current_raw > threshold) | (current_raw < threshold2), np.nan, current_raw)
    
    # 绘制单层表面 (去掉 im2，防止重叠变黑)
    surf = ax1.plot_surface(xnew, ynew, (spec_frame * 10**6).T, 
                            rstride=4, cstride=4, # 增大步长可提升动画流畅度
                            cmap="rainbow", 
                            edgecolor=(0,0,0,0.2), 
                            linewidth=0.1, 
                            norm=vnorm)
    
    # 重新设置坐标轴属性 (cla会重置所有设置)
    ax1.set_ylabel(r'$\mathbf{p}\,[\mathrm{MeV}]$', fontsize=10)
    ax1.set_xlabel(r'$\omega\,[\mathrm{MeV}]$', fontsize=10)
    ax1.set_zlabel(r'$\rho_{\pi}\,[\mathrm{MeV}^{-2}\times\,10^{-6}]$', fontsize=10, rotation=0)
    
    ax1.set_xlim([0, 701])
    ax1.set_ylim([0, 501])
    ax1.set_zlim([0, 2.5])
    ax1.view_init(elev=40, azim=235)
    ax1.set_title(f"$\mu$ = {(frame+1)*5+195} MeV T= 50 MeV") # 动态标题


    ax2.cla()
    draw_static_ax2() 
    # 这里假设你的相图横轴是 T，纵轴是 mu (或其他参数)
    # 你需要根据实际情况定义 T_path 和 mu_path
    current_mu = (frame + 1) * 5 + 195
    
    # 绘制背景（例如：绘制一条虚线表示扫描路径）
    mu_range = np.linspace(195, 400, 49)
    ax2.plot(mu_range, [50]*len(mu_range), 'k--', alpha=0.3) # 假设 mu=0 的路径
    
    # 绘制当前点（大红点表示当前位置）
    ax2.scatter( current_mu,50, color='black', s=100, zorder=5)

    #im=ax2.imshow(Zdata1, cmap=plt.get_cmap('RdYlGn'),interpolation='nearest',extent=[5,280,300,1],vmin=-1,vmax=1,aspect=1,zorder=1)
    #im2=ax2.imshow(Zdata2, cmap=plt.get_cmap('RdYlGn'),interpolation='nearest',extent=[280,310,300,1],vmin=-1,vmax=1,aspect=1,zorder=1)
    #im3=ax2.imshow(Zdata3, cmap=plt.get_cmap('RdYlGn'),interpolation='nearest',extent=[310,400,300,1],vmin=-1,vmax=1,aspect=1,zorder=1)
    #plt.rcParams['font.size'] = 7
    #cbar=ax2.colorbar(im,fraction=0.031, pad=0.04,norm=vnorm)

    ax2.plot(crossover[:,0],crossover[:,1],color='black',dashes=[3,1],linewidth=2.5,label='Crossover',zorder=2)
    ax2.plot(firstorder[:,0],firstorder[:,1],color='black',linewidth=2.5,label='First Order',zorder=2)
    ax2.scatter(297,30,color='m',marker='o',s=20,label=r'CEP',zorder=3)

    # 2D 坐标轴设置
    ax2.set_xlim([0, 400])
    ax2.set_ylim([0, 300]) # 根据你的相图范围调整
    ax2.set_ylabel('Temperature T [MeV]')
    ax2.set_xlabel('Chemical Potential $\mu$ [MeV]')
    ax2.set_title('Scanning Path in Phase Diagram')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc=1,fontsize=9,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

    ax3.cla()
    current_raw = data_list_sigma[frame]
    ax3.plot(ps_sigma,current_raw/current_raw[0],color='black',dashes=[3,0],linewidth=2.5,label='Renormalized static energy',zorder=2)

    ax3.set_xlim([0, 700])
    ax3.set_ylim([0.6, 1.5]) # 根据你的相图范围调整
    ax3.set_ylabel(r'$E_\pi(\mathbf{p})/E_\pi(\mathbf{p}=0)$')
    ax3.set_xlabel('$\mathbf{p}$ [MeV]')
    ax3.set_title('Static energy of pion')
    ax3.legend(loc=1,fontsize=9,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1,scatterpoints=1)

    return surf,

# 4. 创建动画
# interval=200 表示每 0.2 秒切换一组数据
ani = FuncAnimation(fig, update, frames=len(data_list), interval=150, repeat=True)

# 5. 展示或保存
# plt.show() # 预览
fig.subplots_adjust(top=0.91, bottom=0.14, left=0.02, right=0.95, hspace=0.2, wspace=0.35)
ani.save('spec_T50mu.gif', writer='pillow') # 保存为GIF
print("动画已生成")
######################################################################