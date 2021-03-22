"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    minimum = None
    maximum = None
    with open("some_file.txt") as fi:
        for line in fi:
            to_check = line.strip()
            if maximum is None:
                maximum = to_check
            elif maximum < to_check:
                maximum = to_check

            if minimum is None:
                minimum = to_check
            elif minimum > to_check:
                minimum = to_check

    return (minimum, maximum)


# print(find_maximum_and_minimum("some_file.txt"))
