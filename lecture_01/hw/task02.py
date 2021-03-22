"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    data = sorted(data)
    start_fib = min(data)
    fin_fib = max(data)
    true_fib = list(fib(fin_fib))
    print(true_fib)
    fin_ind = true_fib.index(start_fib)
    return true_fib[fin_ind:] == data


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        if a <= n:
            yield a
            a, b = b, a + b


# print(list(fib(8)))
#
# data_to_process = [
#     0,
#     1,
#     1,
#     2,
#     3,
#     5,
#     8,
#     13,
#     21,
#     34,
#     55,
#     89,
#     144,
#     233,
#     377,
#     610,
#     987,
#     1597,
#     2584,
#     4181,
#     6765,
# ]
#
# print(check_fibonacci(data_to_process))


# def _check_window(x: int, y: int, z: int) -> bool:
#     return (x + y) == z
#
#
# data_to_process = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
#
#
# assert len(data_to_process) >= 3
#
# a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
#
# while data_to_process:
#     if not _check_window(a, b, c):
#         raise ValueError("Invalid data")
#
#     a, b, c = b, c, data_to_process[0]
#     data_to_process = data_to_process[1:]
#
# print("it's a fib sequence!")
