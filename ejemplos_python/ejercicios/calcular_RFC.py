nombre = input("Escribe tu nombre: ")
ape_pa = input("Escribe tu apellido paterno: ")
ape_ma = input("Escribe tu apellido materno: ")
dia = input("Escribe tu día de nacimento: ")
mes = input("Escribe tu mes de nacimento con número: ")
anio = input("Escribe tu año de nacimento: ")

RFC = ape_pa[:2].upper() + ape_ma[0].upper() + nombre[0].upper() + anio[2:]

if len(mes) == 1:
    RFC += "0" + mes
else:
    RFC += mes

if len(dia) == 1:
    RFC += "0" + dia
else:
    RFC += dia


print("Tu RFC es: ", RFC)
