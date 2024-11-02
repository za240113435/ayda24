def numero_a_letras(num):
    if num < 0 or num > 1000000:
        return "Número fuera de rango"

    unidades = ("", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve")
        
    decenas = ("", "diez", "veinte", "treinta", "cuarenta", "cincuenta","sesenta", "setenta", "ochenta", "noventa")
    
    especiales = (
        "cero", "uno", "dos", "tres", "cuatro", "cinco","seis", "siete", "ocho", "nueve", "diez","once", "doce", "trece", "catorce", "quince")
    
    cientos = ("", "cien", "doscientos", "trescientos", "cuatrocientos","quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos")
    
    if num == 1000000:
        return "un millón"

    resultado = ""
    
    if num >= 1000:
        miles = num // 1000
        resultado += numero_a_letras(miles) + " mil"
        num %= 1000
        if num > 0:
            resultado += " "

    if num >= 100:
        centena = num // 100
        resultado += cientos[centena]
        num %= 100
        if num > 0:
            resultado += " "

    if num >= 20:
        decena = num // 10
        resultado += decenas[decena]
        num %= 10
        if num > 0:
            resultado += " "

    if num > 0:
        if resultado:
            resultado += "y "
        resultado += unidades[num]

    return resultado.strip()

# Ejemplo de uso
numero = int(input("Introduce un número: "))
print(numero_a_letras(numero))
