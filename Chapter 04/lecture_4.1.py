'''Topic: Warmup with Lists'''

l =[]

l.append(1)
l.append(2)
l.append(3)

print(l)

x = []

x.append(l)
print(x)

m = [10, 60, 32]

x.append(m)
print(x)

t = []

t.append(x)
print(t)

t.append([100, 102, 104])
print(t)

print(t[0])
print(t[1])

# treat a matrix
# let a matrix m

m = []

m.append([1,2,3])
m.append([7,6,8])
m.append([4,5,9])

print(m)
print(m[0])
print(m[1][1])
print(m[1][0])
print(m[1][2])