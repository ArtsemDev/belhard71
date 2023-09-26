# # # # # # # def foo():
# # # # # # #     return "first function!"
# # # # # # #
# # # # # # #
# # # # # # # res = foo()
# # # # # # # print(res)
# # # # # #
# # # # # #
# # # # # # # def multiply(a, b=6, *args, **kwargs):
# # # # # # #     c = a * b
# # # # # # #     print(args)
# # # # # # #     print(kwargs)
# # # # # # #     return c
# # # # # # #
# # # # # # #
# # # # # # # print(multiply(1, 2, 3, 4, 5, c=8, e=9))
# # # # # #
# # # # # #
# # # # # # def multiply(*numbers):
# # # # # #     if numbers:
# # # # # #         c = 1
# # # # # #         for number in numbers:
# # # # # #             c *= number
# # # # # #         return c
# # # # # #     else:
# # # # # #         return 0
# # # # # #
# # # # # #
# # # # # # # def bar(a, b=5, c=None, *args):
# # # # # # #     print(a)
# # # # # # #     print(b)
# # # # # # #     print(args)
# # # # # # #     print(c)
# # # # # # #
# # # # # # #
# # # # # # # bar(1, 2, 3, 4, 5, 6, 7, 8)
# # # # # #
# # # # # #
# # # # # # def baz(e, *, a, b, c):
# # # # # #     print(a)
# # # # # #     print(b)
# # # # # #     print(c)
# # # # # #
# # # # #
# # # # #
# # # # # def bar(a, b=None):
# # # # #     if b is None:
# # # # #         b = []
# # # # #     b.append(a)
# # # # #     print(b)
# # # #
# # # a = 4
# # #
# # #
# # # def bar(b):
# # #     return b + a
# # #
# # #
# # # # LEGB
# #
# # #  написать функцию is_palindrome, принимающая текст и возвращающая:
# # #  True - если строка является палиндромом
# # #  False - в противном случае
# # #  проверка должна происходить без учета регистра
# #
# # from typing import Literal, Callable
# #
# #
# # def is_palindrome(text: str) -> bool:
# #     return text.lower() == text.lower()[::-1]
# #
# #
# # def get_response(method: Literal["GET", "POST", "PUT"]):
# #     print(method)
# #
# #
# # def b(func):
# #     print(func())
# #
# #
# # def a():
# #     print("a")
# #
# #
# # b(func=a)
#
#
# def foo():
#     def bar():
#         print("bar")
#
#     bar()
#
#
# # multiply = lambda a, b: a * b
# # print(multiply(5, 6))
#
#
# # objs = [1, 3, "5", 2, 3, "9"]
# # objs.sort(key=lambda x: int(x))
# # # [1, 3, 5, 2, 3, 9]
# # print(objs)
#
# users = [
#     {"name": "Alex", "age": 34},
#     {"name": "Pavel", "age": 43},
#     {"name": "Masha", "age": 23},
#     {"name": "Petya", "age": 15},
# ]
# users.sort(key=lambda x: x.get("age", 0))
# # [34, 43, 23, 15]
# print(users)


# numbers = ["3", "5", "2", "6", "4", "8"]
# numbers = [int(number) for number in numbers]
# result = list(map(int, numbers))

# numbers = [5, 6, 4, 3, 4, 5, 3]
# result = [number for number in numbers if number % 2]
# print(result)
# result = filter(lambda x: x % 2, numbers)
# for i in result:
#     print(i)

# text = "Hello"
# numbers = [3, 5, 7]
# result = zip(text, numbers, (True, False))
# print(result)

# numbers = [4, 6, 5, 2, 3, 5, 4]
# result = [str(number) for number in [number for number in numbers if number % 2]]


# def get_users(c):
#     users = []
#     for i in range(c):
#         users.append(f"{i}" * 100)
#     return users
#
#
# for user in get_users(1000000):
#     print(user)

# def get_users():
#     for i in range(1000000):
#         yield f"{i}" * 100
#
# a = get_users()

# result = get_users(c=1000000)
# for user in result:
#     print(user)
# sleep(100)


# get_users = (i for i in range(1000000))
# print(get_users)


# def to_str(x):
#     return str(x)
#
#
# numbers = [1, 2, 3, 4, 5, 6]
# for i in map(to_str, numbers):
#     print(i)


# def my_range(start, step):
#     while True:
#         yield start
#         start += step
#
#
# for i in my_range(0, 2):
#     print(i)


#  Написать функцию принимающая 2 строки одинаковой длинны
#  и кодирующая первую строку используя вторую с использованием шифра Вернама
#  message = LONDON
#  key = SYSTEM
#  01001100 01001111 01001110 01000100 01001111 01001110
#  01010011 01011001 01010011 01010100 01000101 01001101
#  00011111 00010110 00011101 00010000 00001010 00000011


def vernama_encode(message: str, key: str) -> list[int]:
    if len(message) != len(key):
        raise ValueError("the message and the key do not match in length")

    result = []
    for i in range(len(message)):
        # VAR 1
        m = message[i]
        k = key[i]
        m = ord(m)
        k = ord(k)
        r = m ^ k
        result.append(r)
        # VAR 2
        # result.append(ord(message[i]) ^ ord(key[i]))
    return result
    # VAR 3
    # return list(map(lambda x: x[0] ^ x[1], zip(map(ord, message), map(ord, key))))


print(vernama_encode("LONDON", "SYSTEM"))
