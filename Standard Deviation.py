import math
n = int(input("Enter the Number of Values: "))
weight = []
s = 0
for i in range(n):
    w = int(input("Enter the Weight: "))
    weight.append(w)
    s = s + w 
    print(weight)
average = int(s/n)
d = 0
for i in range(n):
    d = (weight[i] - average) * (weight[i] - average)
sd = math.sqrt(d)
print("The Standard Deviation is: ",sd)

    
    