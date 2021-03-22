"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    counter = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if i + j + k + l == 14:
                        counter += 1
    return counter


# A = [1, 2, 3, 4, 5, 6]
# B = [5, 2, 7, 9, 3, 6]
# C = [1, 4, 2, 1, 6, 0]
# D = [0, 1, 4, 2, 7, 3]
#
# print(check_sum_of_four(A, B, C, D))
