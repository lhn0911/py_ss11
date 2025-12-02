import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 51, 100)
y = np.random.randint(0, 51, 100)

plt.scatter(x, y)

plt.title("Scatter Plot Ngẫu Nhiên")
plt.xlabel("Giá trị X")
plt.ylabel("Giá trị Y")

plt.show()
