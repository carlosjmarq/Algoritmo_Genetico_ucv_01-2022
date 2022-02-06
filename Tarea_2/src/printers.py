import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from selection_methods import *

"""
data debe ser un diccionario con las siguientes keys:
data ={
	'poblacion': ...,
	'copias_esp': ...,
	'rul': ...,
	'sobra': ...,
	'univ': ...,
	'mues': ...,
	'tor_det': ...,
	'tor_proba': ...,
}
"""
def imprimir_tabla(data: dict):
	tabla = PrettyTable()
	tabla.field_names = ('ind','fitness','% seleccion', 'copias esp', \
		'ruleta', 'sobrante estocastico', 'universal estocastica', \
		'muestreo deterministico', 'torneo deterministico', 'torneo probabilistico')
	poblacion = data['poblacion']
	# copias_esp = valores_esperados(poblacion)
	# rul = ruleta(poblacion)
	# sobra = sobrante_estocastico(poblacion)
	# univ = universal_estocastica(poblacion)
	# mues = muestreo_deterministico(poblacion)
	# tor_det = torneo_deterministico(poblacion)
	# tor_proba = torneo_probabilistico(poblacion)
	orden = [int(ind['individuo'].split('_')[-1]) for ind in poblacion]
	poblacion = quicksort(poblacion, orden)
	poblacion.reverse()
	for index, ind in enumerate(poblacion):
		tabla.add_row([
			ind['individuo'],
			ind['fitness'],
			ind['p_seleccion'],
			data['copias_esp'][index],
			len([survivor for survivor in data['rul'] if survivor['individuo']==ind['individuo']]),
			len([survivor for survivor in data['sobra'] if survivor['individuo']==ind['individuo']]),
			len([survivor for survivor in data['univ'] if survivor['individuo']==ind['individuo']]),
			len([survivor for survivor in data['mues'] if survivor['individuo']==ind['individuo']]),
			len([survivor for survivor in data['tor_det'] if survivor['individuo']==ind['individuo']]),
			len([survivor for survivor in data['tor_proba'] if survivor['individuo']==ind['individuo']]),
		])
	print(tabla)
	return

def grafico_barras(data: dict):
	#estructurar data
	poblacion = data['poblacion']
	orden = [ind['fitness'] for ind in poblacion]
	poblacion = quicksort(poblacion, orden)
	poblacion.reverse()
	rul, sobra, univ, mues, tor_det, tor_proba = [],[],[],[],[],[]
	copias_esp = valores_esperados(poblacion)
	for index, ind in enumerate(poblacion):
		# copias_esp.append(len([survivor for survivor in data['copias_esp'] if survivor['individuo']==ind['individuo']]))
		rul.append(len([survivor for survivor in data['rul'] if survivor['individuo']==ind['individuo']]))
		sobra.append(len([survivor for survivor in data['sobra'] if survivor['individuo']==ind['individuo']]))
		univ.append(len([survivor for survivor in data['univ'] if survivor['individuo']==ind['individuo']]))
		mues.append(len([survivor for survivor in data['mues'] if survivor['individuo']==ind['individuo']]))
		tor_det.append(len([survivor for survivor in data['tor_det'] if survivor['individuo']==ind['individuo']]))
		tor_proba.append(len([survivor for survivor in data['tor_proba'] if survivor['individuo']==ind['individuo']]))
	#Preparar grafica
	indice_barras = np.arange(len(poblacion))
	ancho = 0.07

	plt.bar(indice_barras, copias_esp, width=ancho, label='copias esperadas')
	plt.bar(indice_barras + ancho*1, rul, width=ancho, label='ruleta')
	plt.bar(indice_barras + ancho*2, sobra, width=ancho, label='sobrante estocastico')
	plt.bar(indice_barras + ancho*3, univ, width=ancho, label='universal estocastica')
	plt.bar(indice_barras + ancho*4, mues, width=ancho, label='muestreo deterministico')
	plt.bar(indice_barras + ancho*5, tor_det, width=ancho, label='torneo deterministico')
	plt.bar(indice_barras + ancho*6, tor_proba, width=ancho, label='torneo probabilistico')
	plt.legend(loc='best')
	plt.xticks(indice_barras + ancho*3, [str(ind['fitness']) for ind in poblacion])

	plt.ylabel('Numero de copias')
	plt.xlabel('Fitness')
	plt.title('Comparación de métodos de selección')
	
	plt.show()

	return