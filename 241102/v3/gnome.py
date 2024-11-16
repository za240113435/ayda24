#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

CANTIDAD = 10


def gnome(lista):
    i = 0
    while i < len(lista):
        if i == 0 or lista[i] >= lista[i - 1]:
            i += 1
        else:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
            i -= 1
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
    ordenado = gnome(desordenado)

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")
    print("Lista ordenada:", ordenado)


if __name__ == "__main__":
    main()
