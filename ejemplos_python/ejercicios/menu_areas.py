def menu():
    print("   Menu ")
    print("1. Área de rectangulo")
    print("2. Área de cuadrado")
    print("3. Área de triangulo")
    print("4. Área de ciruclo")
    print("5. Salir")
    opcion = eval(input("Opcion: "))
    return opcion

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

opcion_menu = 0
while opcion_menu != 5:
    opcion_menu = menu.menu()
    
    if opcion_menu == 1:
        base = eval(input("Escribe la base: "))
        altura = eval(input("Escribe la altura: "))
        print("El resultado es", funciones.area_rectangulo(base, altura))
    elif opcion_menu == 2:
        lado = eval(input("Escribe el valor del lado: "))
        area = funciones.area_rectangulo(lado, lado)
        print("El resultado es", area)
    elif opcion_menu == 3:
        base = eval(input("Escribe la base: "))
        altura = eval(input("Escribe la altura: "))
        print("El resultado es", funciones.area_triangulo(base, altura))
    elif opcion_menu == 4:
        pass
    elif opcion_menu == 5:
        pass
    else:
        print("ERROR: Opción no valida")