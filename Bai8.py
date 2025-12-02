import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 200)

fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))

ax.set_title("Đồ thị động y = sin(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")


def update(frame):
    y = np.sin(x + frame * 0.1)
    line.set_ydata(y)
    return line,


ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
