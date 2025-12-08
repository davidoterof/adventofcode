import sys


def euclidean_distance(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def merge_circuits(circuits):
    merged = []
    while circuits:
        current = circuits.pop(0)
        merged_flag = False
        for i in range(len(merged)):
            if not current.isdisjoint(merged[i]):
                merged[i] = merged[i].union(current)
                merged_flag = True
                break
        if not merged_flag:
            merged.append(current)
    return merged


def solve_p1_1(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    points = []
    for line in lines:
        x, y, z = map(float, line.strip().split(","))
        points.append((x, y, z))

    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dist = euclidean_distance(p1[0], p1[1], p1[2], p2[0], p2[1], p2[2])
            distances.append((dist, i, j))

    distances.sort(key=lambda x: x[0])
    count = 1
    circuits = []
    for dist, i, j in distances:
        print(f"Distance between point {i} and point {j}: {dist:.2f}")
        if len(circuits) == 0:
            circuits.append({i, j})
        else:
            found = False
            for circuit in circuits:
                if i in circuit or j in circuit:
                    circuit.add(i)
                    circuit.add(j)
                    found = True
                    break
            if not found:
                circuits.append({i, j})
            # merge circuits if needed
            circuits = merge_circuits(circuits)
        if count >= 1000:
            break
        count += 1

    circuits.sort(key=lambda x: len(x), reverse=True)
    circuits = circuits[:3]
    result = 1
    for circuit in circuits:
        result *= len(circuit)
    print(result)


solve_p1_1(sys.argv[1])
