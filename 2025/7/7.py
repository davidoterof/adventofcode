import sys


def solve_p1(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    rays = set()
    rays.add(lines[0].index("S"))
    split = 0
    for line in lines[1:]:
        for i in rays.copy():
            if line[i] == "^":
                rays.add(i - 1)
                rays.add(i + 1)
                rays.remove(i)
                split += 1

    print(split)


solve_p1(sys.argv[1])
