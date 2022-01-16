from functions.solicitud_variables import solicitud_variables
from functions.calculo_parametros import calcular_parametros
from functions.format_params import print_params
from functions.bits_to_real import bits2float
from functions.real_to_bits import float2bits

if __name__ == '__main__':
	"""Solicitud de variables"""
	parametros = solicitud_variables()
	parametros = calcular_parametros(parametros)
	"""Inicio de la lógica"""
	while True:
		respuesta = int(input("""Que desea hacer?:\n(1)Convertir un número real del dominio en bits\n(2)Convertir un conjunto de bits en un número real del dominio\n(3)Mostrar Variables\n(4)Reprogramar variables\n(5)Salir\n"""))
		if respuesta not in range(1,6):
			print('debe seleccionar una opción válida.')
			continue
		if respuesta == 5:
			break
		if respuesta == 4:
			parametros = solicitud_variables()
			parametros = calcular_parametros(parametros)
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
					continue
				break
			bits2float(bits,parametros)
		if respuesta == 1:
			reales = []
			for var in parametros['variables']:
				while True:
					try:
						real = float(input('Inserte un valor real para {} entre {}:  '.format(var['nombre'],str(var['limites']))).strip())
						if real < min(var['limites']) or real > max(var['limites']):
							print('El valor debe formar parte del dominio descrito')
							continue
						reales.append(real)
						break
					except:
						print('Debe ingresar un número real.')
			float2bits(reales,parametros)
