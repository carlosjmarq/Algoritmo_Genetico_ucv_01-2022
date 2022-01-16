def solicitud_variables():
	"""Solicitud de variables de inicio"""
	# Precisión o número de bits???
	while True:
		try:
			respuesta = str(input('Desea usar (P)recisión o número de (B)its para realizar los calculos?\n')).strip().upper()	
			if respuesta not in ['P','B']:
				print('La respuesta debe ser "P" o "B"')
				continue
			usar_precision = respuesta == 'P'
			break
		except:
			print('Debe insertar un string válido')
			continue
	# Número de variables
	while True:	
		try:
			len_variables = int(input('Inserte el número de variables del sistema:  '))
			break
		except:
			print('el numero de variables debe ser un número entero.')
			continue
	# Nombre y Dominio de las Variables
	variables = []
	for i in range(len_variables):
		while True:
			try:
				nombre_variable = str(input('Inserte el nombre de la variable {}:  '.format(i+1))).strip() 
				break				
			except:
				print('El nombre debe ser un string válido.')
				continue
		while True:
			try:
				limite_inferior = float(input('Inserte el limite inferior de {}:  '.format(nombre_variable))) 
				break				
			except:
				print('El límite inferior debe ser un número de punto flotante.')
				continue
		while True:
			try:
				limite_superior = float(input('Inserte el limite superior de {}:  '.format(nombre_variable))) 
				break				
			except:
				print('El límite superior debe ser un número de punto flotante.')
				continue
		if not(usar_precision):
			# Bits
			while True:
				try:
					num_bits = int(input('Inserte el número de bits para {}:  '.format(nombre_variable)))
					break
				except:
					print('El número de bits debe ser un número entero')
					continue
		else:
			# Precisión
			while True:
				try:
					precision = int(input('Inserte la presición de la variable (cantidad de digitos despues del punto):  '))
					break
				except:
					print('la precision debe ser un numero de punto flotante. Ej: 0.00001')
					continue

		variables.append({
			'nombre': nombre_variable,
			'limites': [limite_inferior,limite_superior],
			'num_bits': num_bits if not(usar_precision) else None,
			'precision': precision if usar_precision else None
		})
	return {
		'variables': variables,
		'usar_precision': usar_precision,
	}
