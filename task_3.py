import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))

x3 = np.linspace(-3, 4, 400)
y3 = x3**2 - x3 - 6

ax.plot(x3, y3, 'b-', linewidth=2, label='$y(x) = x^2 - x - 6$')
ax.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
ax.axvline(x=0, color='black', linewidth=0.5, linestyle='--')
ax.grid(True, alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('y(x)')
ax.set_title('y(x) = x^2 - x - 6')

root1 = -2
root2 = 3
ax.plot(root1, 0, 'ro', markersize=8, label=f'Корень: x = {root1}')
ax.plot(root2, 0, 'go', markersize=8, label=f'Корень: x = {root2}')
ax.legend()

plt.tight_layout()
plt.show()
