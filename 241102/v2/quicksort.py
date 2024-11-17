#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#Jose Manuel Bautista
import random
import time

CANTIDAD = 1000

def quicksort(lista):
    if len(lista) <= 1:  # Caso base: lista de 0 o 1 elemento ya está ordenada
        return lista
    else:
        # Selecciona el pivote
        pivote = lista[len(lista) // 2]

        # Particiona la lista en tres partes
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]

        # Combina las partes ordenadas
        return quicksort(menores) + iguales + quicksort(mayores)

def es_valido(lista):
    #print(lista)
    tamanio = len(lista)
    esta_ordenado = True

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
    ordenado = quicksort(desordenado)
    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial

    print("Se tardo un total de", tiempo_total, "segundos")

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
