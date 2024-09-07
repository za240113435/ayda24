import math

# Pedimos los números al usuario
a = eval(input("Escribe el número a: "))
	
b = eval(input("Escribe el número b: "))
	
c = eval(input("Escribe el número c: "))
	
# Calculamos la formula
discrimeante = b**2 - 4*a*c
	
x1 = (-b + math.sqrt(discrimeante)) / (2*a)
x2 = (-b - math.sqrt(discrimeante)) / (2*a)

# Imprimo resultado
print("X1 es: ", x1)
print("X2 es: ", x2)
