import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = []

for xi in x:
    inner = 1 / (1 + np.sin(xi) ** 2)

    base = 1 + np.tan(inner)

    log_arg = xi ** 2 + 1

    log_part = np.log(log_arg) / np.log(base)

    exp_part = np.exp(-abs(xi) / 10)

    y.append(log_part * exp_part)


plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(x=0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('График сложной функции')

plt.tight_layout()
plt.show()
