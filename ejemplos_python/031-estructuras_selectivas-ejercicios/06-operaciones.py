print("    Menu")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
la_opcion = eval(input("Opción: "))

num1 = eval(input("Escribe el primer número: "))
num2 = eval(input("Escribe el segundo número: "))

if la_opcion == 1:
    print("La suma es", num1 + num2)
elif la_opcion == 2:
    print("La resta es", num1 - num2)
elif la_opcion == 3:
    print("La multiplicación es", num1 * num2)
elif la_opcion == 4:
    if num2 == 0:
        print("No se puede dividir entre cero")
    else:
        print("La división es", num1 / num2)
