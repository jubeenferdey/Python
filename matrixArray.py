# declare a 10x1 matrix and implement the following
#           5x + 6y = z
# where, x,y,z are 10 X 1 matrices.
a = [10,10,10,10,10,10,10,10,10,10]
b = [10,10,10,10,10,10,10,10,10,10]
for i in range(0,10):
    a[i] = a[i] * 5
    b[i] = b[i] * 6
    #110 should come.
    print(a[i] + b[i])