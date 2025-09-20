'''Topic: Introduction to "import library"'''

import math

print(math.log(10))
print(math.sqrt(23))
print(math.factorial(5))

import random

print(random.random())

# let us simulate a coin toss
a = random.random()

if (a<.5):
    print("Heads")
else: 
    print("Tails")

# let us simulate a coin toss
print(random.randrange(1,7))


