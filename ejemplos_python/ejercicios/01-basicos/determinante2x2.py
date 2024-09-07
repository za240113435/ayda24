# Pedimos los números al usuario
a11 = eval(input("Escribe el número a11: "))

a22 = eval(input("Escribe el número a22: "))

a12 = eval(input("Escribe el número a12: "))

a21 = eval(input("Escribe el número a21: "))

# Calculamos el determinante
determinante = a11*a22 - a12*a21

# Imprimo resultado
print("El determinate es: ", determinante)
