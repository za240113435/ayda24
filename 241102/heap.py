#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time

CANTIDAD = 10_000_000


def heapify(lista, n, i):
    # Encuentra el nodo más grande entre el nodo raíz, el hijo izquierdo y el hijo derecho
    mayor = i  # Inicializar el nodo más grande como la raíz
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # Si el hijo izquierdo es mayor que la raíz
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda

    # Si el hijo derecho es mayor que el mayor hasta ahora
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha

    # Si el nodo más grande no es la raíz, intercambiarlos
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        # Recursivamente aplicar el heapify en el nodo afectado
        heapify(lista, n, mayor)

def heapsort(lista):
    n = len(lista)

    # Construir el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        # Mover el elemento raíz actual al final
        lista[i], lista[0] = lista[0], lista[i]
        # Llamar a heapify en el heap reducido
        heapify(lista, i, 0)

    return lista


def es_valido(lista):
    print(lista)
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
    ordenado = heapsort(desordenado)
    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial

    print("Se tardo un total de", tiempo_total, "segundos")

    if not es_valido(ordenado):
        print("No esta ordenado")
    else:
        print("La lista SI esta ordenada")


if __name__ == "__main__":
    main()
