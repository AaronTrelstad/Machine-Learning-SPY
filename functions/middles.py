import numpy as np
from arrays import *

## 1 year average
averageClose = np.mean(dayClose)
averageOpen = np.mean(dayOpen)
averageHigh = np.mean(dayHigh)
averageLow = np.mean(dayLow)
averageVolume = np.mean(dayVolume)
averagePercentChange = np.mean(percentChange)

## 60 day averege
averageClose60 = np.mean(dayClose[-60:])
averageOpen60 = np.mean(dayOpen[-60:])
averageHigh60 = np.mean(dayHigh[-60:])
averageLow60 = np.mean(dayLow[-60:])
averageVolume60 = np.mean(dayVolume[-60:])
averagePercentChange60 = np.mean(percentChange[-60:])

## 30 day average
averageClose60 = np.mean(dayClose[-30:])
averageOpen60 = np.mean(dayOpen[-30:])
averageHigh60 = np.mean(dayHigh[-30:])
averageLow60 = np.mean(dayLow[-30:])
averageVolume60 = np.mean(dayVolume[-30:])
averagePercentChange60 = np.mean(percentChange[-30:])

## 1 year median
medianClose = np.median(sorted(dayClose))
medianOpen = np.median(sorted(dayOpen))
medianHigh = np.median(sorted(dayHigh))
meadianLow = np.median(sorted(dayLow))
medianVolume = np.median(sorted(dayVolume))
medianPercentChange = np.median(sorted(percentChange))

## 60 day median
medianClose = np.median(sorted(dayClose[-60:]))
medianOpen = np.median(sorted(dayOpen[-60:]))
medianHigh = np.median(sorted(dayHigh[-60:]))
meadianLow = np.median(sorted(dayLow[-60:]))
medianVolume = np.median(sorted(dayVolume[-60:]))
medianPercentChange = np.median(sorted(percentChange[-60:]))

## 30 day median 
medianClose = np.median(sorted(dayClose[-30:]))
medianOpen = np.median(sorted(dayOpen[-30:]))
medianHigh = np.median(sorted(dayHigh[-30:]))
meadianLow = np.median(sorted(dayLow[-30:]))
medianVolume = np.median(sorted(dayVolume[-30:]))
medianPercentChange = np.median(sorted(percentChange[-30:]))
