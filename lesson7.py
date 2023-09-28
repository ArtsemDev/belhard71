# users = [
#     {"name": "Vasya", "salary": 1400},
#     {"name": "Petya", "salary": 1300},
#     {"name": "Pavel", "salary": 1500},
#     {"name": "Masha", "salary": 1350},
# ]
#
#
# def find_min_salary(x):
#     return x.get("salary")
#
#
# print(min(users, key=lambda x: x.get("salary")))
# a = 5
#
#
# def foo():
#     def bar():
#         print("bar")
#
#     return bar
#
#
# res = foo()

#
# def multiply(a):
#     def wrapper(b):
#         def wrapped(c):
#             return a * b * c
#
#         return wrapped
#
#     return wrapper
decorated_function = []


def decorator(func):
    decorated_function.append(func)

    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError

        result = func(*args)
        return f"{result=}"

    return wrapper


@decorator
def multiply(*args):
    res = 1
    for number in args:
        res *= number
    return res


routes = {}


def dispatcher(path):
    def wrapper(func):
        routes[path] = func

        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return wrapper


@dispatcher(path="/")
def index():
    return "index.html"


@dispatcher(path="/about")
def about():
    return "about.html"


# l = [1, 2, 3, 4, 5, 6]
# print(1, 2, 3, 4, 5, 6)

# data = {"a": 1, "b": 2}


def foo(a, b):
    print(a * b)


#  Написать функция, принимающая 2 аргумента:
#  1. shops - словарь, в качестве ключа которого выступает название магазина
#  а в качестве значения, список товаров которые есть в данном магазине
#  2. product - название товара
#  необходимо вернуть список названий магазинов, отсортированный в алфавитном порядке
#  в которых нет данного товара
#  * список названий отсортировать в алфавитном порядке игнорируя регистр


def find_shop(shops: dict[str, list[str]], product: str) -> list[str]:
    # VAR 1
    result = []
    for shop, products in shops.items():
        if product not in products:
            result.append(shop)
    result.sort(key=lambda x: x.lower())
    return result
    # VAR 2
    # return sorted(
    #     [shop[0] for shop in filter(lambda x: product not in x[1], shops.items())],
    #     key=lambda x: x.lower(),
    # )


#  На вход функции поступает
#  1. строка содержащая слова разделенные пробелом
#  2. строка - окончание
#  Вернуть список слов, которые не заканчиваются на указанное окончание


def find_words(words: str, end: str) -> list[str]:
    """Ищет слова не заканчивающиеся на указанное окончание

    :param words: Строка слов разделенных пробелом
    :param end: Окончанием
    :return: Список слов которые не заканчиваются на указанное окончание
    """
    words = words.split()
    result = []
    for word in words:
        if not word.endswith(end):
            result.append(word)
    return result
    # return [word for word in words.split() if not word.endswith(end)]
    # return [*filter(lambda x: not x.endswith(end), words.split())]


numbers = [
    3,
    4,
    2,
    3,
    2,
    [
        3,
        4,
        2,
        4,
        [
            6,
            4,
            5,
            4,
            [7, 5, 6, 4],
            [
                7,
                4,
                5,
                3,
                42,
            ],
        ],
    ],
    6,
    4,
    5,
    4,
    [4, 2, 4, 2, 4, [7, 5, 6, 3, 4, 2]],
    8,
    5,
    7,
    45,
    3,
    [7, 6, 4, 3, 2, [8, 7, 5, 7, 6, 7]],
]


def recursive_multiply(numbers: list) -> int:
    result = 1
    for number in numbers:
        if isinstance(number, int):
            result *= number
        else:
            result *= recursive_multiply(number)
    return result


# data = [1, 2, 3, [1, 2, 3, [1, 2, 3]]]
# print(recursive_multiply(data))
