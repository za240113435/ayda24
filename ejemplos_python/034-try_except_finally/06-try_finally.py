# Con finally, siempre se ejecuta
try:
    print(x)
except:
    print("Algo salio mal")
finally:
    print("El bloque de 'try except' ha terminado")
