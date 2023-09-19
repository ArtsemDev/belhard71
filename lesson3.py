# # # # # text = 'python\nworld'
# # # # # print(len(text))
# # # # # text = r'\n\n\n\n\n'
# # # # # print(text)
# # # # # name = 'Alex'
# # # # # age = 23
# # # # # text1 = 'hello %s your age %d' % (name, age)
# # # # # text2 = 'hello {} your age {}'.format(name, age)
# # # # # text4 = 'hello {name} your age {age}'.format_map({'name': name, 'age': age})
# # # # # text3 = f'hello {name} your age {age}'
# # # # # print(text4)
# # # #
# # # # # a = 3.3456789
# # # # # text = f'{a:.3f}'
# # # # # text = '\N{grinning face}'
# # # # # print(text)
# # # #
# # # #
# # # # # text = 'hello world python java'
# # # # # a = text.split(' ', 2)
# # # # # text2 = ' | '.join(a)
# # # # # print(text2)
# # # # # # print(text.rsplit(' ', 2))
# # # #
# # # #
# # # # # text = 'Hello world'
# # # # # print(text.partition('1'))
# # # # # print(text.rpartition('1'))
# # # # # print(text.find('o'))
# # # # # print(text.rfind('o'))
# # # # # text = 'hello hello hello world'
# # # # # text2 = text.replace('hello', 'bye', 2)
# # # # # print(text2)
# # # #
# # # # # text = 'hello world'
# # # # # print(text.startswith('hell'))
# # # # # print(text.endswith('rld'))
# # # #
# # # #
# # # # # text = 'hello\twe\twe'
# # # # # print(text.expandtabs(4))
# # # #
# # # # # text = '...,,,---hello---,.world,.,.,.,'
# # # # # print(text.lstrip('.,-'))
# # # # # print(text.rstrip('.,-'))
# # # # # print(text.strip('.,-'))
# # # #
# # # # # text = 'hello'
# # # # # print(text.center(12, '-'))
# # # # # print(text.ljust(12, '-'))
# # # # # print(text.rjust(12, '-'))
# # # # # print(text.zfill(12))
# # # #
# # # # # print(bin(12)[2:].zfill(8))
# # # #
# # # # # text = 'привет'
# # # # # print(text.encode())
# # # #
# # # # # text = 'hello'
# # # # # text2 = 'hello'
# # # # # print(text2 != text)
# # # #
# # # #
# # # # # text = 'Hello world'
# # # # # print('Hell' in text)
# # # #
# # # #
# # # # # a = 13
# # # # # b = 14
# # # # # print(bin(a))
# # # # # print(bin(b))
# # # # # print(a ^ b)
# # # #
# # # # # print(~-25)
# # # # # text = 'hello world'
# # # # # print(text[4])
# # # # # print(text[~4])
# # # #
# # # # # print(bin(13 >> 2))
# # # #
# # # #
# # # # # a = [1, 2, 3, 4]
# # # # # print(a[1])
# # # # # a[1] = 'Hello'
# # # # # print(a)
# # # # # text = 'hello'
# # # # # a = list(text)
# # # # # print(a)
# # # #
# # # # # a = [2 ** i for i in range(10)]
# # # # # print(a)
# # # #
# # # # a = [5, 3, 4, 6, 7, 2, 3]
# # # # b = sorted(a)
# # # # print(b)
# # # # # a.sort(reverse=True)
# # # # # a.append(a)
# # # # # a.extend(a)
# # # # # a.insert(3, 'hello')
# # # # # a.remove(3)
# # # # # print(a)
# # # # # b = a.pop(1)
# # # # # print(a)
# # # # # print(b)
# # # # # del a[1:5:2]
# # # # print(a)
# # #
# # #
# # # a = ['Hello', 'World', 'Python']
# # # b = [3, 4, 5]
# # # a.append(b)
# # # c = a.copy()
# # # b.append(6)
# # # print(c)
# # # b = [6, 7, 4]
# # # a = (3, 5, 2, 3, b)
# # # a[4].append(45)
# # # print(a)
# # # print(b)
# #
# # # a = 3,
# # # print(a)
# #
# # # a = ['hello', 'python', 'world']
# # # # b, *c = a
# # # # print(b)
# # # # print(c)
# # # b, c = a[2], a[0]
# # # print(b)
# # # print(c)
# #
# # # a = 5
# # # b = 4
# # # c = 9
# # # a, b, c = c, b, a
# #
# # # a = [1, 2, 3, 4, [5, 6, 7, 'Hello']]
# # # print(a[-1][-1][1])
# #
# #
# # data = {
# #     'name': 'Alex',
# #     'age': 45
# # }
# # data2 = {
# #     'city': 'Minsk',
# #     'age': 46
# # }
# # # print('name' in data)
# # # data3 = {**data, **data2}
# # # data4 = data | data2
# # # data.update(data2)
# # # print(data)
# # # print(data['name'])
# # # data['city'] = 'Minsk'
# # # print(data)
# # # print(data.setdefault('email'))
# # # print(data)
# #
# # # print(list(data))
# # # print(sum([4, 5, 6, 7, 8, 9], 2))
# #
# # # print(max(['Hello', 'Python']))
#
# a = float(input())
# b = float(input())
# c = float(input())
# a_is_positive = a > 0
# b_is_positive = b > 0
# c_is_positive = c > 0
# positive_count = a_is_positive + b_is_positive + c_is_positive
#
# s = {7, 4, 6, 3, 5, 4, 8, 7, 5, 6, 34, 45, 109}
# # print(s.isdisjoint([12121, 23232]))
# s2 = {4, 6, 3, 5}
# s.intersection_update()


# numbers = [i ** 2 for i in range(0, 101, 2)]
# zero = [0 for _ in range(100)]
# print(zero)

# text = 'hello world'
# data = {i: ord(i) for i in text}
# print(data)

# TODO пользователь вводит текст, необходимо сдвинуть все символы на 2 по таблице ASCII
# result = ''.join([chr(ord(i) + 2) for i in input()])
# print(result)

from collections import *


# data = {'a': 1, 'b': 2, 'c': 3}
# order_data = OrderedDict(data)
# order_data.move_to_end('b', last=False)
# print(order_data)
# order_data.move_to_end('b', last=True)
# print(order_data)

# User = namedtuple('User', ['name', 'email'])
# vasya = User(name='Vasya', email='vasya@gmail.com')
# print(vasya.name)
# print(vasya.email)
# print(vasya._asdict())


# text = 'Hello world'
# c = Counter(text)
# print(c)
# c2 = Counter('Goodbye')
# print(c2)
# print(c - c2)
# c.subtract(c2)
# print(c)

# print(c.most_common(n=2))
# print(list(c.elements()))

# data = defaultdict(list)
# data['a'].append(1)
# data['a'].append(5)
# print(data)
# data = {}
# data['a'] = []
# data['a'].append(3)

# data = dict(name='Alex', age='34')


# text = 'hello {} {}'.format('asdf', 'asdf')


# data1 = {'a': 1, 'b': 2}
# data2 = {'c': 3, 'b': 4}
#
# chain = ChainMap(data1, data2)
# chain.maps[1]['d'] = 5
# print(chain.maps)
# b = [1, 2, 3]
# a = [2, 4, 6, 8, 10, b]
# q = deque(a)
# q[5].append(4)
# print(b)


# a = [2, 4, 2, 4, 2]
# print(4 in a)
# print(5 not in a)
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# print(a.index(4, 2))
# a.insert(1, 'qwerty')
# print(a.pop(1))


# allowed_methods = ['get', 'post']
# user_method = 'get'
# print(user_method in allowed_methods)

# a = (4, )

n = 3
data = {
    0: {'name': 'Alex', 'email': 'alex@gmail.com'},
    1: {'name': 'Petya', 'email': 'petya@gmail.com'},
    2: {'name': 'Masha', 'email': 'masha@gmail.com'}
}
