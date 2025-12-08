import sys


# part 1
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


# part 2
def solve_p2(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    caminos = [0 for _ in range(len(lines[0].strip()))]
    caminos[lines[0].index("S")] += 1
    for line in lines[2:]:
        for i in range(len(line)):
            if line[i] == "^":
                caminos[i - 1] += caminos[i]
                caminos[i + 1] += caminos[i]
                caminos[i] = 0

    print(sum(caminos))


solve_p2(sys.argv[1])
