import operator
import sys
from functools import reduce

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


# part 1
def solve_p1(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    n_operations = len(lines[0].strip().split())
    arrays = [[] for _ in range(n_operations)]
    operations = lines[-1].strip().split()
    data = lines[:-1]
    for line in data:
        numbers = line.strip().split()
        for i, elem in enumerate(numbers):
            arrays[i].append(int(elem))

    result = sum(
        [reduce(ops[operacion], array) for operacion, array in zip(operations, arrays)]
    )

    print(int(result))


# part 2
def solve_p2(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()
    lines = [line.rstrip("\n") for line in lines]
    n_columns = len(lines[0])

    data = lines[:-1]
    lend = len(data)
    numbers = []
    total = 0
    for i in range(n_columns - 1, -1, -1):
        number = ""
        for j in range(lend):
            if lines[j][i] != " ":
                number += lines[j][i]
        if number != "":
            numbers.append(int(number))

        if lines[lend][i] in ops:
            operacion = lines[lend][i]
            result = reduce(ops[operacion], numbers)
            total += result
            numbers = []

    print(int(total))


solve_p2(sys.argv[1])
