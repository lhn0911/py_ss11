import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2

sx = np.random.randint(0, 50, 100)
sy = np.random.randint(0, 50, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title("Lineplot: y = x")

axs[1, 0].plot(x, y2, color='green')
axs[1, 0].set_title("Lineplot: y = x²")

axs[0, 1].scatter(sx, sy, color='red')
axs[0, 1].set_title("Scatterplot 1")

sx2 = np.random.randint(0, 50, 100)
sy2 = np.random.randint(0, 50, 100)
axs[1, 1].scatter(sx2, sy2, color='purple')
axs[1, 1].set_title("Scatterplot 2")

plt.tight_layout()

plt.show()
