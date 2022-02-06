import numpy as np
from numpy.random import rand, randint, shuffle

""" Se tendrá en cuenta que una población será una lista de diccionarios
	que van a contener tanto el individuo como otras cualidades (como su fitness). Ej:

	Pob = [
		{
			individuo: [1,0,1,0,0],
			fitness: 122,
			p_selección: 0.02315,
			etc
		},
		{
			individuo: [1,0,0,1,1],
			fitness: 201,
			p_selección: 0.05124,
			etc
		},
		...
	]

"""

def poblacion_constructor(n: int):
	poblacion = [
		{
			'individuo': 'ind_{}'.format(i),
			'fitness': randint(low=1,high=1000),
		} for i in range(n)
	]
	sum_fitness = sum([ind['fitness'] for ind in poblacion])
	for ind in poblacion:
		ind.update({
			'p_seleccion': ind['fitness']/sum_fitness
		})
	return poblacion

def valores_esperados(poblacion: list):
	fit_prom = sum([ind['fitness'] for ind in poblacion])/len(poblacion)
	valores_esperados = [ind['fitness']/fit_prom for ind in poblacion]
	return valores_esperados

def ruleta(poblacion: list):
	nueva_poblacion = []
	while len(nueva_poblacion) != len(poblacion):
		target = rand()
		sum = 0
		for i,ind in enumerate(poblacion):
			sum += ind['p_seleccion']
			if sum >= target:
				nueva_poblacion.append(poblacion[i])
				break
	return nueva_poblacion

def sobrante_estocastico(poblacion: list):
	# Versión sin reemplazo
	val_esp = valores_esperados(poblacion)
	parte_entera = [val//1 for val in val_esp]
	sobrante = [val%1 for val in val_esp]
	nueva_poblacion = []
	for index,val in enumerate(parte_entera):
		k=0
		while k != val:
			nueva_poblacion.append(poblacion[index])
			k+=1
	while len(nueva_poblacion) != len(poblacion):
		for index, val in enumerate(sobrante):
			r = rand()
			if r <= val:
				nueva_poblacion.append(poblacion[index])
			if len(nueva_poblacion) == len(poblacion):
				break
	return nueva_poblacion

def universal_estocastica(poblacion: list):
	nueva_poblacion = []
	offset = rand()
	targets = [(i+1)*1/(len(poblacion)+1)+offset if (i+1)*1/(len(poblacion)+1)+offset < 1 else (i+1)*1/(len(poblacion)+1)+offset-1 \
		for i in reversed(range(len(poblacion)))]
	targets.sort(reverse=True)
	sum=0
	for i, ind in enumerate(poblacion):
		sum += ind['p_seleccion']
		while True and len(targets) != 0:
			if sum < targets[-1]:
				break
			nueva_poblacion.append(ind)
			targets.pop()
	return nueva_poblacion

def muestreo_deterministico(poblacion: list):
	val_esp = valores_esperados(poblacion)
	parte_entera = [val//1 for val in val_esp]
	sobrante = [val%1 for val in val_esp]
	nueva_poblacion = []
	for index,val in enumerate(parte_entera):
		k=0
		while k != val:
			nueva_poblacion.append(poblacion[index])
			k+=1
	if len(nueva_poblacion) == len(poblacion):
		return nueva_poblacion
	poblacion = quicksort(poblacion,sobrante)
	for ind in poblacion:
		nueva_poblacion.append(ind)
		if len(nueva_poblacion) == len(poblacion):
			break
	return nueva_poblacion

def torneo_deterministico(poblacion: list):
	pob_aux = poblacion
	nueva_poblacion = []
	n = len(poblacion)
	while len(nueva_poblacion) != len(poblacion):
		shuffle(pob_aux)
		for i in range(n//2):
			nueva_poblacion.append(pob_aux[i] if pob_aux[i]['fitness'] >= pob_aux[i+n//2]['fitness'] else pob_aux[i+n//2])
	return nueva_poblacion

def torneo_probabilistico(poblacion: list):
	pob_aux = poblacion
	nueva_poblacion = []
	n = len(poblacion)
	flip = 0.5 + 0.5*rand()
	while len(nueva_poblacion) != len(poblacion):
		shuffle(pob_aux)
		for i in range(n//2):
			mas_apto = pob_aux[i] if pob_aux[i]['fitness'] >= pob_aux[i+n//2]['fitness'] else pob_aux[i+n//2]
			menos_apto = pob_aux[i] if pob_aux[i]['fitness'] < pob_aux[i+n//2]['fitness'] else pob_aux[i+n//2]
			r = rand()
			nueva_poblacion.append(mas_apto if r < flip else menos_apto)
	return nueva_poblacion

def quicksort(poblacion: list, probabilidades: list):
	pob_izq = []
	proba_izq = []
	pob_cen = []
	proba_cen = []
	pob_der = []
	proba_der = []
	if len(poblacion) > 1:
		pivote = probabilidades[int(rand()*len(poblacion))]
		for index, ind in enumerate(poblacion):
			if probabilidades[index] > pivote:
				pob_izq.append(ind)
				proba_izq.append(probabilidades[index])
			elif probabilidades[index] == pivote:
				pob_cen.append(ind)
				proba_cen.append(probabilidades[index])
			elif probabilidades[index] < pivote:
				pob_der.append(ind)
				proba_der.append(probabilidades[index])
		return quicksort(pob_izq,proba_izq)+pob_cen+quicksort(pob_der,proba_der)
	else:
	  return poblacion