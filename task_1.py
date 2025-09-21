import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1

x = [0, 50]
y = [0, 140]

plt.figure(figsize=(8, 8))
plt.plot(x, y, linewidth=3, color='blue')

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

plt.yticks(range(0, 161, 20))
plt.xticks(range(0, 51, 10))

plt.xlim(0, 50)
plt.ylim(0, 140)

plt.show()

# 2

plt.figure(figsize=(8, 8))

x_blue = [10, 20, 30]
y_blue = [20, 40, 10]
plt.plot(x_blue, y_blue, 'b-', linewidth=2, label='Синий график')

x_red = [10, 20, 30]
y_red = [40, 10, 30]
plt.plot(x_red, y_red, 'r-', linewidth=2, label='Красный график')

plt.xlim(10, 30)
plt.ylim(10, 40)
plt.xticks(range(10, 31, 5))
plt.yticks(range(10, 41, 5))

plt.title('Два графика с заданными точками', fontsize=14)
plt.legend()

plt.tight_layout()
plt.show()

#3

plt.figure(figsize=(8, 8))

x_blue = [10, 20, 30]
y_blue = [20, 40, 10]
plt.plot(x_blue, y_blue, ':', linewidth=3, color='blue', label='Синий график')

x_red = [10, 20, 30]
y_red = [40, 10, 30]
plt.plot(x_red, y_red, '--', linewidth=3, color='red', label='Красный график')

plt.xlim(10, 30)
plt.ylim(10, 40)
plt.xticks(range(10, 31, 5))
plt.yticks(range(10, 41, 5))

plt.title('Два графика с заданными точками', fontsize=14)
plt.legend()

plt.tight_layout()
plt.show()

#4

plt.figure(figsize=(8, 8))

x_red = [1, 4, 5, 6, 7]
y_red = [2, 6, 3, 6, 3]
plt.plot(x_red, y_red, '-.', linewidth=3, color='red', label='Красный график',
         marker='o',
         markersize=10,
         markerfacecolor='blue',
         markeredgecolor='black',
         markeredgewidth=2)


plt.xlim(1, 8)
plt.ylim(1, 8)
plt.xticks(range(1, 9, 1))
plt.yticks(range(1, 9, 1))

plt.title('График с вершинами', fontsize=14)
plt.legend()

plt.tight_layout()
plt.show()

#5

plt.figure(figsize=(8, 8))

x_red = [2, 3, 3, 4, 5, 6, 6, 7, 8 , 9]
y_red = [1, 2, 5, 6, 10, 11, 18, 20, 20, 22]
for i, (x, y) in enumerate(zip(x_red, y_red)):
    if i % 2 == 0:
        plt.plot(x, y, marker='*', markersize=15,
                 markerfacecolor='blue', markeredgecolor='black',
                 markeredgewidth=1, linestyle='none')
    else:
        plt.plot(x, y, marker='o', markersize=12,
                 markerfacecolor='red', markeredgecolor='black',
                 markeredgewidth=2, linestyle='none')


plt.xlim(1, 8)
plt.ylim(1, 8)
plt.xticks(range(0, 11, 2))
plt.yticks(range(0, 31, 5))

plt.title('График с вершинами: кружочки и звездочки', fontsize=14)

plt.tight_layout()
plt.show()

# 6

dates = pd.date_range('2016-10-03', periods=5, freq='D')
values = [772.5, 776.4, 776.5, 776.9, 775.1]

plt.figure(figsize=(10, 6))

plt.plot(dates, values, 'r-o', linewidth=2, markersize=8, markerfacecolor='red', markeredgecolor='black')

plt.xlim(dates[0], dates[-1])
plt.ylim(772.5, 777.0)

plt.grid(True, color='red', alpha=0.9, linestyle='-')
plt.xticks(dates)
plt.yticks(np.arange(772.5, 777.5, 0.5))

ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(1/5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.grid(True, which='minor', alpha=0.8, linestyle=':', color='gray')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
