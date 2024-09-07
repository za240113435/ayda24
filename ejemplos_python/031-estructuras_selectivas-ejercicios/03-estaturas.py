estatura = eval(input("Escribe tu estatura en metros: "))

if estatura < 1.5:
    print("Eres de estatura baja")
else:
    if estatura > 1.7:
        print("Eres de estatura alta")
    else:
        print("Eres de estatura media")
