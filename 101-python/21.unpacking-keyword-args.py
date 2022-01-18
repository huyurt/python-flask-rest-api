def named(**kwargs):
    print(kwargs)

details = {"name": "HY", "age": 11}

named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print(print_nicely(name="Hudayfe", age=12))


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Yurt", age=15)


def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Hudayfe") # Error, must be mapping
# myfunction(**None) # Error

