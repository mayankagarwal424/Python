'''Topic: for loop for multiplication tables'''

n = int(input("Enter a number: "))

for i in range(1,11):
    tab = i * n

    print(f"{n} X {i} = {tab}")
