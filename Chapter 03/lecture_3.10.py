'''Topic: Nested for loop'''

s = "VIBGYOR"
t = "VIBGYOR"
count  = 0

for i in range(7):
    for j in range(7):
        print(i, j, s[i], s[j])
        count += 1

print("The total way in which the two brothers can wear 7 different colors:", count)

# i = 0 and j = 0 print V V
# i = 0 and j = 1 print V I
# i = 0 and j = 2 print V B
# ........
# ........
# i = 0 and j = 6 print V R
# i = 1 and j = 0 print I V 
# ........ and so on.......