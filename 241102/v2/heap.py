import random

CANTIDAD = 10

def heapify(arr, n, i):
    # ... implementación de heapify (igual a la anterior)

def heapSort(arr):
    n = len(arr)
    # Crear una copia de la lista para no modificar la original
    arr_copy = arr.copy()

    # Construir un max-heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr_copy, n, i)

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
        heapify(arr_copy, i, 0)

    return arr_copy

def es_valido(lista):
    # Verificación más eficiente: comparar cada elemento con el siguiente
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

def main():
    desordenado = [random.randint(1, 100) for _ in range(CANTIDAD)]
    ordenado = heapSort(desordenado)

    if not es_valido(ordenado):
        print("No está ordenada")
    else:
        print("La lista SÍ está ordenada")
        print(ordenado)  # Imprimir la lista ordenada

if __name__ == "__main__":
    main()