# AUTOR: ALEJANDRO ANTONIO AMAVIZCA LOPEZ.
# CONVERSOR DE NÚMEROS DE DECIMAL A LETRA
# HASTA UN TRILLÓN
# DISEÑO Y ANÁLISIS DE ALGORITMOS





numeros = {0:"cero",1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",
           10:"diez",11:"once",12:"doce",13:"trece",14:"catorce",15:"quince",16:"dieciseis",17:"diecisiete",
           18:"dieciocho",19:"diecinueve",20:"veinte",21:"veintiuno",22:"veintidos",23:"veintitres",24:"veiticuatro",
           25:"veinticinto",26:"veintiseis",27:"veintisiete",28:"veintiocho",29:"veintinueve"}

decenas = {10:"diez",20:"veinte",30:"treinta",40:"cuarenta",50:"cincuenta",
           60:"sesenta",70:"setenta",80:"ochenta",90:"noventa"}

centenas = {100: 'cien',200: 'doscientos',300: 'trescientos',400: 'cuatrocientos',
            500: 'quinientos',600: 'seiscientos',700: 'setecientos',800: 'ochocientos',900: 'novecientos'
            }


def conversor(num):
        num = int(num)
        if num < 29:GG
            return numeros[num]
        if num < 100:
            return decenas[int(num/10)*10]+ " y " + conversor(num%10) if num%10 !=0 else decenas[int(num/10)*10]
        if num ==100:
            return centenas[num]
        if num < 200:
            return "ciento " + conversor(num%100)
        if num < 1000:
            return centenas[int(num/100)*100] +" "+ conversor(num%100) if num%100 != 0 else centenas[int(num/100)*100]
        if num == 1000:
            return "mil"
        if num < 1000000:
            return conversor(int(num/1000)) + " mil "+conversor(num%1000) if num%1000 != 0 else conversor(int(num/1000)) + " mil"
        if num == 1000000:
            return "un millón"
        if num < 1000000000000:
            mills = " millon " if int(num/1000000) == 1 else " millones "
            return conversor(int(num/1000000)) + mills+", " + conversor(num%1000000) if num%1000000 != 0 else conversor(int(num/1000000)) + mills
        if num == 1000000000000:
            return "un billón"
        if num < 1000000000000000000:
            billones = int(num/1000000000000)
            bills = " billón " if billones == 1 else " billones "
            return conversor(billones) + bills + ", " + conversor(num%1000000000000) if num%1000000000000 != 0 else conversor(billones) + bills
        if num == 1000000000000000000:
            return "1 trillón"
        else:
            return "ES MÁS DE UN TRILLÓN !!! PAPITO, NO PUEDO CONVERTIR MÁS DE UN TRILLÓN, A POCO TIENES TANTO VARO?"
        

while True:
    try:
        num = input("Número entero en decimal: ")
        print(conversor(num))
    except ValueError:
        print("Sólo números, mi buen, intenta de nuevo...")