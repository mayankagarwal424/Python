'''Topic: break, continue and pass'''

# break
email_id = input("Enter your email ID : ")

for i in email_id:

    if i == "@":
        break

    print(i, end = "")

# continue
for x in email_id:

    if x == "@":
        print("")
        continue

    print(x, end = "")

# pass
for y in range(11):

    if(y % 3 == 0):
        print(y)

    else:
        pass