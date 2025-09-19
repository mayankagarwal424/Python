'''Topic: Naive Search in a list'''

from random import *

l = []
flag = 0
a = int(input("Enter a number: "))

for i in range(1000000):
    l.append(randrange(1,200))

for j in range(len(l)-1):
    if (l[j] == a):
        print(f"{a} found at position {j+1} in list")
        flag = 1
        break

if(flag == 0):
    print(f"{a} is not found at any position in list")

