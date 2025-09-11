# Topic: More on variables, opreators and expressions

# variables are case sensitive
roll = 5
ROLL = 50
Roll = 13
print(roll, ROLL, Roll)

# multiple assignment
d, c = 1,8                                            # here sequance is important
print(d, c)
x = y = z = 20
print(x, y, z)
s, t = 9,7
print(s, t)
s, t = t, s                                           # it's use to swap the two numbers
print(s, t)

# deleting a variable
b = 10
print(b)
del b
# print(b)                                            # this give error because b is not define due to delete then 

# shorthand operator's
count = 0
count = count + 1
count += 1                                            # here both statement do same work and can be use any airthmetic opreator (+,-,*,/,//,%,**)
print(count)

# in operater

print("alpha" in "A variable is a name can only contain alpha numeric characters and underscore")
print("Welcome" in "welcome back in python")          # here "in" operater find that 1st str is in 2nd str or not

# chaining opreater's
h = 6
print(2 < h < 10)                                     # here we use multiple opreater in one line
print(10 < h < 20)                                    # this concept is known as chaining              
print(4 < h * 4 < 50)
print(6 == h < 8)