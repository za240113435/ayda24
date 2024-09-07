texto = "abcdefghijklmnñopqrstuvwxyz"
num = 0

while num < len(texto):
    if texto[num] == "a" or texto[num] == "e" or texto[num] == "i" or texto[num] == "o" or texto[num] == "u":
        print(texto[num])
    num += 1
