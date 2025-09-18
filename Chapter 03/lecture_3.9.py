'''Topic: Tutorial on for loop and difference between while loop and for loop'''

# 1st problem
num = int(input("Enter a number: "))
fact = 1

if (num < 0):
    print("Not define")

else:
    for i in range(num, 1, -1):
        fact *= i
    print(fact)

# 2nd problem
num_1 = abs(int(input("Enter a number: ")))
strnum_1 = str(num_1)
digit = 0

for c in strnum_1:
    digit += 1

print(digit)

# This not a ideal way to sole this problem, its only for knowing that, this problem can be solve using "forEach"