num1 = eval(input("Escribe el primer número: "))
num2 = eval(input("Escribe el segundo número: "))
num3 = eval(input("Escribe el tercer número: "))

if num1 > num2:
    if num1 > num3:
        print("El primer número es mayor")
    else:
        print("El tercer número es mayor")
else:
    if num2 > num3:
        print("El segundo número es mayor")
    else:
        print("El tercer número es mayor")
