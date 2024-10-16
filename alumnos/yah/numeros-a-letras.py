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

TERCEROS = (
    "",
    "ciento",
    "quinientos",
    "setecientos",
    "novecientos",
)

CUARTOS = (
    "mil",
    "millón",
)


def numero_a_letra(numero):
    """Función que convierte el número a letras"""

    en_letra = ""
    tamanio = len(numero)

    if tamanio == 1:
        en_letra = PRIMEROS[int(numero)]
    elif tamanio == 2:
        if numero[0] in ("0", "1") and numero[1] < "6":
            en_letra = PRIMEROS[int(numero)]
        elif numero == "20":
            en_letra = SEGUNDOS[int(numero[0])][:-1] + "e"
        elif numero[1] == "0":
            en_letra = SEGUNDOS[int(numero[0])]
        elif numero < "31":
            en_letra = SEGUNDOS[int(numero[0])] + PRIMEROS[int(numero[1])]
        else:
            en_letra = SEGUNDOS[int(numero[0])] + " y " + PRIMEROS[int(numero[1])]
    elif tamanio == 3:
        if numero == "100":
            en_letra = TERCEROS[int(numero[0])][:-2]
        elif numero[0] == "0":
            en_letra = numero_a_letra(numero[1:])
        elif numero[0] == "1":
            en_letra = TERCEROS[int(numero[0])] + " " + numero_a_letra(numero[1:])
        elif numero[0] == "5":
            en_letra = TERCEROS[2] + " " + numero_a_letra(numero[1:])
        elif numero[0] == "7":
            en_letra = TERCEROS[3] + " " + numero_a_letra(numero[1:])
        elif numero[0] == "9":
            en_letra = TERCEROS[4] + " " + numero_a_letra(numero[1:])
        else:
            en_letra = (
                PRIMEROS[int(numero[0])]
                + TERCEROS[1]
                + "s "
                + numero_a_letra(numero[1:])
            )
    elif tamanio < 7:
        primeros = numero[-3:]
        segundos = numero[:-3]

        if len(segundos) == 1 and segundos[0] == "1":
            en_letra = CUARTOS[0]
        else:
            en_letra = numero_a_letra(segundos) + " " + CUARTOS[0]

        # verificamos que no sean puros ceros
        if int(primeros):
            en_letra += " " + numero_a_letra(primeros)
    elif tamanio < 10:
        primeros = numero[-6:]
        segundos = numero[:-6]

        if len(segundos) == 1 and segundos[0] == "1":
            en_letra = "un " + CUARTOS[1]
        else:
            en_letra = numero_a_letra(segundos) + " " + CUARTOS[1][:-2] + "ones"

        # verificamos que no sean puros ceros
        if int(primeros):
            en_letra += " " + numero_a_letra(primeros)

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
