def number_to_words(num):
    if num < 0 or num > 1000000:
        return "Número fuera de rango. Debe estar entre 0 y 1,000,000."

    unidades = [
        "", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
        "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
        "dieciocho", "diecinueve"
    ]
    
    decenas = [
        "", "", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro",
        "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"
    ]
    
    decenas_multiples = [
        "", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta",
        "setenta", "ochenta", "noventa"
    ]

    centenas = [
        "", "cien", "doscientos", "trescientos", "cuatrocientos",
        "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"
    ]
    
    if num == 1000000:
        return "un millón"
    
    palabras = ""
    
    if num >= 1000:
        miles = num // 1000
        palabras += number_to_words(miles) + " mil"
        num %= 1000
    
    if num >= 100:
        centenas_num = num // 100
        palabras += " " + centenas[centenas_num] if palabras else centenas[centenas_num]
        num %= 100
    
    if num >= 20:
        decenas_num = num // 10
        palabras += " " + decenas_multiples[decenas_num] if palabras else decenas_multiples[decenas_num]
        num %= 10
    
    if num >= 10:
        palabras += " " + unidades[num] if palabras else unidades[num]
        return palabras.strip()
    
    if num > 0:
        palabras += " " + unidades[num] if palabras else unidades[num]
    
    return palabras.strip()

# Ejemplo de uso
numero = int(input("Ingresa un número entre 0 y 1,000,000: "))
resultado = number_to_words(numero)
print(f"El número {numero} en palabras es: {resultado}")