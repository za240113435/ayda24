texto = "abcdefghijklmnñopqrstuvwxyz"
num = 0

while num < len(texto):
    if texto[num] != "a" and texto[num] != "e" and texto[num] != "i" and texto[num] != "o" and texto[num] != "u":
        num += 1
        continue
    print(texto[num])
    num += 1
