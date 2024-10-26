#se declaran los valores posibles, de numeros a texto
def number_to_words(n):
    #Se declaran las unidades
    unidades = ["", 
                "uno", 
                "dos", 
                "tres", 
                "cuatro", 
                "cinco", 
                "seis", 
                "siete", 
                "ocho", 
                "nueve"]
    #Se declaran las decenas
    decenas = ["", 
               "diez", 
               "veinte", 
               "treinta", 
               "cuarenta", 
               "cincuenta", 
               "sesenta", 
               "setenta", 
               "ochenta", 
               "noventa"]
    #Se declaran los numeros que son casos especiales
    especiales = ["once", 
                  "doce", 
                  "trece", 
                  "catorce", 
                  "quince", 
                  "dieciséis", 
                  "diecisiete", 
                  "dieciocho", 
                  "diecinueve"]
    #Se declaran las cemtemas
    centenas = ["", 
                "cien", 
                "doscientos", 
                "trescientos", 
                "cuatrocientos", 
                "quinientos", 
                "seiscientos", 
                "setecientos", 
                "ochocientos", 
                "novecientos"]
    #Definición de prefijos, respecto al numero superior a mil
    grandes_numeros = [
        (10**18, "trillones"),
        (10**15, "mil billones"),
        (10**12, "billones"),
        (10**9, "mil millones"),
        (10**6, "millones"),
        (10**3, "mil"),
        (1, "")
    ]
    # Corrección de error con cero
    if n == 0:
        return "cero"
    # Se tiene que colocar esta validación dado que cien es un numero unico
    if n == 100:
        return "cien"
    # Declaración de arreglo palabra
    palabras = []
    
    #definimos las Casos conjuntivos
    def menos_de_mil(n):
        if n < 10: # Se validan las unidades
            return unidades[n]
        elif 10 < n < 20: #se validan los casos especiales que son menores a 20 y mayores a 10
            return especiales[n - 11]
        elif n < 100:
            if n % 10 == 0:
        #validamos si dentro de este caso tiene que tener una
                return decenas[n // 10]
            return decenas[n // 10] + " y " + unidades[n % 10]
        else:
            if n % 100 == 0:
                return centenas[n // 100]
            return centenas[n // 100] + " " + menos_de_mil(n % 100)

    
    #Siclo para validar de numeros mayores a menores
    for valor, nombre in grandes_numeros:
        if n >= valor:
            # Se utiliza // para redondear el resultado
            cantidad = n // valor
            if cantidad == 1 and nombre == "mil":
                palabras.append("mil")
            else:
                palabras.append(menos_de_mil(cantidad) + (" " + nombre if nombre else ""))
            n %= valor
    
    return " ".join(palabras)

# Ejemplo de uso
numero = int(input("Introduce un número: "))
print(number_to_words(numero))
 #git set-url "direccion a la cual voy a subir mi trabajo"