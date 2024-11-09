#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import time

CANTIDAD = 10_000


def burbuja(lista):  # T(n) =  9n(n-1) + 2 ->  9n^2 - 9n + 2 => n^2
    # T(10,000) = 3s -> 9(10,000)^2 + 9(10,000) + 2 ->  n^2
    # T(100,000) =  T(10,000 x 10) -> 3s x 10^2 -> 3 x 100 -> 300s
    tamanio = len(lista)  # 1

    for i in range(tamanio):  # n -> 9n(n-1)
        for j in range(tamanio - i - 1):  # n - i - 1  -> 9(n-1)
            if lista[j] > lista[j + 1]:  # 3 + 6 = 9
                # Intercambia los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # 6

    return lista  # 1


def es_valido(lista):
    tamanio = len(lista)
    esta_ordenado = False

    for pos in range(tamanio - 1):
        if lista[pos] > lista[pos + 1]:
            break
    else:
        esta_ordenado = True

    return esta_ordenado


def main():
    # Caso promedio
    # desordenado = [random.randint(1, 100) for _ in range(CANTIDAD)]  # nosec B311
    # Mejor caso
    # Este si esta ordenado
    # desordenado = [x for x in range(CANTIDAD)]  # nosec B311
    # Peor caso
    # Este esta ordenado a la inversa
    # desordenado = [CANTIDAD-x for x in range(CANTIDAD)]
    desordenado = [x for x in range(CANTIDAD, 0, -1)]

    tiempo_inicial = time.time()
    # Algoritmo de ordenamiento
    ordenado = burbuja(desordenado)
    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial

    print("Se tardo un total de", tiempo_total, "segundos")

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
