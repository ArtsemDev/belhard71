# a = int(input())
#
# is_even = 'No' if a % 2 else 'Yes'
#
# if a % 2:
#     is_even = 'No'
# else:
#     is_even = 'Yes'

# if a > 0:
#     print("a is positive")
# elif a == 0:
#     print("a is zero")
# else:
#     print("a is negative")

# if a > 0 or a == -5:
#     print('some print')

# if a > 0 and a == 5:
#     print("some print")

# if a > 0 or a == -5 and a < 0:
#     print()

# if a:
#     print()

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# a = 0
# b = 0
# print(a and False)


# for i in range(1, 10, 2):
#     i **= 2
#     print(i)

# for _ in range(10):
#     print('Hello world')

# text = "Hello world"
# for i, j in enumerate(text):
#     print(i, j)

# t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# for i, j, k in t:
#     print(i, j, k)


# data = {"a": 1, "b": 2, "c": 3, "d": 4, "f": 5}
#
# for key, val in data.items():
#     print(key, val)


# for i in range(10):
#     i **= 2
#     print(i)


# BAD
# numbers = [5, 6, 3, 4, 5, 6, 2]
#
# for numbers in numbers:
#     print(numbers)
# print(numbers)

# BAD
# n = int(input())
# for n in range(n):
#     print(n)


# for i in range(10):
#     if i == 7:
#         break
#     else:
#         pass
#     print(i)
# else:
#     print("цикл закончился самостоятельно!")
# print("finish!")

# BAD
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     numbers.append(number)

# BAD
# numbers = [2, 4, 3, 5, 4, 6, 5, 7, 6, 3, 4]
# for number in numbers:
#     if number % 2 == 0:
#         numbers.remove(number)
# print(numbers)

# n = int(input())
# # numbers = [2**i for i in range(1, n + 1)]
# numbers = []
# for i in range(1, n + 1):
#     numbers.append(2**i)
# print(numbers)

# numbers = [(i**2) if i % 2 != 0 else (i**3) for i in range(1, 101) if i % 5 != 0]
# numbers = [i for i in range(1, 101) if i % 5 != 0]
# for i in range(1, 101):
#     if i % 5 != 0:
#         numbers.append((i**2) if i % 2 != 0 else (i**3))
# print(numbers)


# words = ["hello", "world", "python", "java", "pycharm"]
# letters = [[letter for letter in word] for word in words]
# for word in words:
#     data = [letter for letter in word]
#     letters.append(data)
# print(letters)
# n = int(input())
# m = int(input())
# matrix = [[0 for _ in range(n)] for _ in range(m)]


# i = 0
# while i < 10:
#     i += 1
# print(i)


# TODO Переспрашивать у пользователя возраст до тех пор, пока он не введет число

# age = input("Enter age: ")
# while not age.isdigit():
#     age = input("Are you stupid? Try again: ")

# while not (age := input()).isdigit():
#     pass

# TODO Пользователь вводит сумму вклада и процент по вкладу
#  необходимо высчитать через сколько лет сумма вклада удвоится (вклад капитализации)
# deposit = float(input())
# percent = float(input())
# target_amount = deposit * 2
# year = 0
# while deposit < target_amount:
#     deposit += deposit * percent
#     year += 1
# print(year)

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError:
#     print("введено не число")
# except ZeroDivisionError as e:
#     print(e)
#     print("на 0 делить нельзя")
# else:
#     print("ошибок не было")
# finally:
#     print('выполняется в любом случае')

# BAD
# a = 5
# if type(a) is int or type(a) is float or type(a) is complex:
#     pass


# a = 5
# print(isinstance(a, (int, float, complex)))

# obj = [1, 2, 3, "hello", True, 0]
# print(all(obj))
# print(any(obj))
# N = 5
# M = 3
# K = -10
# -9 -6 -3 0 3

# N = 34
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34
