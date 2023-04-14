from arrays import *
import matplotlib.pyplot as plt

plt.scatter(dates[-30:], percentChange[-30:])
plt.savefig("scatterPercentChange30.png")