import sys

import numpy as np


def reloj(valor, cambio):
    zero_count = 0
    for _ in np.arange(0, abs(cambio)):
        if cambio > 0:
            valor += 1
        else:
            valor -= 1

        if valor > 99:
            valor = 0
        elif valor < 0:
            valor = 99

        if valor == 0:
            zero_count += 1
    return valor, zero_count


def solve(ruta):
    with open(ruta, "r") as f:
        position = 50
        count_0 = 0
        count_pasos = 0
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue

            letra = linea[0]
            numero = int(linea[1:])

            if letra == "L":
                position, pasos = reloj(position, -numero)
            elif letra == "R":
                position, pasos = reloj(position, numero)

            count_pasos += pasos

            if position == 0:
                count_0 += 1

        print(count_0)
        print(count_pasos)


solve(sys.argv[1])
