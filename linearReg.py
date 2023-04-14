from arrays import *
import matplotlib.pyplot as plt
from scipy import stats

days = 30

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

slope, intercept, r, p, std_err = stats.linregress(x[-days:], percentChange[-days:])

def linear(x):
  return slope * x + intercept

mymodel = list(map(linear, x[-days:]))

plt.scatter(x[-days:], percentChange[-days:])
plt.plot(x[-days:], mymodel)
plt.savefig("percentChange30.png")

