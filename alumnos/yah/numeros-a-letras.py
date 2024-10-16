#!/usr/bin/env python3
"""
Programa que convierte de números a letras
"""

PRIMEROS = (
    "cero",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
)

SEGUNDOS = (
    "",
    "dieci",
    "veinti",
    "treinta",
    "cuarenta",
    "cincuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "noventa",
)


def numero_a_letra(numero):
    """Función que convierte el número a letras"""

    en_letra = ""
    tamanio = len(numero)

    if tamanio == 1:
        en_letra = PRIMEROS[int(numero)]
    elif tamanio == 2:
        if numero[0] == "1" and numero[1] < "6":
            en_letra = PRIMEROS[int(numero)]
        elif numero == "20":
            en_letra = SEGUNDOS[int(numero[0])][:-1] + "e"
        elif numero[1] == "0":
            en_letra = SEGUNDOS[int(numero[0])]
        elif numero < "31":
            en_letra = SEGUNDOS[int(numero[0])] + PRIMEROS[int(numero[1])]
        else:
            en_letra = SEGUNDOS[int(numero[0])] + " y " + PRIMEROS[int(numero[1])]

    return en_letra


def ingresa_numero():
    """Función que devuelve un número en formato str"""

    numero = input("Ingresa un número entero positivo: ")

    while not numero.isdecimal():
        print("No es un número entero, por favor ", end="")
        numero = input("ingresa un número entero positivo: ")

    return numero


def main():
    """
    Función principal
    """
    numero = ingresa_numero()

    en_letra = numero_a_letra(numero)

    if en_letra:
        print("El número", numero, "es:", en_letra)


if __name__ == "__main__":
    main()
