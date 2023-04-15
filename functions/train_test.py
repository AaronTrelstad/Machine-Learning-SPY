from arrays import *
import numpy as np
import matplotlib.pyplot as plt

##80% train 20% test

days = 100

x = []
for idx, num in enumerate(dates):
  x.append(idx + 1)

x = x[-days:]
dayClose = dayClose[-days:]

train_x = x[:80]
train_y = dayClose[:80]

test_x = x[80:]
test_y = dayClose[80:]

plt.scatter(train_x, train_y)
plt.savefig("train.png")