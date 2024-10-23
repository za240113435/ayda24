# Función para convertir números a texto
# Se introduce el numero que se va a convertir a texto
def numero_a_texto(num):
#     Esta se utiliza en dado caso de que el numero sea negativo para
#  para agregar el menos al inicio del resultado 
    if num < 0:
        return "menos " + numero_a_texto(-num)
#    Se define una lista de unidades, decenas y numeros especiales 
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
#  Números menores a 10 donde se devuelve el
#  valor de la lista de unidades 
    if num < 10:
        return unidades[num]
#     Números entre 10 y 19 que son los especiales
    elif 10 <= num < 20:
        return especiales[num - 10]
#     Números entre el 20 y 99
    elif 20 <= num < 100:
#         Decenas 
        d = num // 10
#         Unudades 
        u = num % 10
        return decenas[d] + ('' if u == 0 else ' y ' + unidades[u])
#    Números de 100 a 999
    elif 100 <= num < 1000:
#       Centenas  
        c = num // 100
#         Decenas  y unidades 
        d = num % 100
        return unidades[c] + 'cientos' + ('' if d == 0 else ' ' + numero_a_texto(d))
#     Números entre 1,000 y 999,999
    elif 1000 <= num < 1_000_000:
#         La letra m representa los miles 
        m = num // 1000
        return numero_a_texto(m) + ' mil' + ('' if num % 1000 == 0 else ' ' + numero_a_texto(num % 1000))
#   Números entre 1,000,000 y 999,999,999  
    elif 1_000_000 <= num < 1_000_000_000:
#         En este caso la letra m es para millones
        m = num // 1_000_000
        return numero_a_texto(m) + ' millones' + ('' if num % 1_000_000 == 0 else ' ' + numero_a_texto(num % 1_000_000))
#    Números entre 1,000,000,000 y 999,999,999,999 
    elif 1_000_000_000 <= num < 1_000_000_000_000:
#         En este caso los números son en miles de millones
        b = num // 1_000_000_000
        return numero_a_texto(b) + ' mil millones' + ('' if num % 1_000_000_000 == 0 else ' ' + numero_a_texto(num % 1_000_000_000))
#  Números entre 1,000,000,000,000 y 999,999,999,999,999  
    elif 1_000_000_000_000 <= num < 1_000_000_000_000_000:
#        En este caso son los billones 
        billon = num // 1_000_000_000_000
        return numero_a_texto(billon) + ' billones' + ('' if num % 1_000_000_000_000 == 0 else ' ' + numero_a_texto(num % 1_000_000_000_000))
    
    return str(num)  # Para números mayores a billones

# Solicitar un número al usuario
numero = int(input("Introduce un número (hasta billones): "))

# Convertir el número a texto
texto = numero_a_texto(numero)

# Mostrar el resultado
print(f"El número {numero} en letras es: {texto}")
