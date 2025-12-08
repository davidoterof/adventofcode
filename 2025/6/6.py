import operator
import sys
from functools import reduce

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


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


solve_p1(sys.argv[1])
