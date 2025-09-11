# Topic: Tutorial on if, else and elif conditions

# problem 1
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(num, "is even number")
else:
    print(num, "is a odd number")

# problem 2
num1 = int(input("Enter a number: "))

rem = num1 % 10

if(rem == 0):
    print(num1, "is end with 0")
elif(rem == 5):
    print(num1, "is end with 5")
else:
    print(num1, "is not end with 0 or 5")

# problem 3
mark = int(input("Enter your marks : "))

if(mark < 0 or mark > 100):
    print("invalid input")
elif(mark >= 90):
    print("A")
elif(mark >= 80):
    print("B")
elif(mark >= 70):
    print("C")
elif(mark >= 60):
    print("D") 
else:
    print("E")