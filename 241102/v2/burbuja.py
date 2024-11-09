#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time

CANTIDAD = 10


def burbuja(lista):
    tamanio = len(lista)

    for i in range(tamanio - 1):
        for j in range(tamanio - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


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
    desordenado = [random.randint(1, 100) for _ in range(CANTIDAD)]  # nosec B311
    # Este si esta ordenado
    # desordenado = [ x for x in range(CANTIDAD) ]

    tiempo_inicial = time.time()
    # Algoritmo de ordenamiento

    # Lista desordenada
    print("Lista desordenada:", desordenado)

    # Burbuja
    ordenado = burbuja(desordenado)
    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial

    print("Se tardo un total de", tiempo_total, "segundos")

    # Lista ordenada
    print("Lista ordenada:", ordenado)

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
