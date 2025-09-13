#introduction of while loop

print("When did India get its independence (year)? ")
year = int(input())

if year == 1947:
    print("Hip Hip Hurray. You got that right!")
else:
    print("Comeon, dont you know even this?")

#I would like to write a piece of code, which  lets the user attempt as many time as he wants.
#The code will end, only when it gets the right answer.

print("When did India get its independence (year)?")
year = int(input())

while year != 1947:
    print("you got this wrong. Enter once again.")
    year = int(input())

print("Wowwwww... you got it right! 1947.")