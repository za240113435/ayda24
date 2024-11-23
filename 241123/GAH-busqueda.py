#!/usr/bin/env python3

def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  # Devuelve el índice si encuentra el elemento
    return -1  # Devuelve -1 si no se encuentra el elemento

def busqueda_binaria(lista, objetivo, inicio, fin):
    if inicio > fin:
        return -1  # Elemento no encontrado

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)

if __name__ == "__main__":
    lista = [10, 20, 30, 40, 50, 60]
    objetivo = 11

    #resultado = busqueda_binaria(lista, objetivo, 0, len(lista) - 1)

    resultado = busqueda_lineal(lista, objetivo)
    
    if resultado != -1:
        print(f"Elemento encontrado en el índice {resultado}.")
    else:
        print("Elemento no encontrado.")
