import sys

import numpy as np


def aux(lines, count):
    sum = 0

    for line in lines:
        number_s = line.strip()
        biggest = -1
        b_i = -1
        start = 0
        indexes = np.array([])
        for i in np.arange(count - 1, -1, -1):
            for j in np.arange(start, len(number_s) - i):
                n1 = int(number_s[j])
                if n1 > biggest:
                    biggest = n1
                    b_i = j
            start = b_i + 1
            indexes = np.append(indexes, b_i)
            b_i = -1
            biggest = -1
        fns = int("".join(number_s[int(i)] for i in indexes))
        sum += fns

    return sum


def solve(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    print(aux(lines, 2))  # part 1
    print(aux(lines, 12))  # part 2


solve(sys.argv[1])
