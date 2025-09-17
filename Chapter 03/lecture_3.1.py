'''Topic: Introduction to while loop'''

year = int(input("When did INDIA get its Independance (year): "))

if year == 1947:
    print("Hip Hip Hurray. You got that right!")
else:
    print("Comeon don't you know even this?")
    print("That ok, I will let you attempt this once more: ")

# I would like to write a piece of code, which lets the user attempt as many times as user wants
# The code will end, only when it get the right answer

print("To exit this please enter 1")
new_year = int(input("When did INDIA get its Independance (year): "))

while new_year != 1947:
    if new_year == 1:
        exit()
    print("you got this wrong.") 
    new_year = int(input("Enter once again: "))

print("Hip Hip Hurry. you got that right!")

