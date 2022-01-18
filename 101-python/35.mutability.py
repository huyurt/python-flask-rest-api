a = []
b = a
a.append(35)
print(id(a))
print(id(b))
print(a)
print(b)


c = 87
d = 87
print(id(c))
print(id(d))
c = 233
print(id(c))
print(id(d))


e = "hi"
f = e
print(id(e))
print(id(f))
e += " Hudayfe"
print(id(e))
print(id(f))
