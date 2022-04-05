import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("The Array, before Dequeing: \t\t ", arr)
print("---------------------------------------")
#arr = np.delete(arr,0)
for i in range(0,len(arr)):
    print("The Element to be popped: ",arr[0])
    arr = np.delete(arr,0)
    print("Array after Dequeing the First Element: ",arr)
