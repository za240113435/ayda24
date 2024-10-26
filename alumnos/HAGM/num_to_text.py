#!/usr/bin/env python3

def unidades(n):
    return ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"][n]

def especiales(n):
    return ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"][n - 10]

def decenas(n):
    palabras = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    diez_unidad = n % 10
    return palabras[n // 10] + ((" y " + unidades(diez_unidad)) if diez_unidad > 0 else "")

def centenas(n):
    if n == 100:
        return "cien"
    palabras = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    centena = palabras[n // 100]
    resto = n % 100
    return centena + (" " + numero_a_letra(resto) if resto else "")

def miles(n):
    mil = n // 1000
    resto = n % 1000
    if mil == 1:
        return "mil " + numero_a_letra(resto) if resto else "mil"
    else:
        return numero_a_letra(mil) + " mil" + (" " + numero_a_letra(resto) if resto else "")

def millones(n):
    millon = n // 1000000
    resto = n % 1000000
    if millon == 1:
        return "un millón" + (" " + numero_a_letra(resto) if resto else "")
    else:
        return numero_a_letra(millon) + " millones" + (" " + numero_a_letra(resto) if resto else "")

def numero_a_letra(n):
    if n < 10:
        return unidades(n)
    elif n < 20:
        return especiales(n)
    elif n < 100:
        return decenas(n)
    elif n < 1000:
        return centenas(n)
    elif n < 1000000:
        return miles(n)
    elif n <= 1000000000:
        return millones(n)
    else:
        return "Número fuera de rango"

if __name__ == "__main__":
    numero = int(input("Introduce un número: "))
    print(numero_a_letra(numero))
