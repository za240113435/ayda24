#!/usr/bin/env python3

def convertir_a_letras(n):
    # Listas de palabras para la conversión
    UNIDADES = (
        "",
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
        "dieciséis",
        "diecisiete",
        "dieciocho",
        "diecinueve",
    )
    DECENAS = (
        "",
        "",
        "veinte",
        "treinta",
        "cuarenta",
        "cincuenta",
        "sesenta",
        "setenta",
        "ochenta",
        "noventa",
    )
    CENTENAS = (
        "",
        "cien",
        "doscientos",
        "trescientos",
        "cuatrocientos",
        "quinientos",
        "seiscientos",
        "setecientos",
        "ochocientos",
        "novecientos",
    )
    GRANDES = ["", "mil", "millón", "mil millones", "billón"]

    def convertir_menor_1000(num):
        if num == 0:
            return ""
        elif num < 20:
            return UNIDADES[num]
        elif num < 100:
            return DECENAS[num // 10] + ("" if num % 10 == 0 else " y " + UNIDADES[num % 10])
        else:
            return CENTENAS[num // 100] + (" " + convertir_menor_1000(num % 100) if num % 100 != 0 else "")

    def convertir_grande(num):
        if num == 0:
            return "cero"
        if num == 1_000_000_000:
            return "un billón"

        partes = []
        i = 0

        while num > 0:
            parte = num % 1000
            if parte > 0:
                prefijo = convertir_menor_1000(parte)
                sufijo = GRANDES[i]
                if i == 1 and parte == 1:
                    partes.append(sufijo)  # "mil"
                elif i > 1 and parte == 1:
                    partes.append("un " + sufijo)  # "un millón", "un billón"
                else:
                    partes.append(prefijo + (" " + sufijo if sufijo else ""))
            num //= 1000
            i += 1

        return " ".join(reversed(partes)).strip()

    return convertir_grande(n)


# Ejemplo de uso
if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    print(convertir_a_letras(numero))
