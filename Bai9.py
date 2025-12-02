import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(start="2025-12-01", periods=30, freq='D')
temperature = np.random.normal(loc=20, scale=3, size=30)

temperature[[5, 15, 25]] += [10, -8, 12]
z = np.polyfit(range(len(temperature)), temperature, 1)
trend = np.polyval(z, range(len(temperature)))

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, temperature, label="Nhiệt độ hàng ngày", color='blue', marker='o')
ax.plot(dates, trend, label="Trendline", color='red', linestyle='--')

spike_indices = [5, 15, 25]
ax.scatter(dates[spike_indices], temperature[spike_indices],
           color='orange', s=100, label="Spike")

special_dates = [dates[0], dates[14], dates[29]]
for d in special_dates:
    ax.axvline(d, color='green', linestyle=':', alpha=0.7)
    ax.text(d, ax.get_ylim()[1], d.strftime('%d-%b'),
            rotation=90, verticalalignment='top', color='green')


ax.set_title("Biểu đồ nhiệt độ hàng ngày trong tháng với trendline và spikes")
ax.set_xlabel("Ngày")
ax.set_ylabel("Nhiệt độ (°C)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
