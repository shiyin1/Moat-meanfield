#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

# 示例数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 自定义 colormap 和 norm
norm = Normalize(vmin=np.min(z), vmax=np.max(z))
colors = cm.viridis(norm(z))  # 使用 viridis colormap

# 选择某一区域改变颜色，例如 Z > 0 的区域
colors[z > 0] = cm.autumn(norm(z[z > 0]))  # Z > 0 区域使用 autumn colormap

# 绘制 3D 图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制 plot_surface，指定 facecolors
surf = ax.plot_surface(x, y, z, facecolors=colors, rstride=1, cstride=1)

plt.show()