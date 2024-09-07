# Imprimir un mensaje si el bloque try genera un NameError
# y otro para otros errores:
try:
    print(x)
except NameError:
    print("La variable x no esta definida")
except:
    print("Algo más salio mal")
