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

# mpl.style.use('classic')

# data_list = []
# for x in range(1, 2):
#     # 使用 f-string 构建文件名：rhoT1.dat, rhoT2.dat ...
#     file_name = f"./spec_data/rhoT{x*10}.dat"
    
#     try:
#         # 读取数据并存入列表
#         data = np.loadtxt(file_name)
#         data_list.append(data)
#         print(f"成功读取: {file_name}")
#     except Exception as e:
#         print(f"读取 {file_name} 失败: {e}")

# # 查看总共有多少组数据 (列表长度)
# print(f"总数据组数: {len(data_list)}")

# # 查看第一组数据的结构 (假设第一组存在)
# if len(data_list) > 0:
#     first_data = data_list[0]
#     print(f"单组数据的类型: {type(first_data)}")
#     print(f"单组数据的形状 (行, 列): {first_data.shape}")

# omega=np.arange(1, 711, 10)
# ps=np.arange(1,511,10)
# spec1 = np.where((data_list[0] > 9/10**7), np.nan, data_list[0])
# #spec1=data_list[0]

# fig=plt.figure(figsize=(4.5, 3.5))
# #fig=plt.figure()
# ax1=plt.subplot(1,1,1,projection='3d')
# xnew, ynew = np.meshgrid(omega, ps)
# vnorm = mpl.colors.Normalize(vmin=0, vmax=1.)
# vnorm1 = mpl.colors.Normalize(vmin=0., vmax=2.)
# plt.rcParams['font.size'] = 7
# im=ax1.plot_surface(xnew, ynew, spec1*10**7, rstride=1, cstride=1, cmap="rainbow",edgecolor=(0,0,0,0.3), antialiased=True,linewidth=0.2,norm=vnorm) 
# #im2=ax1.plot_surface(xnew, ynew, spec1*10**6, rstride=1, cstride=1, cmap="gray",edgecolor=(0,0,0,0.3), antialiased=True,linewidth=0.2,norm=vnorm1) 
# ax1.set_ylabel(r'$\mathbf{p}\,[\mathrm{MeV}]$', fontsize=13, color='black')
# ax1.set_xlabel(r'$\omega\,[\mathrm{MeV}]$', fontsize=13, color='black')
# ax1.zaxis.set_rotate_label(False)
# ax1.set_zlabel(r'$\rho_{\pi}(\omega,\mathbf{p})\,[\mathrm{MeV}^2\times10^6]$', fontsize=13, color='black', rotation=90)
# ax1.view_init(elev=40,azim=235)
# ax1.set_xlim([0, 701])
# ax1.set_ylim([0, 501])
# ax1.set_zlim([0, 9])
# #ax1.set_zscale('log')
# for label in ax1.xaxis.get_ticklabels():
#     label.set_fontsize(7)
# for label in ax1.yaxis.get_ticklabels():
#     label.set_fontsize(7)
# for label in ax1.zaxis.get_ticklabels():
#     label.set_fontsize(7)

# fig.subplots_adjust(top=1., bottom=0.07, left=0.1, right=0.99, hspace=0.33,wspace=0.2)

# fig.savefig("./spec.pdf")

# 1. 确保读取了所有 20 组数据 (修改 range 为 1, 21)
data_list = []
for x in range(1, 21):
    file_name = f"./spec_data/rhoT{x*10}.dat"
    try:
        data = np.loadtxt(file_name)
        data_list.append(data)
    except Exception as e:
        print(f"读取 {file_name} 失败: {e}")

# 2. 准备网格
omega = np.arange(1, 711, 10)
ps = np.arange(1, 511, 10)
xnew, ynew = np.meshgrid(omega, ps)

fig = plt.figure(figsize=(4.5, 3.5))
ax1 = fig.add_subplot(1, 1, 1, projection='3d')
vnorm = mpl.colors.Normalize(vmin=0, vmax=1.5)

# 3. 定义更新函数
def update(frame):
    ax1.cla()  # 必须清除，否则多层表面会重叠导致变黑
    
    # 数据预处理（根据你的逻辑处理每一帧数据）
    current_raw = data_list[frame]
    spec_frame = np.where((current_raw > 20/10**7), np.nan, current_raw)
    
    # 绘制单层表面 (去掉 im2，防止重叠变黑)
    surf = ax1.plot_surface(xnew, ynew, spec_frame * 10**6, 
                            rstride=2, cstride=2, # 增大步长可提升动画流畅度
                            cmap="rainbow", 
                            edgecolor=(0,0,0,0.2), 
                            linewidth=0.1, 
                            norm=vnorm)
    
    # 重新设置坐标轴属性 (cla会重置所有设置)
    ax1.set_ylabel(r'$\mathbf{p}$', fontsize=10)
    ax1.set_xlabel(r'$\omega$', fontsize=10)
    ax1.set_zlabel(r'$\rho_{\pi}$', fontsize=10, rotation=90)
    
    ax1.set_xlim([0, 701])
    ax1.set_ylim([0, 501])
    ax1.set_zlim([0, 1.])
    ax1.view_init(elev=40, azim=235)
    ax1.set_title(f"T = {frame*10+10} MeV") # 动态标题
    
    return surf,

# 4. 创建动画
# interval=200 表示每 0.2 秒切换一组数据
ani = FuncAnimation(fig, update, frames=len(data_list), interval=200, repeat=True)

# 5. 展示或保存
# plt.show() # 预览
ani.save('spec_animation.gif', writer='pillow') # 保存为GIF
print("动画已生成")
