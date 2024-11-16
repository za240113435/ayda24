def numero_a_texto(n):
    # Definir las listas de palabras para unidades, decenas, centenas, etc.
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    
    if n == 0:
        return "cero"
    
    if n == 1000000:
        return "un millón"
    
    texto = ""
    
    # Miles
    if n >= 1000:
        miles = n // 1000
        n = n % 1000
        if miles > 1:
            texto += numero_a_texto(miles) + " mil "
        else:
            texto += "mil "
    
    # Centenas
    if n >= 100:
        centena = n // 100
        n = n % 100
        if centena == 1 and n == 0:
            texto += "cien"
        else:
            texto += centenas[centena] + " "
    
    # Decenas
    if n >= 20:
        decena = n // 10
        n = n % 10
        texto += decenas[decena] + " "
    
    # Unidades (para números entre 1 y 19)
    if n > 0:
        texto += unidades[n]
    
    # Limpiar los espacios innecesarios
    return texto.strip()

# Solicitar el número al usuario
numero = int(input("Introduce un número entre 0 y 1,000,000: "))
if 0 <= numero <= 1000000:
    print(f"El número {numero} en texto es: {numero_a_texto(numero)}")
else:
    print("El número está fuera del rango permitido.")
