l = ["Hudayfe", "Yurt"]
t = ("Hudayfe", "Yurt")
s = {"Hudayfe", "Yurt"}

print(l)
print(t)
print(s)

l[0] = "Yurt"
# t[1] = "Hudayfe" # 'tuple' object does not support item assignment
print(l[0])
print(t[0])

l.append("HY")
l.append("HY")
# t.append("HY") # 'tuple' object has no attribute 'append'
s.add("HY")
s.add("HY")
print(l)
print(s)

l.remove("HY")
print(l)

my_list = [10, 40, 50]
my_tuple = 99,

set1 = {5, 77, 9, 12, 0}
set2 = {5, 77, 9, 12}
diff = set1.intersection(set2)



