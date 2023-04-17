import csv

with open('oneyear.csv') as f:
    reader = csv.reader(f)
    spy = list(reader)

dates = []
dayClose = []
dayOpen = []
dayHigh = []
dayLow = []
dayVolume = []
percentChange = []

for i in range(0, len(spy)):
    dates.append(spy[i][0])
    dayClose.append(float(spy[i][1]))
    dayOpen.append(float(spy[i][2]))
    dayHigh.append(float(spy[i][3]))
    dayLow.append(float(spy[i][4]))
    dayVolume.append(float(spy[i][5]))
    percentChange.append(float(spy[i][6]))


