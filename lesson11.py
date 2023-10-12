# # from itertools import *
# #
# # # print(list(product("ABCD", [1, 2, 3, 4], (True, False))))
# #
# # # print(list(takewhile(lambda x: x != 4, (1, 2, 3, 4, 5, 6, 7, 8))))
# # # print(list(dropwhile(lambda x: x != 4, (1, 2, 3, 4, 5, 6, 7, 8))))
# #
# # # print(list(compress([2, 4, 6, 8, 10], (0, 1))))
# #
# #
# # a = chain("hello", (1, 2, 3, 4), ["Python", True, None])
# #
# # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # # for number in islice(numbers, 0, 10, 2):
# # #     print(number)
# # # print(list(zip_longest("hello", (1, 2, 3), [True, False])))
# # # print(tee("hello", 2))
# #
# # print(list(groupby([{"a": 1}, {"a": 3}, {"a": 2}, lambda x: x.get("a")])))
# # # print(list(accumulate([1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x, y: x - y)))
# # from math import *
# #
# #
# # print(isqrt(5))
#
# # print(choices([3, 5, 7, 9, 10], k=2))
#
#
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # shuffle(numbers)
# # print(numbers)
# # print(sample(numbers, 3))
#
#
# # from os import *
# #
# #
# # print(system(""))
#
#
# # from pathlib import Path
# #
# #
# # BASE_DIR = Path(__file__).resolve().parent
# # print(BASE_DIR / "core")
#
# # from datetime import *
#
#
# # BELARUS_TIMEZONE = timezone(timedelta(hours=3), "Europe/Minsk")
# # print(datetime.now(tz=BELARUS_TIMEZONE))
# # d = datetime.utcnow()
# # print(d.day)
# # print(d.strftime("%A %d-%b %Y"))
# # print(datetime.strptime("Thursday 12-Oct 2023", "%A %d-%b %Y"))
# # delta = timedelta(weeks=52)
#
#
# # from dataclasses import dataclass
# # from enum import IntEnum
# # from http import HTTPStatus
# #
# #
# # class Roles(IntEnum):
# #     USER: int = 1
# #     MANAGER: int = 2
# #     ADMIN: int = 3
# #
# #
# # @dataclass
# # class User:
# #     name: str
# #     role: int
#
#
# # vasya = User(name="Vasya", role=2)
# #
# #
# # if vasya.role == Roles.ADMIN:
# #     pass
#
# # status = 418
# # if status == HTTPStatus.IM_A_TEAPOT:
# #     pass
#
#
# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument("-p", "--port", required=True)
# parser.add_argument("--host", default="127.0.0.1")
# parser.add_argument("-d", "--debug", action="store_true")
# args = parser.parse_args()
# print(args)
from functools import *
from time import sleep


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        return func(*args, **kwargs)

    return wrapper


# @decorator
# def foo():
#     """FOO docstring"""
#
#
# print(foo())


@lru_cache(maxsize=3)
def bar(a, b):
    sleep(2)
    return a * b


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @cached_property
    def c(self):
        sleep(2)
        return self.a * self.b


# print(reduce(lambda x, y: x * y, [1, 3, 5, 2, 4, 3]))


@singledispatch
def foo(a: int, b):
    return a * b


@foo.register
def _(a: str, b):
    return a + str(b)


# from re import *
#
#
# PASSWORD_PATTERN = compile(
#     r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}$"
# )


# PASSWORD_PATTERN.fullmatch("")
# from phonenumbers import parse

# print(parse("+375 (25) 914-52-08"))


from requests import Session


with Session() as session:
    response = session.get(
        url="https://catalog.onliner.by/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0"
        },
    )
    print(response.status_code)
    # print(response.text)
    print(response.headers)
    print(response.cookies)
# https://catalog.onliner.by/player?player_type%5B0%5D=hifiplayer&player_type%5Boperation%5D=union
