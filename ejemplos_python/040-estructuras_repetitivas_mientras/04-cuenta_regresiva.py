import time
contador = 10

while contador > 0:
    print(contador)
    contador -= 1 # es lo mismo que: contador = contador - 1
    time.sleep(1)

print("Despegue")
