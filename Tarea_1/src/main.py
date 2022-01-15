import numpy as np
from decimal import Decimal, ROUND_UP
from solicitud_variables import solicitud_variables
from calculo_parametros import calcular_parametros
from format_params import print_params
from bits_to_real import bits2float

if __name__ == '__main__':
	"""Solicitud de variables"""
	parametros = solicitud_variables()
	parametros = calcular_parametros(parametros)
	"""Inicio de la lógica"""
	while True:
		# try:
			respuesta = int(input("""Que desea hacer?:\n(1) Convertir un número real del dominio en bits\n(2)Convertir un conjunto de bits en un número real del dominio\n(3)Mostrar Variables\n(4)Salir\n"""))
			if respuesta not in range(1,5):
				print('debe seleccionar una opción válida.')
				continue
			if respuesta == 4:
				break
			if respuesta == 3:
				print_params(parametros)
				continue
			if respuesta == 2:
				while True:
					bits = list(input('Inserte un string de bits de longitud {}:  '.format(parametros['bits_totales'])).strip())
					if set(bits) != set(('1','0')):
						print('Debe insertar un conjunto de bits válido')
						continue
					if len(bits) != parametros['bits_totales']:
						print('La longitud de la frase debe se de {}'.format(parametros['bits_totales']))
					break
				bits2float(bits,parametros)
		# except:
		# 	print('Debe insertar un número entero')
		# 	continue
