import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

x = sorted([1234, 221, 765, 124, 2312, 890])
idx = np.arange(len(x))
plt.barh(idx, x)
plt.show()