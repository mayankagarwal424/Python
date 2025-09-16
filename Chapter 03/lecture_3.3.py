# Topic: Tutorial on while loop

# 1st Problem
num = int(input("Enter a number: "))
fact = 1

if num < 0 :
    print("Not define")
else:
    while num > 0:
        fact *= num
        num -= 1

    print(fact)

# 2nd Problem
num_1 = abs(int(input("Enter a number: ")))
digits = 1

while(num_1 > 9):
    num_1 //= 10
    digits += 1

print(digits)

# 3rd Problem
num_2 = int(input("Enter a number: "))
rev = 0
abs_num = abs(num_2)

while(abs_num > 0):
    rev = rev*10 + (abs_num % 10)
    abs_num //= 10

if (num_2 < 0):
    rev = (rev - 2*rev)

print(rev)

# 4th Problem
num_3 = int(input("Enter a number: "))
rev_1 = 0
abs_num_1 = abs(num_3)

while(abs_num_1 > 0):
    rev_1 = rev_1*10 + (abs_num_1 % 10)
    abs_num_1 //= 10

if (num_3 < 0):
    rev_1 = (rev_1 - 2*rev_1)

if (num_3 == rev_1):
    print("Palindrome")
else:
    print("Not a Palindrome")