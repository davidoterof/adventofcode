import sys

# part 1
def rectangle_area(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    h = abs(y2 - y1) + 1
    w = abs(x2 - x1) + 1
    return h * w

def solve_p1(input_path):
    with open(input_path, "r") as f:
        lines = f.readlines()
    
    points = []
    for line in lines:
        parts = line.strip().split(",")
        point = (int(parts[0]), int(parts[1]))
        points.append(point)

    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point_a = points[i]
            point_b = points[j]
            area = rectangle_area(point_a, point_b)
            if area > max_area:
                max_area = area

    print(max_area)

solve_p1(sys.argv[1])
