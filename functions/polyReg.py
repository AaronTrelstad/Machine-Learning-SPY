from arrays import *
import numpy as np
import matplotlib.pyplot as plt

days = 30
myline = np.linspace(dates[-days], len(dates), 100)

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

n = 3
mymodel = np.poly1d(np.polyfit(x[-days:], dayClose[-days:], n))

plt.scatter(x[-days:], dayClose[-days:])
plt.plot(myline, mymodel(myline))
plt.savefig("poly_reg30Close.png")
