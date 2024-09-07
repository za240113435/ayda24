import math
import menu
import funciones

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
    
    
    