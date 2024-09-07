Algoritmo mayor_a_3_numeros
	Escribir "Escribe el primer número"
	Leer num1
	Escribir "Escribe el segundo número"
	Leer num2
	Escribir "Escribe el tercer número"
	Leer num3
	
	Si num1 > num2 Entonces
		Si num1 > num3 Entonces
			Escribir "El primer número es mayor"
		SiNo
			Escribir "El tercer número es mayor"
		FinSi
	SiNo
		Si num2 > num3 Entonces
			Escribir "El segundo número es mayor"
		SiNo
			Escribir "El tercer número es mayor"
		FinSi
	FinSi
	
	
FinAlgoritmo
