from arrays import *
import numpy as np
import matplotlib.pyplot as plt

days = 30

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

n = 3
mymodel = np.poly1d(np.polyfit(x[-days:], percentChange[-days:], n))

plt.scatter(x[-days:], percentChange[-days:])
plt.plot(x[-days:], mymodel(x[-days:]))
plt.savefig("poly_reg30PercentChange.png")
