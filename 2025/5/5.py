import sys

##########################
# part 1
##########################


# idea: keep a set of valid ids and a set of read ids, then do intersection
# oom
def solve_p1_1(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    ranges = True
    valid_ids = set()
    read_ids = set()
    for line in lines:
        line = line.strip()
        if line == "":
            ranges = not ranges
            continue

        if ranges:
            parts = line.split("-")
            init = parts[0]
            end = parts[1]
            valid_ids.update(range(int(init), int(end) + 1))
        else:
            ID = int(line)
            read_ids.add(ID)

    count_valid = len(read_ids.intersection(valid_ids))
    print(count_valid)


# idea: read ranges into a list, then for each read id check if it is in any range
# works
def solve_p1_2(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    ranges = True
    ranges_list = []
    read_ids = []
    count_valid = 0
    for line in lines:
        line = line.strip()
        if line == "":
            ranges = not ranges
            continue

        if ranges:
            parts = line.split("-")
            init = parts[0]
            end = parts[1]

            ranges_list.append((int(init), int(end)))
        else:
            ID = int(line)
            read_ids.append(ID)

    for read_id in read_ids:
        for init, end in ranges_list:
            if int(init) <= read_id <= int(end):
                count_valid += 1
                break
    print(count_valid)


##########################
# part 2
##########################


# idea: merge overlapping rankges, then sum their lengths
# works
def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]

    for current in ranges[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged


def solve_p2_1(ruta):
    with open(ruta, "r") as file:
        lines = file.readlines()

    ranges = True
    ranges_list = []
    for line in lines:
        line = line.strip()
        if line == "":
            ranges = not ranges
            continue

        if ranges:
            parts = line.split("-")
            init = parts[0]
            end = parts[1]

            ranges_list.append((int(init), int(end)))
        else:
            pass

    merged_ranges = merge_ranges(ranges_list)
    count_valid = 0
    for init, end in merged_ranges:
        count_valid += end - init + 1
    print(count_valid)


solve_p2_1(sys.argv[1])
