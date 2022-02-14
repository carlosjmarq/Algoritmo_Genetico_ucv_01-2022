import numpy as np
from decimal import Decimal, ROUND_UP

def solicitud_parametros():
	"""Solicitud de parametros de inicio"""
	# Funcion a usar
	while True:
		try:
			funcion = str(input('Cual función desea optimizar? (1)F1 o (2)F2?\n')).strip().upper()	
			if funcion not in {'1','2'}:
				print('La respuesta debe ser 1 o 2')
				continue
			break
		except:
			print('Debe insertar un string válido')
			continue
	# Máximo o minimo
	while True:	
		try:
			max_min = str(input(f'Desea (1)maximizar o (2)minimizar la función F{funcion}'))
			if max_min not in {'1','2'}:
				print('La respuesta debe ser 1 o 2')
				continue
			break
		except:
			print('Debe insertar un string válido')
			continue
	# Variables
	nombre_variable = ('x','y','z')
	variables = []
	for i in range(int(funcion)+1):
		while True:
			try:
				limite_inferior = float(input('Inserte el limite inferior de {}:  '.format(nombre_variable[i]))) 
				break				
			except:
				print('El límite inferior debe ser un número de punto flotante.')
				continue
		while True:
			try:
				limite_superior = float(input('Inserte el limite superior de {}:  '.format(nombre_variable[i]))) 
				break				
			except:
				print('El límite superior debe ser un número de punto flotante.')
				continue
		# Bits
		while True:
			try:
				num_bits = int(input('Inserte el número de bits para {}:  '.format(nombre_variable[i])))
				break
			except:
				print('El número de bits debe ser un número entero')
				continue
		variables.append({
			'nombre': nombre_variable[i],
			'limites': [limite_inferior,limite_superior],
			'bits': num_bits,
			'precision': None
		})
	# Calculo de precision
	for var in variables:
		var.update({
			'precision': int(Decimal(np.log((2**var['bits']-1)/(max(var['limites'])-min(var['limites'])))/np.log(10)).quantize(Decimal('0.'), rounding=ROUND_UP))
		})
	# Continuar con parámetros standar
	while True:	
		try:
			respuesta = input('Desea modificar los parámetros estandar del algoritmo genético? (Y) o (N)').strip().upper()
			if respuesta not in ('Y','N'):
				print('La respuesta debe ser Y o N')
				continue
			continuar = True if respuesta == 'Y' else False
			break
		except:
			print('Debe insertar un string válido')
			continue
	if not continuar:
		return {
			'variables': variables,
			'funcion': funcion,
			'max': True if max_min == 1 else False,
			'n_pob': None,
			'n_gen': None,
			'p_cruce': None,
			'p_muta': None
		}
	#Tamaño de Poblacion
	while True:	
		try:
			n_pob = int(input('Insete el tamaño de poblacion'))
			if n_pob%2 == 1:
				print('Por facilidada de cálculo debe insertar un mútiplo de 2')
				continue
			break
		except:
			print('Debe insertar un número entero')
			continue
	#Cantidad de generaciones
	while True:	
		try:
			n_gen = int(input('Inserte la cantidad de generaciones'))
			break
		except:
			print('Debe insertar un número entero')
			continue
	#Probabilidad de Cruce
	while True:
		try:
			p_cruce = float(input('Inserte la Probabilidad de Cruce'))
			if p_cruce > 1.0 or p_cruce < 0.0:
				print('la probabilidad debe ser un número entre 1 y 0')
				continue
			break
		except:
			print('Debe insertar un número de punto flotante')
			continue
	#Probabilidade de mutacion
	while True:
		try:
			p_muta = float(input('Inserte la Probabilidad de Mutacion'))
			if p_muta > 1.0 or p_muta < 0.0:
				print('la probabilidad debe ser un número entre 1 y 0')
				continue
			break
		except:
			print('Debe insertar un número de punto flotante')
			continue
	return {
			'variables': variables,
			'funcion': funcion,
			'max': True if max_min == 1 else False,
			'n_pob': n_pob,
			'n_gen': n_gen,
			'p_cruce': p_cruce,
			'p_muta': p_muta
		}

