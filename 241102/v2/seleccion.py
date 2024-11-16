#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time

CANTIDAD = 10


def seleccion(lista):
       # Algoritmo de ordenamiento por selección
    for i in range(len(lista)):
        # Encontrar el índice del elemento más pequeño en la parte no ordenada
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiar el elemento encontrado con el primero de la parte no ordenada
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
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
    
    tiempo_inicial = time.time()
   # Este si esta ordenado
    # desordenado = [ x for x in range(CANTIDAD) ]

    # Algoritmo de ordenamiento
    ordenado = seleccion(desordenado)

    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial

    print("Se tardo un total de", tiempo_total, "segundos")

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
