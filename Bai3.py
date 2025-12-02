import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor='black')
ax.set_title("Histogram phân phối chuẩn")
ax.set_xlabel("Giá trị")
ax.set_ylabel("Tần suất")

plt.show()
