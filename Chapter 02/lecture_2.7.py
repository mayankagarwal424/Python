'''Topic: Introduction to the if Statement'''

birth_year = int(input("Enter your birth year: "))
current_year = 2025

age = current_year - birth_year

if (age < 13):
    print("Sorry!! You are under age, you can't watch this movie...")
    print("wait until you are old enough to watch this movie")
else:
    print("Enjoy Your Movie...")
    print("Don't forget to watch the sequels and prequels")

print("Have a nice time")

