opcion_menu = 0
lista = []

while opcion_menu != 9:
    print("   Menú")
    print("1. Inicializar lista")
    print("2. Agregar elemento")
    print("3. Buscar un elemento")
    print("4. Eliminar un elemento")
    print("5. Remplazar un elemento")
    print("6. Número de elementos")
    print("7. Ordernar lista")
    print("8. Imprimir lista")
    print("9. Salir")
    
    opcion_menu = eval(input("Opcion: "))
    
    if opcion_menu == 1:
        lista = list()
    elif opcion_menu == 2:
        elemento = input("Ingresa un nuevo elemento: ")
        lista.append(elemento)
    elif opcion_menu == 3:
        elemento = input("Ingresa elemento a buscar: ")
        if elemento in lista:
            posicion = lista.index(elemento)
            print("La posición es:", posicion)
        else:
            print("Elemento NO encontrado")    
    elif opcion_menu == 4:
        elemento = input("Ingresa elemento a borrar: ")
        if elemento in lista:
            lista.remove(elemento)
        else:
            print("Elemento NO encontrado")    
    elif opcion_menu == 5:
        elemento = input("Ingresa elemento a remplazar: ")
        if elemento in lista:
            posicion = lista.index(elemento)
            nuevo = input("Ingresa un nuevo elemento: ")
            lista[posicion] = nuevo
        else:
            print("Elemento NO encontrado")    
    elif opcion_menu == 6:
        print(len(lista))
    elif opcion_menu == 7:
        lista.sort()
    elif opcion_menu == 8:
        print(lista)
    elif opcion_menu == 9:
        pass
    else:
        print("Opción invalida")
    