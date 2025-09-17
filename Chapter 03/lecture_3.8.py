'''Topic: Formatted Printing'''

# 1st Type
for x in range(10):
    print(x, end = " ")

# 2nd type
d, m, y = 10, 5, 2021

print("\nToday's date is ", d, m, y)
#we can print date like that but we are using "- or /" symbol's in date
#that have "sep" in print function th seprated after ",". so we can print date as

print("Today's date is", d, m, y, sep = "/")
#but there is an small error that it give / after is, so we can write as

print("Today's date is: ", end = " ")
print(d, m, y, sep = "/")

# 3rd Type
num = int(input("Enter a number: "))
for i in range(1, 11):
    # print(num, "x", i, "=", num * i)  
    # It is a format which we use in previous lecture's

    # Now from here we use "f" where "f" stands for formatted printing
    # the syntax of formatted print is '''print(f"{var1} {var2})''' just like that 
    print(f"{num} X {i} = {num*i}")

    #  this formatting can also achived by using ".format()" like that
    print("{0} X {1} = {2}" .format(num, i, num*i))

    # print using "string modulo opreator"
    print("%d X %d = %d" % (num, i, num*i))

# Now let see why the formatted printing is important
# let We want to output only two digits after decimal

pi = 22 / 7 
print(f"Value of PI = {pi : .2f}")  
print(f"Value of PI = {pi : .3f}")
print(f"Value of PI = {pi : .4f}")