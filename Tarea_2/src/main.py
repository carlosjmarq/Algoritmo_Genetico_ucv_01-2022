from printers import *
from selection_methods import *

def preparar_data(n: int):
	pob = poblacion_constructor(n)
	return {
		'poblacion': pob,
		'copias_esp': valores_esperados(pob),
		'rul': ruleta(pob),
		'sobra': sobrante_estocastico(pob),
		'univ': universal_estocastica(pob),
		'mues': muestreo_deterministico(pob),
		'tor_det': torneo_deterministico(pob),
		'tor_proba': torneo_probabilistico(pob),
	}

if __name__ == '__main__':
	while True:
		respuesta = int(input("""Que desea hacer?:\n(1)Realizar una prueba aleatoria y mostrar resultados en una tabla\n(2)Realizar una prueba aleatoria y mostrar resultados en una gráfica (no recomendado para poblaciones con más de 20 individuos)\n(3) Realizar (1) y (2) a la vez\n(4)Salir\n"""))
		
		if respuesta not in range(1,5):
			print('debe seleccionar una opción válida.')
			continue
		
		if respuesta == 4:
			break
		
		if respuesta == 3:
			while True:
				try:
					n = int(input('Inserte el tamaño de la población:  '))
					if n%2 == 1:
						print('Para faciltar el calculo del torneo, n debe ser par')
						continue
					data = preparar_data(n)
					imprimir_tabla(data)
					grafico_barras(data)
					break
				except:
					print('Debe insertar un número entero.')
					continue
		
		if respuesta == 2:
			while True:
				try:
					n = int(input('Inserte el tamaño de la población:  '))
					if n%2 == 1:
						print('Para faciltar el calculo del torneo, n debe ser par')
						continue
					data = preparar_data(n)
					grafico_barras(data)
					break
				except:
					print('Debe insertar un número entero.')
					continue
		
		if respuesta == 1:
			while True:
				try:
					n = int(input('Inserte el tamaño de la población:  '))
					if n%2 == 1:
						print('Para faciltar el calculo del torneo, n debe ser par')
						continue
					data = preparar_data(n)
					imprimir_tabla(data)
					break
				except:
					print('Debe insertar un número entero.')
					continue


	
