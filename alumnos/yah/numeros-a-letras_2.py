#!/usr/bin/env python3


def numero_a_letras(numero):
    """Convierte un número a su representación en letras en español.

    Args:
        numero: El número a convertir.

    Returns:
        Una cadena con el número en letras.
    """

    unidades = [
        "",
        "un",
        "dos",
        "tres",
        "cuatro",
        "cinco",
        "seis",
        "siete",
        "ocho",
        "nueve",
    ]
    decenas = [
        "",
        "diez",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    ]
    centenas = [
        "",
        "ciento",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    ]
    unidades_miles = [
        "",
        "mil",
        "dos mil",
        "tres mil",
        "cuatro mil",
        "cinco mil",
        "seis mil",
        "siete mil",
        "ocho mil",
        "nueve mil",
    ]
    decenas_miles = [
        "",
        "diez mil",
        "veinte mil",
        "treinta mil",
        "cuarenta mil",
        "cincuenta mil",
        "sesenta mil",
        "setenta mil",
        "ochenta mil",
        "noventa mil",
    ]
    centenas_miles = [
        "",
        "cien mil",
        "doscientos mil",
        "trescientos mil",
        "cuatrocientos mil",
        "quinientos mil",
        "seiscientos mil",
        "setecientos mil",
        "ochocientos mil",
        "novecientos mil",
    ]
    millones = [
        "",
        "un millón",
        "dos millones",
        "tres millones",
        "cuatro millones",
        "cinco millones",
        "seis millones",
        "siete millones",
        "ocho millones",
        "nueve millones",
    ]

    # Manejar números negativos
    if numero < 0:
        return "menos " + numero_a_letras(-numero)

    # Convertir a cadena y separar en grupos de tres dígitos
    numero_str = str(numero)
    grupos = []
    while numero_str:
        grupos.insert(0, numero_str[-3:])
        numero_str = numero_str[:-3]

    # Convertir cada grupo de tres dígitos a letras
    resultado = ""
    for i, grupo in enumerate(grupos):
        c, d, u = int(grupo[0]), int(grupo[1]), int(grupo[2])
        if i == 0:
            if c == 1 and d == 0 and u == 0:
                resultado += "cien"
            else:
                resultado += centenas[c] + " "
                resultado += decenas[d]
                if d == 1:
                    resultado += " y " + unidades[u]
                else:
                    resultado += " " + unidades[u]
        elif i == 1:
            resultado += (
                " "
                + unidades_miles[u]
                + " "
                + decenas_miles[d]
                + " "
                + centenas_miles[c]
                + " "
            )
        elif i == 2:
            resultado += " " + millones[c] + " "

    return resultado.strip()


def ingresa_numero():
    """Función que devuelve un número en formato str"""

    numero = input("Ingresa un número entero positivo: ")

    while not numero.isdecimal():
        print("No es un número entero, por favor ", end="")
        numero = input("ingresa un número entero positivo: ")

    return int(numero)


def main():
    """
    Función principal
    """
    numero = ingresa_numero()

    en_letra = numero_a_letras(numero)

    if en_letra:
        print("El número", numero, "es:", en_letra)


if __name__ == "__main__":
    main()
