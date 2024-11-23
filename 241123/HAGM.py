import random


CANTIDAD = 20

def lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1

    while inicio <= fin:
        medio = inicio + (fin - inicio) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


def main():
    lista = [random.randint(1, 100) for _ in range(CANTIDAD)]
    objetivo = random.choice(lista)  # Seleccionar un número aleatorio de la lista como objetivo

    print(f"\nLista generada: {lista}")
    print(f"Número a buscar: {objetivo}")

    print("\nBúsqueda Lineal")
    resultado_lineal = lineal(lista, objetivo)
    if resultado_lineal != -1:
        print(f"Encontrado en el índice {resultado_lineal}.")
    else:
        print(f"Número {objetivo} no está en la lista.")

    print("\nBúsqueda Binaria")
    lista_ordenada = sorted(lista)
    print(f"Lista ordenada para la búsqueda binaria: {lista_ordenada}")
    resultado_binaria = binaria(lista_ordenada, objetivo)
    if resultado_binaria != -1:
        print(f"Encontrado en el índice {resultado_binaria}.")
    else:
        print(f"Número {objetivo} no está en la lista.")


if __name__ == "__main__":
    main()
