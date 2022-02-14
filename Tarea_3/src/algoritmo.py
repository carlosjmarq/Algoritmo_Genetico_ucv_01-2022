import numpy as np
import random
from operadores import *
from individuos import Individuo
from pprint import pprint
from printers import *

def AGS(func, variables, max=True, n=50, n_gen=100, p_cruce=0.8, p_muta=0.2, poblacion=None):
	#Generación de la primera población
	if not poblacion:
		poblacion = poblacion_constructor(n,variables)
	#Evaluacion inicial
	for ind in poblacion:
		ind.reales = bits2float(ind.valor,variables)
		ind.fitness = eval_fitness(ind,func,max)
	for ind in poblacion:
		ind.p_seleccion = ind.fitness/sum([indv.fitness for indv in poblacion])
	#Inicio del ciclo
	for iter in range(n_gen):
		#mezclar poblacion
		random.shuffle(poblacion)
		#aplicar cruce1
		for i in range(n//2):
			r = rand()
			if r>p_cruce:
				continue
			for hijo in cruce_2_puntos(poblacion[i], poblacion[n//2+i]):
				poblacion.append(hijo)
		#aplicar mutación
		for ind in poblacion:
			r = rand()
			if r>p_muta:
				continue
			ind = mutacion(ind)
		#evaluar población
		for ind in poblacion:
			ind.reales = bits2float(ind.valor,variables)
			ind.fitness = eval_fitness(ind,func,max)
		for ind in poblacion:
			ind.p_seleccion = ind.fitness/sum([indv.fitness for indv in poblacion])
		#Aplicar seleccion
		poblacion = muestreo_deterministico(poblacion)
		#evaluar población
		for ind in poblacion:
			ind.reales = bits2float(ind.valor,variables)
			ind.fitness = eval_fitness(ind,func,max)
		for ind in poblacion:
			ind.p_seleccion = ind.fitness/sum([indv.fitness for indv in poblacion])
		#ordenamiento y descarte de los menos aptos
		fitness_list = [ind.fitness for ind in poblacion]
		poblacion = quicksort(poblacion,fitness_list)
		poblacion = poblacion[0:n]
		imprimir_prueba(poblacion)
	return poblacion

variables = [
	{'nombre':'x', 'limites': (-8,8), 'bits': 6},
	{'nombre':'y', 'limites': (-4,4), 'bits': 4},
]

def f1(x,y):
	return x**2 +2*y**2 -0.3*np.sin(3*np.pi*x)-0.4*np.cos(4*np.pi*y)+0.4

def f2(x,y,z):
	return (x*x+y*y)**0.25*(1+np.sin(50*(x*x+y*y)**0.1)**2) + (x*x+z*z)**0.25*(1+np.sin(50*(x*x+z*z)**0.1)**2) + (z*z+y*y)**0.25*(1+np.sin(50*(z*z+y*y)**0.1)**2)