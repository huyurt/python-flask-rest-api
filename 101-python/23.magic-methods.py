class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

student = Person("Hudayfe", 45)
print(student)



class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        return sum([item['price'] for item in self.items])


