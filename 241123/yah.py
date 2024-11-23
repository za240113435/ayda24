"""
Busqueda lineal y busqueda binaria
"""


def busqueda_binaria(lista, elemento):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Args:
      lista: Una lista ordenada de elementos.
      elemento: El elemento a buscar.

    Returns:
      El índice del elemento si se encuentra, -1 en caso contrario.
    """

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def busqueda_secuencial(lista, elemento):
    """
    Realiza una búsqueda secuencial en una lista.

    Args:
      lista: Una lista de elementos.
      elemento: El elemento a buscar.

    Returns:
      El índice del elemento si se encuentra, -1 en caso contrario.
    """

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


def main():
    """
    Busqueda de elmentos
    """
    lista = [x for x in range(100)]

    n = eval(input("Escribe un número entre 0 y 99: "))

    encontrado = busqueda_binaria(lista, n)

    if encontrado != -1:
        print("Si se encontró el número")
    else:
        print("NO se encontró el número")

    encontrado = busqueda_secuencial(lista, n)

    if encontrado != -1:
        print("Si se encontró el número")
    else:
        print("NO se encontró el número")


if __name__ == "__main__":
    main()
