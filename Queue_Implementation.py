import numpy as np

arr = np.array([1, 2, 3, 4, 5])
#arr = np.delete(arr,0)
for i in range(0,len(arr)):
    print(arr[0])
    arr = np.delete(arr,0)
    print(arr)
    
