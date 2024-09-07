Algoritmo calcular_formula_general
	// Pedimos los números al usuario
	Escribir "Escribe el número a: "
	Leer a
	
	Escribir "Escribe el número b: "
	Leer b
	
	Escribir "Escribe el número c: "
	Leer c
	
	// Calculamos la formula
	discriminante <- b^2 - 4*a*c
	
	Si discriminante < 0 Entonces
		Escribir "La solución tiene raices imaginarias"
	SiNo
		Si discriminante = 0 Entonces
			Escribir "La solución tiene una sola raiz"
		SiNo
			x1 <- (-b + rc(discriminante)) / (2*a)
			x2 <- (-b - rc(discriminante)) / (2*a)
			
			// Imprimo resultado
			Escribir "La solución tiene dos raices"
			Escribir "X1 es: ", x1
			Escribir "X2 es: ", x2
		Fin Si
	Fin Si
FinAlgoritmo
