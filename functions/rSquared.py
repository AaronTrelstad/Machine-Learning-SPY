from arrays import *
import numpy as np
from sklearn.metrics import r2_score

days = 30

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

## x is used when comparing to the date

mymodel = np.poly1d(np.polyfit(dayVolume[-days:], dayClose[-days:], 3))

print(r2_score(dayClose[-30:], mymodel(dayVolume[-30:])))