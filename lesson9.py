# class Car:
#     def __init__(self, volume: float, max_speed: int, hp: int) -> None:
#         self.volume = volume
#         self.max_speed = max_speed
#         self.hp = hp
#
#     def drive(self):
#         print("drive")
#
#
# class ElectricCar(Car):
#     def __init__(self, volume: float, max_speed: int, hp: int, voltage: int):
#         super().__init__(volume, max_speed, hp)
#         self.voltage = voltage
#
#     def charge(self):
#         print("charge")
#
#
# class A:
#     def name(self):
#         print("a")
#
#
# class B:
#     def name(self):
#         print("b")
#
#
# class C(A, B):
#     pass
#
#
# class K:
#     pass
#
#
# class H:
#     pass
#
#
# class M:
#     pass
#
#
# class D(K, H):
#     pass
#
#
# class E(H, M):
#     pass
#
#
# class F(D, E):
#     pass
#
#
# class G(C, F):
#     pass
#
#
# class Animal:
#     name = "Animal"
#
#     def walk(self):
#         return "walk"
#
#
# class Cat(Animal):
#     name = "Cat"
#
#     def foo(self):
#         print(super().walk())
#
#     def walk(self):
#         raise AttributeError
#
#
# class YandexMusic:
#     def get(self, name):
#         pass
#
#
# class SpotifyMusic:
#     def get(self, name):
#         pass
#
#
# def get_music_by_name(name, music: YandexMusic | SpotifyMusic):
#     return music.get(name)
#
#
# class Phone:
#     def __sms(self):
#         print("sms")
#
#
# class DebitCard:
#     def __init__(self, number):
#         self.__number = number
#
#     @property
#     def number(self):
#         return self.__number[:7] + "** **** " + self.__number[-4:]
#
#     @number.setter
#     def number(self, value):
#         if not isinstance(value, str):
#             raise TypeError
#
#         if len(value.replace(" ", "")) != 16:
#             raise ValueError
#
#         self.__number = value
from abc import ABC, abstractmethod


# from abc import ABC, abstractmethod
#
#
# class AbstractMusic(ABC):
#     def connect(self):
#         print("connected")
#
#     @abstractmethod
#     def get(self):
#         raise NotImplementedError
#
#     @classmethod
#     @abstractmethod
#     def all(cls):
#         raise NotImplementedError
#
#
# class YandexMusic(AbstractMusic):
#     def get(self):
#         pass
#
#     @classmethod
#     def all(cls):
#         pass
#
#     def save(self):
#         pass
#
#
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# from abc import ABC, abstractmethod
#
#
# class Phone(ABC):
#     @abstractmethod
#     def call(self):
#         raise NotImplementedError
#
#
# class SmsMixin:
#     def sms(self):
#         raise NotImplementedError
#
#
# class MobilePhone(SmsMixin, Phone):
#     def call(self):
#         pass
#
#     def sms(self):
#         pass
#
#
# class SimplePhone(Phone):
#     def call(self):
#         pass


# SOLID
# S - Single responsibility
# O - Open/Close
# L - Liskov
# I - Interface segregation
# D - Dependency inversion


class AbstractMusic(ABC):
    @abstractmethod
    def get(self, name: str) -> str:
        raise NotImplementedError


class Music(AbstractMusic):
    __slots__ = ("name",)

    def __init__(self):
        self.name = "Music"

    def get(self, name: str) -> str:
        return name


class MusicScreen(AbstractMusic):
    def __init__(self, music: Music):
        self.music = music

    def get(self, name):
        return self.music.get(name)


def foo(self):
    print("foo")


class MyMeta(type):
    def __new__(cls, clsname, superclassess, attributes):
        print(clsname, superclassess, attributes)
        attributes["foo"] = foo
        return super().__new__(cls, clsname, superclassess, attributes)


class A(metaclass=MyMeta):
    class_attr = "Class attribute"

    def __init__(self, first_name):
        self.first_name = first_name


def __init__(self, name):
    self.name = name


last_name = "Pupkin"


User = type("User", (Music,), {"__init__": __init__, "last_name": last_name})

vasya = User(name="Vasya")
print(vasya.last_name)
print(vasya.get("Music"))


a = Music()
