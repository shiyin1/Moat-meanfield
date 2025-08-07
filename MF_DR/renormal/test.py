#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 使用 Seaborn 的调色板
colors = sns.color_palette("husl", 5)  # husl 调色板

# 示例数据
x = np.linspace(0, 10, 100)

for i, color in enumerate(colors):
    plt.plot(x, np.sin(x + i), label=f'Line {i+1}', color=color)

plt.legend()
plt.show()

x = np.linspace(0, 10, 100)
cmap = plt.get_cmap('plasma')

for i in range(5):
    plt.plot(x, np.sin(x + i), label=f'Line {i+1}', color=cmap(i / 5.0))

plt.legend()
plt.show()

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

for i, color in enumerate(colors):
    plt.plot(x, np.sin(x + i), label=f'Line {i+1}', color=color)

plt.legend()
plt.show()

colors = sns.color_palette("colorblind", 5)  # 色盲友好调色板

for i, color in enumerate(colors):
    plt.plot(x, np.sin(x + i), label=f'Line {i+1}', color=color)

plt.legend()
plt.show()