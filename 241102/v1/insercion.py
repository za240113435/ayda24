#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

CANTIDAD = 10


def insercion(lista):
    print(lista)
    # Traverse through 1 to len(lista)
    for i in range(1, len(lista)):
        key = lista[i]  # Element to be compared
        j = i - 1
        
        # Move elements of lista[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key  # Place the key in its correct position
    return lista


def es_valido(lista):
    tamanio = len(lista)
    esta_ordenado = False

    for pos in range(tamanio - 1):
        if lista[pos] >= lista[pos + 1]:
            break
    else:
        esta_ordenado = True

    return esta_ordenado


def main():
    desordenado = [random.randint(1, 100) for _ in range(CANTIDAD)]  # nosec B311
    # Este si esta ordenado
    # desordenado = [ x for x in range(CANTIDAD) ]

    # Algoritmo de ordenamiento
    ordenado = insercion(desordenado)

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
