txt = "Las mejores cosas en la vida son gratis!"
print("La frase es:",txt)

buscar = input("Ingresa la palabra a buscar: ")

if buscar in txt:
    print(buscar,": si se encuentra en la frase")
