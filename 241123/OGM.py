import random
import time

CANTIDAD = 1000_000

def busqueda_lineal(lista, elemento):
    # Recorremos toda la lista
    for i in range(len(lista)):
        # Si encontramos el elemento, retornamos su índice
        if lista[i] == elemento:
            return i
    # Si el elemento no se encuentra, retornamos -1
    return -1

def busqueda_binaria(lista, elemento):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2  # Índice medio
        if lista[medio] == elemento:  # Elemento encontrado
            return medio
        elif lista[medio] < elemento:  # Buscar en la mitad derecha
            bajo = medio + 1
        else:  # Buscar en la mitad izquierda
            alto = medio - 1
    
    # Si el elemento no se encuentra
    return -1

def main():
    lista = [random.randint(1, 100) for _ in range(CANTIDAD)]
    elemento_a_buscar = 8

    tiempo_inicial = time.time()
    resultado = busqueda_lineal(lista, elemento_a_buscar)
    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    print("Busqueda lineal Se tardo un total de", tiempo_total, "segundos")
    """
    tiempo_inicial = time.time()
    resultado = busqueda_binaria(lista, elemento_a_buscar)
    "tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicial
    print("Busqueda binaria Se tardo un total de", tiempo_total, "segundos")
    """
    if resultado != -1:
        print(f"El elemento {elemento_a_buscar} se encuentra en el índice {resultado}")
    else:
        print(f"El elemento {elemento_a_buscar} no se encuentra en la lista")
                
if __name__ == "__main__":
    main()