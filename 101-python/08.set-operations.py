names_1 = {"Hudayfe", "Yurt", "HY"}
names_2 = {"Yurt", "Hudayfe"}

dif_1 = names_1.difference(names_2)
dif_2 = names_2.difference(names_1)

print(dif_1)
print(dif_2)

name_3 = names_1.union(names_2)
print(name_3)

name_4 = names_1.intersection(names_2)
print(name_4)
