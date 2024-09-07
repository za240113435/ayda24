Algoritmo operaciones
	Escribir "     Menu"
	Escribir "1. Suma"
	Escribir "2. Resta"
	Escribir "3. Multiplicacion"
	Escribir "4. Division"
	Escribir "Opción:"
	Leer la_opcion
	
	Escribir "Ingresa el primer número: "
	Leer num1
	Escribir "Ingresa el segundo número: "
	Leer num2
	
	Si la_opcion = 1 Entonces
		Escribir "La suma es", num1 + num2
	FinSi
	
	Si la_opcion = 2 Entonces
		Escribir "La resta es", num1 - num2
	SiNo
		Si la_opcion = 3 Entonces
			Escribir "La multiplicación es", num1 * num2
		SiNo
			Si la_opcion = 4 Entonces
				Escribir "La división es", num1 / num2
			FinSi
		FinSi
	FinSi
FinAlgoritmo
