import matplotlib.pyplot as plt

# 启用 LaTeX 渲染
plt.rcParams['text.usetex'] = False  # 不使用完整的 LaTeX 引擎，而是使用 mathtext
plt.rcParams['mathtext.fontset'] = 'dejavusans'  # 设置 mathtext 字体为 DejaVu Sans
plt.rcParams['font.family'] = 'DejaVu Sans'  # 设置主字体为 DejaVu Sans

# 绘图示例
fig, ax = plt.subplots()
ax.set_title(r"$E = mc^2$", fontsize=20)
ax.set_xlabel(r"$\alpha + \beta$", fontsize=15)
ax.set_ylabel(r"$\int_a^b f(x)dx$", fontsize=15)

plt.show()