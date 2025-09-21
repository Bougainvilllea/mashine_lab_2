import matplotlib.pyplot as plt
import numpy as np


# 1

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]

plt.grid(True, color='red', alpha=0.9, linestyle='-')

ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1/5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(True, which='minor', alpha=0.8, linestyle=':', color='gray')

plt.xlim(-0.4, len(x) - 0.5)
plt.ylim(0, max(y) + 2)

plt.bar(x, y, color='blue', alpha=0.7)

plt.xlabel('Language')
plt.ylabel('Popularity')
plt.title('Пример столбчатой диаграммы')
plt.show()

# 2

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]

plt.grid(True, color='red', alpha=0.9, linestyle='-')

ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1/5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(True, which='minor', alpha=0.8, linestyle=':', color='gray')

plt.ylim(-0.4, len(x) - 0.5)
plt.xlim(0, max(y) + 2)

plt.barh(x, y, color='green', alpha=0.7)

plt.xlabel('Language')
plt.ylabel('Popularity')
plt.title('Пример столбчатой диаграммы')
plt.show()

# 3

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']

plt.grid(True, color='red', alpha=0.9, linestyle='-')

ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1/5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(True, which='minor', alpha=0.8, linestyle=':', color='gray')

plt.xlim(-0.4, len(x) - 0.5)
plt.ylim(0, max(y) + 2)

plt.bar(x, y, color=colors)

plt.xlabel('Language')
plt.ylabel('Popularity')
plt.title('Пример столбчатой диаграммы')
plt.show()

# 4

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]

plt.grid(True, color='red', alpha=0.9, linestyle='-')

ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1/5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(True, which='minor', alpha=0.8, linestyle=':', color='gray')

plt.xlim(-0.4, len(x) - 0.5)
plt.ylim(0, max(y) + 2)

bars = plt.bar(x, y, color='blue', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{height:.6f}', ha='center', va='bottom', fontsize=10)

plt.xlabel('Language')
plt.ylabel('Popularity')
plt.title('Пример столбчатой диаграммы')
plt.show()

# 5

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]

plt.grid(True, color='red', alpha=0.9, linestyle='-')

ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1/5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(True, which='minor', alpha=0.8, linestyle=':', color='gray')

num_bars = len(x)
center_index = (num_bars - 1) / 2
widths = [1 - abs(i - center_index) / center_index for i in range(num_bars)]

min_width = 0.1
max_width = 1
widths = [min_width + (max_width - min_width) * w for w in widths]

for i, (language, height, width) in enumerate(zip(x, y, widths)):
    plt.bar(i, height, width=width, color='blue', alpha=0.7)

plt.xticks(range(len(x)), x)
plt.xlim(0, len(x) - 0.5)
plt.ylim(0, max(y) + 2)

plt.xlabel('Language')
plt.ylabel('Popularity')
plt.title('Диаграмма с изменяющейся шириной столбиков')
plt.show()

# 6


x = ['G1', 'G2', 'G3', 'G4', 'G5']

women = [22, 29, 33, 30, 25]
men = [25, 32, 29, 35, 28]

bar_width = 0.35
x_pos = np.arange(len(x))

plt.bar(x_pos - bar_width/2, women, bar_width, label='Men', color='green', alpha=0.7)
plt.bar(x_pos + bar_width/2, men, bar_width, label='Women', color='red', alpha=0.7)

plt.xticks(x_pos, x)
plt.xlim(-0.5, len(x) - 0.5)
plt.ylim(0, max(max(men), max(women)) + 2)

plt.xlabel('Person')
plt.ylabel('Popularity')
plt.title('Scores by person')
plt.legend()
plt.show()

# 7

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]
explode = [0.1, 0, 0, 0, 0, 0]

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

plt.figure(figsize=(8, 8))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90,
        explode=explode, colors=colors, shadow=True,
        wedgeprops={'edgecolor': 'black', 'linewidth': 2})

plt.title('Popularity of Programming Languages', fontsize=16)
plt.axis('equal')
plt.show()

# 8

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [23, 17.5, 7, 6, 5, 4]
explode = [0.1, 0, 0, 0, 0, 0]

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90,
        explode=explode, colors=colors, shadow=True,
        wedgeprops={'edgecolor': 'black', 'linewidth': 2})

plt.title('Популярные языки программирования 2017 года, \n статистика использования по всему миру',
          fontsize=12, fontweight='bold', pad=20,
          bbox=dict(facecolor='gray', alpha=0.3, boxstyle='round,pad=0.5'))

plt.axis('equal')
ax = plt.gca()
ax.set_aspect(0.6)

plt.show()
