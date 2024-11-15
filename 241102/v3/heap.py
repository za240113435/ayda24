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


def heapify(arr, n, i):
    largest = i  # Inicializa el nodo más grande como raíz
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar

        # Recursivamente heapificar el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un heap (max-heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Uno a uno extraer elementos del heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover la raíz actual al final
        heapify(arr, i, 0)  # Llamar a heapify en el heap reducido

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Array original:", arr)

heap_sort(arr)
print("Array ordenado:", arr)




if __name__ == "__main__":
    main()
