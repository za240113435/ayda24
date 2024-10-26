#!/usr/bin/env python3

from num2words import num2words

# Número que quieres convertir
numero = int(input("Ingresa un numero: "))

# Convertir el número a palabras en español
numero_en_letras = num2words(numero, lang='es')

print(numero_en_letras)