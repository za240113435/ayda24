def busqueda_lineal(lista, objetivo):
    """
    Busca el objetivo en la lista de forma secuencial.
    
    Args:
    - lista: Lista de elementos.
    - objetivo: Elemento a buscar.
    
    Returns:
    - Índice del objetivo si se encuentra, de lo contrario -1.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna el índice donde se encontró
    return -1  # Si no se encuentra, retorna -1


def busqueda_binaria(lista, objetivo):
    """
    Busca el objetivo en una lista ordenada usando el enfoque binario.
    
    Args:
    - lista: Lista ordenada de elementos.
    - objetivo: Elemento a buscar.
    
    Returns:
    - Índice del objetivo si se encuentra, de lo contrario -1.
    """
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Encuentra el punto medio
        if lista[medio] == objetivo:
            return medio  # Elemento encontrado
        elif lista[medio] < objetivo:
            inicio = medio + 1  # Buscar en la mitad derecha
        else:
            fin = medio - 1  # Buscar en la mitad izquierda

    return -1  # Si no se encuentra, retorna -1


# Programa principal
def main():
    print("Selecciona el tipo de búsqueda:")
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")

    opcion = int(input("Opción: "))
    lista = list(map(int, input("Introduce la lista de números separados por espacio: ").split()))
    objetivo = int(input("Introduce el número a buscar: "))

    if opcion == 1:
        print("\n=== Búsqueda Lineal ===")
        resultado = busqueda_lineal(lista, objetivo)
    elif opcion == 2:
        print("\n=== Búsqueda Binaria ===")
        lista.sort()  # Aseguramos que la lista esté ordenada
        print(f"Lista ordenada: {lista}")
        resultado = busqueda_binaria(lista, objetivo)
    else:
        print("Opción no válida.")
        return

    if resultado != -1:
        print(f"El número {objetivo} fue encontrado en el índice {resultado}.")
    else:
        print(f"El número {objetivo} no está en la lista.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
