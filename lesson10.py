# # from time import sleep
# #
# # file = open(file="out.txt", mode="r", encoding="utf-8")
# # for line in file:
# #     sleep(2)
# #
# # file.close()
#
#
# # file = open("input.txt", "r", encoding="utf-8")
# # print(file.read())
# # file.seek(2)
# # print(file.read())
# # file.close()
# # from time import sleep
# #
# # file = open("output.txt", "w", encoding="utf-8")
# # for _ in range(1000):
# #     file.write("hello\n")
# #     file.flush()
# #     sleep(1)
# # file.close()
#
#
# # with (
# #     open("input.txt", "r", encoding="utf-8") as file,
# #     open("output.txt", "w", encoding="utf-8") as file2,
# # ):
# #     print(file.readlines())
# #     print(file.closed)
# # print(file.closed)
#
#
# class Repository:
#     def __init__(self):
#         self.closed = False
#
#     def close(self):
#         self.closed = True
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#
#
# # with Repository() as rep:
# #     print(rep.closed)
# # print(rep.closed)
#
# # from ujson import dump
#
#
# # text = '{"name": "Alex"}'
# # print(loads(text))
#
# # with open("input.json", "r", encoding="utf-8") as file:
# # print(file.read())
# # data = load(file)
# # print(data)
#
#
# # data = {"id": 4, "title": "Мобильный телефон", "category_id": 3, "is_new": True}
# # with open("output.json", "w", encoding="utf-8") as file:
# #     dump(data, file, indent=2, ensure_ascii=False)
# # text = dumps(data, indent=2)
# # print(text)
#
# # with open("input.csv", "r", encoding="utf-8") as file:
# #     for line in DictReader(file, delimiter=";"):
# #         print(line)
# # lines = [line.strip().split(",") for line in file]
# # print(lines)
# # print(list(reader(file)))
# from csv import *
#
# # lines = [["name", "email", "age"], ["vasya", "vasya@gmail.com", 34]]
# # lines = ["name", "email", "age"]
# data = [
#     {"name": "vaysa", "email": "vasya@gmail.com"},
#     {"name": "petya", "email": "petya@gmail.com"},
# ]
#
# with open("output.csv", "w", encoding="utf-8") as file:
#     # w = writer(file)
#     # w.writerow(lines)
#     w = DictWriter(file, fieldnames=("email", "name"))
#     w.writeheader()
#     w.writerows(data)
from datetime import datetime
from re import fullmatch
from typing import Optional, Self, Annotated

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    model_validator,
    AfterValidator,
    # validate_call,
)
from pydantic.types import Decimal


# print(datetime.utcnow().isoformat())
# from pydantic.types import Decimal


def check_password(value: str) -> str:
    pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}$"
    if fullmatch(pattern, value) is None:
        raise ValueError("incorrect password")
    return value


PasswordStr = Annotated[str, AfterValidator(func=check_password)]


class RegisterForm(BaseModel):
    username: str = Field(default=..., min_length=2)
    email: EmailStr
    password: PasswordStr = Field()
    age: Optional[int] = Field(ge=18, le=65)
    date_of_birth: datetime
    # role: Literal["admin", "manager", "user"]
    # price: Decimal = Field(max_digits=8, decimal_places=2)

    @field_validator("username", mode="after")
    def username_validator(cls, value: str) -> str:
        if not value.isidentifier():
            raise ValueError("invalid username")
        return value

    @model_validator(mode="after")
    def validator(self) -> Self:
        if self.username.lower() in self.password.lower():
            raise ValueError("password has not contains username")
        return self


# form = RegisterForm(
#     username="Vasya",
#     email="qwert@gmail.com.ru",
#     password="VeryStrongPassword1!",
#     age=64,
#     date_of_birth=1696950430.84663,
# )
# print(form.date_of_birth)
# print(datetime.utcnow().timestamp())

# @validate_call()
# def foo(a: str, b: int):
#     pass
#
#
# foo(a="wert", b="dfghjk")


class A(BaseModel):
    b: list[int]


class B(BaseModel):
    c: A


# b = B(c={"b": [2, 3, 4, "dfg"]})


class ProductDetail(BaseModel):
    name: str
    price: Decimal = Field(max_digits=8, decimal_places=2)


class CategoryDetail(BaseModel):
    name: str
    products: list[ProductDetail]
    children: list["CategoryDetail"] = Field(default=None)


data = {
    "name": "Coffee",
    "products": [{"name": "Latte", "price": 5.5}],
    "children": [
        {"name": "IceCoffee", "products": [{"name": "Ice Latte", "price": 4}]}
    ],
}

cat = CategoryDetail(**data)
# print(cat.model_dump_json(indent=2))
