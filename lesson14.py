from threading import (
    Thread,
    current_thread,
    RLock,
    Semaphore,
    Event,
    local
)
# from time import sleep
#
# # from queue import Queue
# # from time import sleep
# #
# #
lock1 = RLock()
# # semaphore1 = Semaphore(value=5)
# # event1 = Event()
# # q = Queue(maxsize=5)
# # l = local()
# #
# #
# # def spam():
# #     with semaphore1:
# #         for i in range(100):
# #             sleep(1)
# #             with lock1:
# #                 print(current_thread().name)
# #
# #
# # # threads = [Thread(target=spam) for _ in range(10)]
# # # for thread in threads:
# # #     thread.start()
# # #
# # #
# # # class MyThread(Thread):
# # #
# # #     def run(self):
# # #         print(self.is_alive())
# # #         for i in range(100):
# # #             print(self.name)
# #
# #
# # # thread = MyThread()
# # # thread.start()
# # # thread.join()
# # # print(thread.is_alive())
# #
# # a = 4
# #
# #
# # def foo():
# #     with lock1:
# #         if a == 4:
# #             sleep(1)
# #             print(a * 2)
# #
# #
# # def bar():
# #     global a
# #     with lock1:
# #         a = 5
# #
# #
# # # thread1 = Thread(target=foo)
# # # thread2 = Thread(target=bar)
# # # thread1.start()
# # # thread2.start()
# #
# #
# # def func1():
# #     l.a = 5
# #     from random import randint
# #     for _ in range(10):
# #         sleep(1)
# #         q.put(randint(1, 10))
# #
# #
# # def func2():
# #     for _ in range(10):
# #         obj = q.get(block=True, timeout=2)
# #         print(obj)
# #
# #
# # thread1 = Thread(target=func1)
# # thread2 = Thread(target=func2)
# # thread1.start()
# # thread2.start()
#
#
# from requests import Session
# # from multiprocessing import Process
# #
# #
# def get_request():
#     with Session() as session:
#         response = session.get("https://www.21vek.by/")
#         # with lock1:
#         print(response.status_code)
#
#
# threads = [Thread(target=get_request) for _ in range(10)]
# for thread in threads:
#     thread.start()
#
#
# if __name__ == '__main__':
#     processes = [Process(target=main) for _ in range(10)]
#     for process in processes:
#         process.start()
from asyncio import current_task, Event, Lock, Semaphore, Barrier, Task, run, sleep, create_task


# async def main():
#     for _ in range(10):
#         print(current_task().get_name())


# run(main())


async def async_func1():
    for _ in range(10):
        print(current_task().get_name())
        await sleep(0)


async def async_func2():
    for _ in range(10):
        print(current_task().get_name())
        await sleep(0)


async def async_func3():
    for _ in range(10):
        print(current_task().get_name())
        await sleep(0)


# async def main():
#     tasks = [create_task(async_func1()), create_task(async_func2()), create_task(async_func3())]
#     for task in tasks:
#         await task


# run(main())

from aiohttp import ClientSession


async def get_request():
    async with ClientSession() as session:
        response = await session.get("https://www.21vek.by/")
        print(response.status)


async def main():
    tasks = [create_task(get_request()) for _ in range(10)]
    for task in tasks:
        await task


run(main())
