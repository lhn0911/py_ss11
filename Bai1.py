
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x**2 + 2*x

plt.plot(x, y, label='y = x² + 2x', color='blue')

plt.title('Biểu đồ đầu tay của Hiếu')

plt.xlabel('Trục x')
plt.ylabel('Trục y')

plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
