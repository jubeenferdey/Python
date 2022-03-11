# # # declare a 10x1 matrix and implement the following
# # #           5x + 6y = z
# # # where, x,y,z are 10 X 1 matrices.
# # import array as arr
# a = [10,10,10,10,10,10,10,10,10,10]
# b = [10,10,10,10,10,10,10,10,10,10]
# c = []
# for i in range(0,10):
#     a[i] = a[i] * 5
#     b[i] = b[i] * 6

#     #110 should come.
#     c.append(a[i] + b[i])  
# print(c)

import array as array
array.matrix = [10,10,10,10,10,10,10,10,10,10]
array.result = []

for i in range(0,10):
    array.result.append( (array.matrix[i]*5) + (array.matrix[i]*6) )

print(array.result)