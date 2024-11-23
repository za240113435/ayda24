def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  # Devuelve el índice del elemento encontrado
    return -1  # Devuelve -1 si el elemento no está en la lista

# Ejemplo de uso
lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_lineal(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Devuelve el índice del elemento encontrado
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1  # Devuelve -1 si el elemento no está en la lista

# Ejemplo de uso
lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")
