#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import time

CANTIDAD = 10000

def seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

def es_valido(lista):
    print(lista)
    tamanio = len(lista)
    for pos in range(tamanio - 1):
        if lista[pos] > lista[pos + 1]:  # Aquí verificamos si algún elemento es mayor al siguiente
            return False  # Retorna False inmediatamente si la lista no está en orden ascendente
    return True  # Retorna True si todos los elementos están en orden

def main():
    desordenado = [random.randint(1, 100) for _ in range(CANTIDAD)]  # nosec B311

    tiempo_inicial = time.time()
    # Algoritmo de ordenamiento
    ordenado = seleccion(desordenado)
    tiempo_final = time.time()

    tiempo_total = tiempo_final - tiempo_inicial
    
    print("Se tardó un total de", tiempo_total, "segundos")

    if not es_valido(ordenado):
        print("No está ordenado")
    else:
        print("La lista SÍ está ordenada")

if __name__ == "__main__":
    main()

