numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)

names = ["Hudayfe", "Yurt", "HY"]
starts_h = [name for name in names if name.startswith("H")]

print(starts_h)
print(names is starts_h)
print("names: ", id(names), "starts_h: ", id(starts_h))
