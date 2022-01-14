t = 5, 11
x, y = t

print(x, y)


persons = [('Hudayfe', 98, "Developer"), ('Yurt', 89, "Artist"), ('HY', 99, "Doctor")]
for name, age, profession in persons:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
for person in persons:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


person = ('Hudayfe', 98, "Developer")
name, _, profession = person

print(name, profession)


head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)


*head, tail = [1, 2, 3, 4, 5]

print(head)
print(*head)
print(tail)

