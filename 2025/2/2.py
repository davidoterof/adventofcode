import sys

import numpy as np

def solve(ruta):
    with open(ruta, 'r') as file:
        lines = file.readline().strip()
    
    sum_1 = 0
    rangos = lines.split(',')
    sum_2 = 0
    for rango in rangos:
        inicio, fin = rango.split('-')
        for i in range(int(inicio), int(fin) + 1):
            nstr = str(i)

            # part 1
            if len(nstr) % 2 == 0:
                middle = (len(nstr) // 2) - 1
                first = nstr[:middle + 1]
                second = nstr[middle + 1:]
                if first == second:
                    sum_1 += i
            
            # part 2
            for lon in np.arange(1,len(nstr) // 2 + 1):
                sequence = nstr[0:lon]
                chunks = [nstr[i:i+lon] for i in range(lon, len(nstr), lon)]
                count = 0
                for chunk in chunks:
                    if sequence != chunk:
                        break
                    count += 1

                if count == len(chunks):
                    sum_2 += i
                    print(f"i: {i}, lon: {lon}, sequence: {sequence}, chunks: {chunks}")
                    break

    print(f"Part 1: {sum_1}")
    print(f"Part 2: {sum_2}")


solve(sys.argv[1])
