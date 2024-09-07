pila = []

n = eval(input("Cuantos números quieres ingresar: "))

for contador in range(n):
    numero = eval(input("Ingresa un número: "))
    pila.append(numero)
    
pila.pop()

numero = eval(input("Ingresa otro número: "))
pila.append(numero)

print(pila)

print(len(pila))