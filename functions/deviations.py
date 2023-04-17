import numpy as np
from arrays import *

deviationClose = np.std(dayClose)
deviationOpen = np.std(dayOpen)
deviationHigh = np.std(dayHigh)
deviationLow = np.std(dayLow)
deviationVolume = np.std(dayVolume)
deviationPercentChange = np.std(percentChange)

## 60 day averege
deviationClose60 = np.std(dayClose[-60:])
deviationOpen60 = np.std(dayOpen[-60:])
deviationHigh60 = np.std(dayHigh[-60:])
deviationLow60 = np.std(dayLow[-60:])
deviationVolume60 = np.std(dayVolume[-60:])
deviationPercentChange60 = np.std(percentChange[-60:])

## 30 day deviation
deviationClose30 = np.std(dayClose[-30:])
deviationOpen30 = np.std(dayOpen[-30:])
deviationHigh30 = np.std(dayHigh[-30:])
deviationLow30 = np.std(dayLow[-30:])
deviationVolume30 = np.std(dayVolume[-30:])
deviationPercentChange30 = np.std(percentChange[-30:])
 