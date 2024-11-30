#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
CANTIDAD = 10

def heapsort(lista):
    return lista

def heapify(arr, n, i):
    # Inicializa el elemento más grande como la raíz
    largest = i
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el elemento más grande actual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el elemento más grande no es la raíz, intercambia y heapifica
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambia
        heapify(arr, n, largest)  # Llama recursivamente para el subárbol afectado
        
    return arr_copy

def heap_sort(arr):
    n = len(arr)

    # Construye el max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrae los elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        # Mueve la raíz al final
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


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
    ordenado = heapsort(desordenado)

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
