'''Topic: Birthday Paradox'''

import random

l = []

l.append(random.randrange(1, 10))
print(l)

l.append(random.randrange(1, 10))
print(l)

# Birthday Paradox

b_day = []                 
#create an empty list

for i in range(30):
    b_day.append(random.randint(1, 365))
    # append random number between 1 to 365
    # append 30 of them

b_day.sort()
print(b_day)

j = 0
flag = 0

while(j < len(b_day)-1):
    if (b_day[j] == b_day[j+1]):
        print("Repeat's", b_day[j], b_day[j+1])
        flag = 1
        break
    j += 1

if flag == 0 :
    print("There is no repitation")