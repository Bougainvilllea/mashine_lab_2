import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(14, 10))

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

ax.axhline(y=0, color='black', linewidth=1.5)  # Ось OX
ax.axvline(x=0, color='black', linewidth=1.5)  # Ось OY

ax.plot(x, y1, 'b-', label='График 1 (sin(x))', linewidth=2)
ax.plot(x, y2, 'r-', label='График 2 (cos(x))', linewidth=2)

x_points = np.array([2, 4, 6, 8])
y_points = np.sin(x_points)
ax.scatter(x_points, y_points, color='green', s=80, zorder=5, label='Маркеры')

major_xticks = np.arange(0, 11, 2)
major_yticks = np.arange(-1, 1.5, 0.5)
ax.set_xticks(major_xticks)
ax.set_yticks(major_yticks)

minor_xticks = np.arange(0, 11, 1)
minor_yticks = np.arange(-1, 1.5, 0.25)
ax.set_xticks(minor_xticks, minor=True)
ax.set_yticks(minor_yticks, minor=True)

ax.tick_params(axis='both', which='major', labelsize=10)

for tick in minor_xticks:
    if tick not in major_xticks:
        ax.text(tick, -0.05, f'{tick}', ha='center', va='top',
                fontsize=8, color='blue', alpha=0.7)

for tick in minor_yticks:
    if tick not in major_yticks:
        ax.text(-0.05, tick, f'{tick:.2f}', ha='right', va='center',
                fontsize=8, color='blue', alpha=0.7)

ax.set_xlabel('Ось OX', fontsize=12, color='blue', fontweight='bold')
ax.set_ylabel('Ось OY', fontsize=12, color='blue', fontweight='bold')

ax.set_title('График с подписями', fontsize=16, pad=20, fontweight='bold')

ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

ax.grid(True, which='major', linestyle='-', alpha=0.7, linewidth=1)
ax.grid(True, which='minor', linestyle=':', alpha=0.4, linewidth=0.5)

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-1.2, 1.2)

plt.tight_layout()
plt.show()
