name = "Hudayfe"
greeting = f"Hi, {name}"

print(greeting)

name = "Yurt"

print(greeting)

greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_2 = greeting.format("Hudayfe")

print(with_name)
print(with_name_2)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Hudayfe", "Thusday")

print(formatted)


