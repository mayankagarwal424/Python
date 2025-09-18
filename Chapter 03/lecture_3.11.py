'''Topic: Tutorail on nested loops'''

# 1st Problem (Find all prime numbers less than the entered number?)
num = int(input("Enter a number: "))

if num > 2:
    print(2, end = " ")

for i in range(3, num):
    flag = False
    for j in range(2, i):
        if i % j == 0 :
            flag = False
            break
        else:
            flag = True

    if flag :
        print(i, end = " ")

# 2nd problem (Find the total profit/loss of each trader working in a trading firm. Information regarding number of traders and number of transactions is unknown.)

emp_id = input("Enter the empolyee ID: ")
while (emp_id != "-1"):
    trade = int(input("Enter the trade ammount: "))
    profit_loss = 0
    while (trade != 0):
        profit_loss += trade
        trade = int(input("Enter the trade amount: "))
    print(f"Profit/loss for employee {emp_id} is {profit_loss}")
    emp_id = input("Enter the empolyee ID: ")

# 3rd problem (Find the day wise total rainfall for the entered duration of time e.g. week, month, etc.)

day = int(input("Enter the number of days: "))

for i in range(1, day + 1):
    total = 0
    rainfall = int(input("Enter the rainfall: "))

    while (rainfall != -1):
        total += rainfall 
        rainfall = int(input("Enter the rainfall: "))

    print(f"total rainfall for day {i} is {total}")

# 4th problem (Find the length of longest word from the set of words entered by the user)

str = input("Enter a string: ")
long = 0

while(str != "-1"):
    count = 0

    for l in str:
        count += 1

    if count > long:
        long = count
    str = input("Enter a string: ")

print("The length of longest word is",long)