import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y, label="y = sin(x)", color='blue')

x_point = np.pi / 2
y_point = np.sin(x_point)

ax.annotate(
    "Điểm cực đại\n(x = π/2)",
    xy=(x_point, y_point),
    xytext=(x_point + 0.5, y_point + 0.5),
    arrowprops=dict(arrowstyle="->", lw=1.5)
)

ax.set_title("Đồ thị y = sin(x) với chú thích")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")

plt.show()
