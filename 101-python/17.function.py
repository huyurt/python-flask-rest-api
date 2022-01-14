def add(x, y):
    result = x + y
    print(result)

add(3, 5)


def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Yurt", name="Hudayfe")


def sum(x, y=10):
    print(x + y)

sum(x=6)



default_y = 8

def s(x, y=default_y):
    print(x + y)

s(2)
default_y = 0
s(2)




def a(x, y):
    return
    print(x + y)
    return x + y

print(a(5, 8))


def return_42():
    return 42

def my_function(x, y):
    return x * y
