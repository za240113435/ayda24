# Función de Búsqueda Lineal
def busqueda_lineal(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i  # Retorna el índice donde se encuentra el valor
    return -1  # Si no se encuentra el valor, retorna -1

# Función de Búsqueda Binaria
def busqueda_binaria(lista, valor_buscado):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2  # Encuentra el índice medio
        if lista[medio] == valor_buscado:
            return medio  # El valor fue encontrado
        elif lista[medio] < valor_buscado:
            bajo = medio + 1  # El valor está en la mitad derecha
        else:
            alto = medio - 1  # El valor está en la mitad izquierda
    
    return -1  # Si el valor no se encuentra

# Función principal
def main():
    # Lista de ejemplo (debe estar ordenada para la búsqueda binaria)
    mi_lista = [10, 20, 30, 40, 50]
    
    # Solicitar al usuario el valor a buscar
    valor = int(input("Introduce el valor a buscar: "))
    
    # Solicitar al usuario qué tipo de búsqueda desea realizar
    tipo_busqueda = input("Elige el tipo de búsqueda (lineal/binaria): ").lower()
    
    if tipo_busqueda == "lineal":
        resultado = busqueda_lineal(mi_lista, valor)
        if resultado != -1:
            print(f"Elemento encontrado en el índice {resultado} usando búsqueda lineal.")
        else:
            print("Elemento no encontrado usando búsqueda lineal.")
    
    elif tipo_busqueda == "binaria":
        # Asegúrate de que la lista esté ordenada para la búsqueda binaria
        resultado = busqueda_binaria(mi_lista, valor)
        if resultado != -1:
            print(f"Elemento encontrado en el índice {resultado} usando búsqueda binaria.")
        else:
            print("Elemento no encontrado usando búsqueda binaria.")
    
    else:
        print("Opción no válida. Debes elegir 'lineal' o 'binaria'.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
