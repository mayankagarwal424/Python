# print("Namastey youtube We are learning python")

'''Variable'''
# sher = "Mayank Agarwal"

# SheriansSchool = "student"      #pascal case
# sheryiansSchool = "Students"    #camel case
# sheryians_school = "students"    #snake case

'''Data types'''
# a = -34          #integer
# b = 45.3         #float
# c = 15/5         #float

# v = 34j          #j is using for imaginary value only j is use for imaginary value other letter gives error

# st = "1234567890 dasdrdnjd !@#$%^&*"        #string
# print(type(st))

# b = True                       #boolean
# f = False                      #boolean have either True value or False value (make sure "T" & "F" should be capital)
# print(type(b))

'''Strings'''
'''string Sliceing syntax  st[Start: Stop: Step]'''

# a = "Sher coders"

# print(a[5::1])                   #print "coder"
# print(a[:4:1])                   #print "Sher"
# print(a[::])                     #print complete string

'''Format printing'''
# name = input("Enter your name: ")
# age = int(input("Enter your age: ")

# print(f"Hello {name}, Happy to know you are {age} year old")

'''Opreation'''
'''Arithmetic opretors'''
# a = 4
# b = 32

# print(a + b)          #provide addition
# print(a - b)          #provide substraction
# print(a * b)          #provide multiplication
# print(b / a)          #provide divition
# print(b // a)         #provide diviser part after devision
# print(a ** b)         #provide a ki power b
# print(b % a)          #provide remider part after division

# print(12 + 4 / 2)     #python is also follow 'BODMAS' rule

'''Assignment opreator'''

# a = 23                #23 is assign to a

'''Compound assignment opreation'''

#a = 20

# a += 20
# a += 25 
# a += 30      

# print(a)               #It can also written as like that
# a -=
# a *=
# a /=
# a **= 

'''Comparison opreator'''

# a = 13.5
# b = 13

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(45 <= 67)
# print(23 >= 43)

# print(ord("A"))
# print(ord("B"))

# print("A" > "B")					#provide False because A = 65 and B = 66
# print("ABC" < "AND")

# print("A" > 34) 					#we can not do this only string to string comparision is allowed

'''Logical opreator'''

# print(12 > 20 and 125 > 110 and 34 ==34 and 46 < 93)				#if all condition is true then only provide "True" answer will be "False"

# print(12 != 12 or 23 == 49 or 10 > 5) 			#if one condition is true provide "True" answer will be "True"

# print(not 12 == 12)					#not reverse the condition answer will be "False"

'''Conditional Statement(if-else)'''

# a = 8

# if a > 10:
# 	print("I will do task A")

# else:
# 	print("I will do task B)

## example
# money = int(input("Please provide me the money: "))

# if money == 10:
# 	print("I will have a choco bar icecream")

# elif money  == 20:
# 	print("I have a mango dolly ieccream")

# else:
# 	print("I hae a cone icecream")
            
'''Some problems based on conditional statement'''

##Problem 1
# num1 = int(input("Enter your 1st number: "))
# num2 = int(input("Enter your 2nd number: "))

# if num1 > num2:
# 	print(f"{num1} is graeter than {num2}")

# elif num2 > num1:
# 	print(f"{num2} is grater than {num1}")

# else:
# 	print("Both number are equal")

##Problem 2
# gen = input("Enter your sex: ")

# if gen == "Male" or gen == "male":
# 	print("Good morning Sir")

# elif gen == "Female" or gen == "female":
# 	print("Good morning ma'an")
	
# else: 
# 	print("Unidentified gender")

##Problem 3
# num = int(input("Enter a number: "))

# if num % 2 == 0:
# 	print(f"{num} is an even number")	

# else:
# 	print(f"{num} is an odd number")

##Problem 4
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# if age >= 18:
# 	print(f"Hello {name} you are a valid voter")

# else:
# 	print(f"Hello {name} you are not a vaild voter")

'''For Loop'''

## lets print a table of 5
# n = int(input("which table you want? "))

# for i in range(n, n * 10 + 1, n):
# 	print(i)

# a = "Mayank is a good guy"

# for i in range(len(a)):
# 	print(i)

# b = "Mayank is a Data Scientist"

# for i in b:
# 	print(i)

# for i in range(1, 21):
# 	if i == 15:
# 		print("break statement is executed")
# 		break
# 	print(i)
	
# else:
# 	print("break statement is not executed")

'''Some problems on For loop'''

## Problem 1
# num = int(input("Enter a number: "))

# for i in range(num):
# 	print("Hello World")

## Problem 2
# n = int(input("Enter a number: "))

# for i in range(1, n+1):
# 	print(i)

## Problem 3
# num = int(input("Enter a number: "))

# for i in range(n, 0, -1):
# 	print(i)

## Problem 4
# num = int(input("Which table you want: ")

# for i in range(1, 11):
# 	print(f"{num} X {i} = {num * i}")

## Problem 5
# n = int(input("Enter a number: "))
# sum = 0

# for i in range(num + 1):
# 	sum += i

# print(sum)

## Problem 6
# n = int(input("Which number of Factorial you want? "))
# fact = 1

# if num == 0 or num == 1:
# 	print(f"The Factorial of {n} is {fact}")

# else:
# 	for i in range(1, n + 1):
# 		fact *= i

# print(f"The Factorial of {n} is {fact}")

##Problem 7
# num = int(input("Tell me a number: "))
# even = 0
# odd = 0

# for i in range(num + 1):
# 	if i % 2 == 0:
# 		even += i

# 	else: 
# 		odd += i

# print(f"Your even and odd sum is {even} and {odd}")

## Problem 8
# num = int(input("Which number factors you want: "))

# for i in range(1, n + 1):
# 	if n % i == 0:
# 		print(i)

## Problem 9
# num = int(input("Which number factors you want: "))
# sum = 0

# for i in range(1, n + 1):
# 	if n % i == 0:
# 		sum += i

# if sum == num:
# 	print(f"{num} is a perfect number")

# else:
# 	print(f"{num} is not a perfect number")
