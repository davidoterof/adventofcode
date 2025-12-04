import sys


def check_position_p1(matrix, i, j, rows, colums):
    if matrix[i][j] != "@":
        return 0

    directions = [
        (-1, -0),
        (-1, -1),
        (0, -1),
        (+1, -1),
        (+1, +1),
        (0, +1),
        (-1, +1),
        (+1, 0),
    ]
    count = 0
    for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        if ni < 0 or ni >= rows or nj < 0 or nj >= colums:
            continue
        if matrix[ni][nj] == "@":
            count += 1
        if count >= 4:
            return 0
    return 1


def check_position_p2(matrix, i, j, rows, colums):
    if matrix[i][j] != "@":
        return matrix, 0

    directions = [
        (-1, -0),
        (-1, -1),
        (0, -1),
        (+1, -1),
        (+1, +1),
        (0, +1),
        (-1, +1),
        (+1, 0),
    ]
    count = 0
    for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        if ni < 0 or ni >= rows or nj < 0 or nj >= colums:
            continue
        if matrix[ni][nj] == "@":
            count += 1
        if count >= 4:
            return matrix, 0

    matrix[i][j] = "x"
    return matrix, 1


def solve(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    # part 1
    matrix = [list(line.strip()) for line in lines]
    rows = len(matrix)
    colums = len(matrix[0])
    sum_1 = 0
    for i in range(rows):
        for j in range(colums):
            sum_1 += check_position_p1(matrix, i, j, rows, colums)

    print(f"Part 1: {sum_1}")

    # part 2
    matrix = [list(line.strip()) for line in lines]
    rows = len(matrix)
    colums = len(matrix[0])
    removed = -1
    total_removed = 0
    while removed != 0:
        sum_1 = 0
        for i in range(rows):
            for j in range(colums):
                matrix, valid = check_position_p2(matrix, i, j, rows, colums)
                sum_1 += valid
        removed = sum_1
        total_removed += removed

    print(f"Part 2: {total_removed}")


solve(sys.argv[1])
