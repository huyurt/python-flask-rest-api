class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method.")


ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperbook")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            "name": name,
            "price": price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")

    @staticmethod
    def store_detail(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

