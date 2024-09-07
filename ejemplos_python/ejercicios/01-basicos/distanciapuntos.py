import math

# Pedimos los números al usuario
x1 = eval(input("Escribe el número x1: "))

y1 = eval(input("Escribe el número y1: "))

x2 = eval(input("Escribe el número x2: "))

y2 = eval(input("Escribe el número y2: "))

# Calculamos la distancia
distancia =  math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

# Imprimo resultado
print("La distancia es: ", distancia)
