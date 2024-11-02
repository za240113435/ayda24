#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

CANTIDAD = 10


def insercion(lista):
    # Recorre desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        key = lista[i]  # Elemento a ser colocado en la posición correcta
        j = i - 1

        # Mueve los elementos de lista[0...i-1] que son mayores que la clave un lugar adelante
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        # Coloca la clave en su posición correcta
        lista[j + 1] = key

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
