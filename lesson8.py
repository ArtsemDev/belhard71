# data1 = {"c": "d"}
# data2 = {"a": "b"}
# data3 = data1 | data2
# data4 = {"a": "b"}
#
# for k, v in data4.items():
#     if k not in data3 or data3.get(k) != v:
#         break
# else:
#     print("YES")

# data1 = {"a": "b", "c": "d"}
# data2 = {"c": "e", "f": "g"}
# data1.update(data2)
# print(data1)


class User:
    name = "A"
    role = "user"

    def __init__(self, email: str, age: int) -> None:
        """Инициализация атрибутов объекта

        :param email: Почта пользователя
        :param age: Возраст пользователя
        """
        self.email = email
        self.age = age

    def foo(self):
        pass

    def bar(self):
        self.foo()

    @classmethod
    def class_foo(cls):
        print("class foo")

    @staticmethod
    def static_method():
        print("static method")


# obj1 = User(email="vasya@gmail.com", age=34)
# obj2 = User(email="petya@gmail.com", age=23)
# print(obj1.email)
# print(obj2.email)

# obj1.foo()
# obj2.foo()

# User.foo(self=obj1)
# User.foo(self=obj2)
# obj1.__class__.name = "B"
# print(obj1.name)
# print(obj2.name)
# print(User.name)


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
        self.is_published = False

    def set_discount(self):
        if self.price * 0.90 > 4:
            self.price *= 0.9
        else:
            self.price *= 0.95

    def __str__(self):
        return f"{self.name}: {self.price}$"

    # def __bool__(self):
    #     return self.is_published

    def __len__(self):
        return round(self.price**2)

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        elif isinstance(other, (int, float)):
            return self.price > other
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, Product):
            return self.price >= other.price
        elif isinstance(other, (int, float)):
            return self.price >= other
        else:
            raise TypeError

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        elif isinstance(other, (int, float)):
            return self.price == other
        else:
            raise TypeError

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        elif isinstance(other, (int, float)):
            return self.price + other
        else:
            raise TypeError

    def __radd__(self, other):
        return self.__add__(other)


product1 = Product(name="Latte", price=5.0)
product2 = Product(name="Cappuccino", price=4.5)
print(5.6 + product1)


class Category:
    def __init__(self, name: str, products: list[Product]):
        self.name = name
        self.products = products
        self.i = -1

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.i += 1
    #     if self.i < len(self.products):
    #         return self.products[self.i]
    #     else:
    #         self.i = -1
    #         raise StopIteration

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item):
        return self.products[item]


# product1.set_discount()
# print(product1.price)
# print(bool(product1))
# category1 = Category(name="Coffee", products=[product1, product1])
# print(category1[1])
# for i in category1:
#     print(i)
