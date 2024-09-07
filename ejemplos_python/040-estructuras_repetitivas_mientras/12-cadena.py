texto = "abcdefghijklmnñopqrstuvwxyz"
#texto = "Una casa rosa en la playa"
#texto = texto.lower()
num = 0
una_linea=""
while num < len(texto):
    if texto[num] == "a" or texto[num] == "e" or texto[num] == "i" or texto[num] == "o" or texto[num] == "u":
        una_linea += texto[num]
    num += 1

print(una_linea)