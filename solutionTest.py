import numpy as np
import sys

print(sys.argv[1])
print(sys.argv[2])
numberList = list(map(int, sys.argv[1].strip('[]').split(',')))
targetNumber = int(sys.argv[2])
print(numberList)
print(targetNumber)
lengthList = len(numberList)
result = []
auxiliar = np.zeros((lengthList, lengthList))
for idx, x in enumerate(numberList):
  auxiliar2 = False
  for idy, y in enumerate(numberList):
    if idy > idx and x + y == targetNumber: 
      for idx2 in range(idx):
        if idy > idx2 and auxiliar[idx2, idy] == True:
          auxiliar2 = True
      if auxiliar2 != True:
        auxiliar[idx, idy] = True
        result.append((x,y))
        continue
print(result)