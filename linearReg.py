from arrays import *
import matplotlib.pyplot as plt
from scipy import stats

slope, intercept, r, p, std_err = stats.linregress(dates[-30:], dayClose[-30:])

x = []
for idx, num in enumerate(dates[-30:]):
  x.append(idx)

def linear(x):
  return slope * x + intercept

mymodel = list(map(linear, x))

plt.scatter(x, dayClose[-30:])
plt.plot(x, mymodel)
plt.savefig("linear_reg.png")

