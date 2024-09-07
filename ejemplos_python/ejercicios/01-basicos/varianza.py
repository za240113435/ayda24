# Pedimos los números al usuario
num1 = eval(input("Escribe el primer número: "))

num2 = eval(input("Escribe el segundo número: "))

num3 = eval(input("Escribe el tercer número: "))

num4 = eval(input("Escribe el cuarto número: "))

num5 = eval(input("Escribe el quinto número: "))

suma = num1 + num2 + num3 + num4 + num5
promedio = suma / 5
varianza = ((num1 - promedio)**2 + (num2 - promedio)**2 + (num3 - promedio)**2 + (num4 - promedio)**2 + (num5 - promedio)**2) / (5-1)

# Escribimos el resulado
print("La varianza es: ", varianza)
