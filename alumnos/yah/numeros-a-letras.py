#!/usr/bin/env python3
"""
Programa que convierte de números a letras
"""


def numero_a_letra(numero):
    pass


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
