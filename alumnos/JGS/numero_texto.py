#!/usr/bin/env python3

def numero_a_palabras(n): # AGREGAMOS LOS NOMBRES DE CADA NUMERO EN TEXTO 
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"] 
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def convertir_decenas(n): # CONVIERTE LOS NUMEROS DEL 0 AL 99
        if n < 10:
            return unidades[n]
        elif n < 20:
            return especiales[n - 10]
        else:
            if n % 10 == 0: # DIVIDE ENTRE 1O Y NO HAY RESIDUO
                return decenas[n // 10] # DIVIDE EL NUMERO ENTRE 10
            else:
                return decenas[n // 10] + " y " + unidades[n % 10] # DIVIDE ENTRE DIEZ PARA SACAR LAS DECENAS Y EL RESIDUO LO ETIQUETA CON UNIDADES
            
    def convertir_centenas(n): # CONVIERTE LOS NUMEROS DEL 100 AL 999
        if n == 100:
            return "cien"
        else:
            return centenas[n // 100] + " " + convertir_decenas(n % 100)    # DIVIDE ENTRE CIEN PARA SACAR LAS CENTENAS Y EL RESIDUO LO MANDA A LA FUNCIÓN convertir_decenas
                                                                            # EL MISMO MODO DE HACER LAS OPERACIONES SE REPITE COMPARA, DIVIDE, ETIQUETA Y EL RESIDUO LO MANDA A LA SIGUIENTE MAS PEQUEÑA
    def convertir_miles(n): # CONVIERTE LOS NUMEROS DEL 1000 AL 999,999
        if n < 1000:
            return convertir_centenas(n)
        else:
            miles = n // 1000
            resto = n % 1000
            if miles == 1:
                return "mil " + convertir_centenas(resto)
            else:
                return convertir_centenas(miles) + " mil " + convertir_centenas(resto)

    def convertir_millones(n): # CONVIERTE LOS NUMEROS DEL 1,000,000 AL 999,999,999
        if n < 1000000:
            return convertir_miles(n)
        else:
            millones = n // 1000000
            resto = n % 1000000
            if millones == 1:
                return "un millón " + convertir_miles(resto)
            else:
                return convertir_miles(millones) + " millones " + convertir_miles(resto)

    def convertir_miles_millones(n): # CONVIERTE LOS NUMEROS DEL 1,000,000,000 AL 999,999,999,999
        if n < 1000000000:
            return convertir_millones(n)
        else:
            miles_millones = n // 1000000000
            resto = n % 1000000000
            if miles_millones == 1:
                return "mil millones " + convertir_millones(resto)
            else:
                return convertir_millones(miles_millones) + " mil " + convertir_millones(resto)
    
    def convertir_billones(n): # CONVIERTE LOS NUMEROS HASTA BILLONES
        if n < 1000000000000:
            return convertir_miles_millones(n)
        else:
            billones = n // 1000000000000
            resto = n % 1000000000000
            if billones == 1:
                return "un billón " + convertir_miles_millones(resto)
            else:
                return convertir_miles(billones) + " billones " + convertir_miles_millones(resto)
    
    return convertir_billones(n).strip()

# Solicitar el número al usuario
while True:
    try:
        numero = int(input("Introduce un número: "))
        if numero < 0:
            print("Por favor, introduce un número positivo.")
        else:
            print(numero_a_palabras(numero))
            break  # Salir del bucle si se ingresa un número válido
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número válido.")