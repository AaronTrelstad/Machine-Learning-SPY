from arrays import *
import numpy as np
import matplotlib.pyplot as plt

days = 200

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

n = 10
mymodel = np.poly1d(np.polyfit(x[-days:], dayVolume[-days:], n))

plt.scatter(x[-days:], dayVolume[-days:])
plt.plot(x[-days:], mymodel(x[-days:]))
plt.savefig("poly_regDayVolume(10).png")
