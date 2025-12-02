import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))

sns.heatmap(
    data,
    cmap="viridis",
    annot=True,
    fmt=".2f",
    linewidths=0.5,
    cbar=True
)

plt.title("Heatmap từ ma trận dữ liệu ngẫu nhiên")
plt.xlabel("Cột")
plt.ylabel("Hàng")

plt.show()
