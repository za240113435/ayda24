import random
# Busqueda lineal(arreglo previamente ordenado)
# Recorremos el arreglo hasta encontrar el valor y devolvemos el indice al encontrar el elemento
# En caso de no entrar el elemento devolvemos -1 que significa que no esta en la lista
def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  # Retorna el índice donde se encuentra el objetivo
    return -1  # Retorna -1 si el objetivo no está en la lista
# Busqueda Binaria(arreglo previamente ordenado)
""" Se definen dos variables izq y der tomando el primer y ultimo indice del arreglo
   Se obtiene la mitad del arreglo que se (medio) promediando el valor de izq y der
        Si
             En caso de ser el elemento se regresa el indice del valor 
        Si no
             se compara sí el elemento a buscar es menor que nuestro valor(medio)
                 Si
                     valor de izq sera = medio + 1
                     lo que nos hace irnos a buscar por el lado izquiedo
                  si no
                      valor der sera medio -1
                      lo que nos hace irnos a buscar del lado derecho
                
"""
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        elemento_medio = lista[medio]

        if elemento_medio == objetivo:
            return medio  # Retorna el índice del objetivo
        elif elemento_medio < objetivo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda

    return -1  # Retorna -1 si el objetivo no está en la lista

# Ejemplo de uso
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# Desordenar la lista
random.shuffle(lista)
#imprimimos lista desordenada
print("Lista desordenada:", lista)

objetivo = 23

# Búsqueda lineal
resultado_lineal = busqueda_lineal(lista, objetivo)
if resultado_lineal != -1:
    print(f"Búsqueda lineal: El elemento {objetivo} se encuentra en el índice {resultado_lineal}")
else:
    print(f"Búsqueda lineal: El elemento {objetivo} no se encontró")

# Ordenar la lista antes de usar búsqueda binaria
lista_ordenada = sorted(lista)
print(f"Lista ordenada para búsqueda binaria: {lista_ordenada}")

# Búsqueda binaria
resultado_binaria = busqueda_binaria(lista_ordenada, objetivo)
if resultado_binaria != -1:
    print(f"Búsqueda binaria: El elemento {objetivo} se encuentra en el índice {resultado_binaria}")
else:
    print(f"Búsqueda binaria: El elemento {objetivo} no se encontró")

    