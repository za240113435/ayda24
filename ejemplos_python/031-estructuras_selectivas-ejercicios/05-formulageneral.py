import math

# Pedimos los número al usuario
a = eval(input("Escribir en número \"a\": "))
b = eval(input("Escribir en número \"b\": "))
c = eval(input("Escribir en número \"c\": "))

# Calculamos la formula 
discriminante = b**2 - 4*a*c

# Si el discriminante es menor a cero
if discriminante < 0:
    print("La solución tiene raices imaginarias.")
elif discriminante == 0:
    print("La solución tiene una sola raiz.")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    # imprimimos resultado
    print("La solución tiene dos raices.")
    print("X1 es:", x1)
    print("X2 es:", x2)
