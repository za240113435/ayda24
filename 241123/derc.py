def busqueda_lineal(lista, objetivo):
    # Recorremos todos los elementos de la lista
    for i in range(len(lista)):
        # Si encontramos el elemento que estamos buscando
        if lista[i] == objetivo:
            return i  # Devolvemos el índice donde se encuentra el objetivo
    return -1  # Si no lo encontramos, devolvemos -1

def busqueda_binaria(lista, objetivo):
    # Definir los límites superior e inferior
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2  # Calcular el índice medio
        # Si encontramos el objetivo en el medio
        if lista[medio] == objetivo:
            return medio  # Devolvemos el índice del elemento
        # Si el objetivo es mayor que el valor en medio, buscamos en la mitad superior
        elif lista[medio] < objetivo:
            bajo = medio + 1
        # Si el objetivo es menor que el valor en medio, buscamos en la mitad inferior
        else:
            alto = medio - 1
    
    return -1  # Si no encontramos el objetivo, devolvemos -1

# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13]
objetivo = 7
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado.")


# Ejemplo de uso
lista = [5, 3, 8, 6, 7, 2]
objetivo = 7
resultado = busqueda_lineal(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado.")