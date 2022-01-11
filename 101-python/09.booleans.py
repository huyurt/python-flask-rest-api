
list_1 = ["Hudayfe", "Yurt"]
list_2 = ["Hudayfe", "Yurt"]

print(list_1 == list_2)
print(list_1 is list_2)

list_2 = list_1
print(list_1 is list_2)

list_1.append("HY")
print(list_2)
print(f"List 1: {list_1}, List 2: {list_2} => {list_1 is list_2}")

