from arrays import *
import numpy as np
import matplotlib.pyplot as plt

days = 150

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

n = 2
mymodel = np.poly1d(np.polyfit(x[-days:], dayOpen[-days:], n))

plt.scatter(x[-days:], dayOpen[-days:])
plt.plot(x[-days:], mymodel(x[-days:]))
plt.savefig("poly_regDayOpen(2).png")
