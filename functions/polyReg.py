from arrays import *
import numpy as np
import matplotlib.pyplot as plt

days = 200

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

n = 3
mymodel = np.poly1d(np.polyfit(x[-days:], dayClose[-days:], n))

plt.scatter(x[-days:], dayClose[-days:])
plt.plot(x[-days:], mymodel(x[-days:]))
plt.savefig("poly_regDayClose.png")
