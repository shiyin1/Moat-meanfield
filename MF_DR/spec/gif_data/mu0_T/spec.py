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

# 1. 确保读取了所有 20 组数据 (修改 range 为 1, 21)
data_list = []
for x in range(1, 43):
    file_name = f"./spec_data_v2/rhoT{10+x*5}.dat"
    try:
        data = np.loadtxt(file_name)
        data_list.append(data)
    except Exception as e:
        print(f"读取 {file_name} 失败: {e}")

# 2. 准备网格
omega = np.arange(1, 703, 2)
ps = np.arange(1, 499, 2)
xnew, ynew = np.meshgrid(omega, ps)

fig = plt.figure(figsize=(4.5, 3.5))
ax1 = fig.add_subplot(1, 1, 1, projection='3d')
vnorm = mpl.colors.Normalize(vmin=0, vmax=1.2)

# 3. 定义更新函数
def update(frame):
    ax1.cla()  # 必须清除，否则多层表面会重叠导致变黑
    
    # 数据预处理（根据你的逻辑处理每一帧数据）
    current_raw = data_list[frame]
    threshold=10/10**7
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
    ax1.set_zlabel(r'$\rho_{\pi}\,[\mathrm{MeV}^2\times\,10^6]$', fontsize=10, rotation=0)
    
    ax1.set_xlim([0, 701])
    ax1.set_ylim([0, 501])
    ax1.set_zlim([0, 1])
    ax1.view_init(elev=40, azim=235)
    ax1.set_title(f"T = {(frame+1)*5+10} MeV") # 动态标题
    
    return surf,

# 4. 创建动画
# interval=200 表示每 0.2 秒切换一组数据
ani = FuncAnimation(fig, update, frames=len(data_list), interval=300, repeat=True)

# 5. 展示或保存
# plt.show() # 预览
ani.save('spec_animation.gif', writer='pillow') # 保存为GIF
print("动画已生成")
