def unidades(n):
    if n == 1:
        return "uno"
    elif n == 2:
        return "dos"
    elif n == 3:
        return "tres"
    elif n == 4:
        return "cuatro"
    elif n == 5:
        return "cinco"
    elif n == 6:
        return "seis"
    elif n == 7:
        return "siete"
    elif n == 8:
        return "ocho"
    elif n == 9:
        return "nueve"
    return ""

def decenas(n):
    if n == 10:
        return "diez"
    elif n == 11:
        return "once"
    elif n == 12:
        return "doce"
    elif n == 13:
        return "trece"
    elif n == 14:
        return "catorce"
    elif n == 15:
        return "quince"
    elif n < 20:
        return "dieci" + unidades(n % 10)
    elif n == 20:
        return "veinte"
    elif 21 <= n <= 29:
        return "veinti" + unidades(n % 10)
    elif n == 30:
        return "treinta"
    elif n < 40:
        return "treinta y " + unidades(n % 10)
    elif n == 40:
        return "cuarenta"
    elif n < 50:
        return "cuarenta y " + unidades(n % 10)
    elif n == 50:
        return "cincuenta"
    elif n < 60:
        return "cincuenta y " + unidades(n % 10)
    elif n == 60:
        return "sesenta"
    elif n < 70:
        return "sesenta y " + unidades(n % 10)
    elif n == 70:
        return "setenta"
    elif n < 80:
        return "setenta y " + unidades(n % 10)
    elif n == 80:
        return "ochenta"
    elif n < 90:
        return "ochenta y " + unidades(n % 10)
    elif n == 90:
        return "noventa"
    else:
        return "noventa y " + unidades(n % 10)

def centenas(n):
    if n == 100:
        return "cien"
    elif n < 200:
        return "cien " + unidades(n % 100)
    elif n < 300:
        return "doscientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 400:
        return "trescientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 500:
        return "cuatrocientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 600:
        return "quinientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 700:
        return "seiscientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 800:
        return "setecientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 900:
        return "ochocientos " + (decenas(n % 100) if n % 100 != 0 else "")
    elif n < 1000:
        return "novecientos " + (decenas(n % 100) if n % 100 != 0 else "")
    return ""

def miles(n):
    if n < 1000:
        return centenas(n)
    elif n == 1000:
        return "mil"
    elif n < 2000:
        return "mil " + centenas(n % 1000)
    else:
        return unidades(n // 1000) + " mil " + centenas(n % 1000)

def millones(n):
    if n < 1000000:
        return miles(n)
    elif n == 1000000:
        return "un millón"
    elif n < 2000000:
        return "un millón " + miles(n % 1000000)
    else:
        return millones(n // 1000000) + " millones " + miles(n % 1000000)

def miles_de_millones(n):
    if n < 1000000000:
        return millones(n)
    elif n == 1000000000:
        return "mil millones"
    elif n < 2000000000:
        return "mil millones " + millones(n % 1000000000)
    else:
        return millones(n // 1000000) + " millones " + miles(n % 1000000000)

def billones(n):
    if n < 100000000000:
        return miles_de_millones(n)
    elif n == 100000000000:
        return "cien billones"
    elif n < 200000000000:
        return "cien billones " + miles_de_millones(n % 100000000000)
    else:
        return billones(n // 100000000000) + " billones " + miles_de_millones(n % 100000000000)

def numero_a_letra(n):
    if n == 0:
        return "cero"
    if n < 0:
        return "menos " + numero_a_letra(-n)
    return billones(n)

# Ejemplo de uso
numero = 123456789
print(numero_a_letra(numero))
