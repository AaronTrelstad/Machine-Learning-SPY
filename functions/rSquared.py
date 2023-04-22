from arrays import *
import numpy as np
from sklearn.metrics import r2_score

days = 30

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

## x is used when comparing to the date
n = 3
mymodel = np.poly1d(np.polyfit(dayVolume[-days:], percentChange[-days:], n))

print(r2_score(percentChange[-days:], mymodel(dayVolume[-days:])))