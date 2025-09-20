'''Topic: An Interesting Cipher; More on String''' 

alpha = "abcdefghijklmnopqrstvwxyz"
i = 10

print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])

i = 28

print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26]) 

# 2nd Program

name = "omkar"
# we wish to print extra 1 letter, expected output "pnlbs"
t = ""
# to store the new String

j = 0   #store name index
k = 1   #store jump step

t += alpha[((alpha.index(name[j]) + k) % 26)]
t += alpha[((alpha.index(name[j+1]) + k) % 26)]
t += alpha[((alpha.index(name[j+2]) + k) % 26)]
t += alpha[((alpha.index(name[j+3]) + k) % 26)]
t += alpha[((alpha.index(name[j+4]) + k) % 26)]


print(t)
