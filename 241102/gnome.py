#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time

CANTIDAD = 1000

def gnome(lista):
    index = 0
    while index < len(lista):
        if index == 0:
            index += 1
        if lista[index] >= lista[index - 1]:
            index += 1
        else:
            # Intercambiar los elementos
            lista[index], lista[index - 1] = lista[index - 1], lista[index]
            index -= 1
    return lista

def es_valido(lista):
    print(lista)
    tamanio = len(lista)
    esta_ordenado = False

    for pos in range(tamanio - 1):
        if lista[pos] > lista[pos + 1]:  # Cambié >= a > para mayor claridad
            break
    else:
        esta_ordenado = True

    return esta_ordenado

def main():
    desordenado = [random.randint(1, 100) for _ in range(CANTIDAD)]

    tiempo_inicial = time.time()
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    # Algoritmo de ordenamiento
    ordenado = gnome(desordenado)
    print("Se tardo un total de", tiempo_total, "segundos")

    # print("Lista original:", desordenado)
    # print("Lista ordenada:", ordenado)

    if not es_valido(ordenado):
        print("No está ordenado")
    else:
        print("La lista SÍ está ordenada")

if __name__ == "__main__":
    main()
