#!/usr/bin/env python3
"""
Programa que convierte de números a letras
"""


def ingresa_numero():
    """Función que devuelve un número en formato str"""

    numero = input("Ingresa un número entero:")

    return numero


def main():
    """
    Función principal
    """
    numero = ingresa_numero()

    if numero:
        print("ok")


if __name__ == "__main__":
    main()
