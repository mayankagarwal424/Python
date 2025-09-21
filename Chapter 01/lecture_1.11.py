'''Topic: More on Strings'''

# Replication in string
s = "good"
print(s*5)
print(s[1]*5)

# Comparision of string
x = "India"
print(x == "India")
print(x == "india")

# 3rd program
print("apple" > "one")
print("four" < "ten")            #Here String compare charcter-by-charcter.

print("ab" < "az")
print("abcdef" < "abcde")        #Here Starting 5 letter's are same then 6th letter is always greater the to nothing. 

# Negative Indexing
y = 'python'
print(y[-1])
print(y[-2])
print(y[-3])
print(y[-4])
print(y[-5])
print(y[-6])

# find the length of string
z = "jnvbrhibcwhbciebcicihcouwejvnwcc"
print(len(z))

print(z[31])
