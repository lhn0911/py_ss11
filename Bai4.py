import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)

y1 = x
y2 = x**2
y3 = x**3

plt.plot(x, y1, label='y = x', color='red')
plt.plot(x, y2, label='y = x²', color='green')
plt.plot(x, y3, label='y = x³', color='blue')

plt.title("Biểu đồ các hàm số")
plt.xlabel("Trục x")
plt.ylabel("Trục y")

plt.legend()

plt.show()
