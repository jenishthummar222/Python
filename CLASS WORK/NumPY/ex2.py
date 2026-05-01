l1 = [85,22,92,6]
l2 = [i+5 for i in l1]

print(l1)
print(l2)

import numpy as np

arr = np.array([85,22,92,6])

print(arr)
print(arr + 5)      # no need of loop is faster than list, it fix value not add on array.