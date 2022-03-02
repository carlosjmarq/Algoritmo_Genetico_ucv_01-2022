import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from operadores import *

def imprimir_tabla(pob1: list, pob2:list):
	print(f'pob1 len es {len(pob1)}')
	print(f'pob2 len es {len(pob2)}')
	tabla = PrettyTable()
	tabla.field_names = ('Pob inicial','fitness0','','Pob final','fitness1')
	for i in range(len(pob1)):
		tabla.add_row([
			pob1[i].reales,
			pob1[i].fitness,
			'',
			pob2[i].reales,
			pob2[i].fitness
		])
	print(tabla)
	return

def imprimir_prueba(poblacion:list):
	tabla = PrettyTable()
	tabla.field_names = ('real','valor','fitness','p_seleccion')
	for i in range(len(poblacion)):
		tabla.add_row([
			poblacion[i].reales,
			poblacion[i].valor,
			poblacion[i].fitness,
			poblacion[i].p_seleccion,
		])
	print(tabla)
	return

def imprimir_mejor_ind(mejor_ind:dict, poblacion:list):
	print(f'El mejor individuo se encontro en la ronda {mejor_ind["ronda"]}')
	print(f'valor: {mejor_ind["ind"].reales}\nfitness: {mejor_ind["ind"].fitness}')
	print(f'Esta presente en la ronda final?: {mejor_ind["ind"].valor in [ind.valor for ind in poblacion]}')
	print('El mejor individuo de la poblacion final es:')
	pob_final = sorted(poblacion,key=lambda ind: ind.fitness)
	pob_final.reverse()
	mejor_final = pob_final[0]
	print(f'valor: {mejor_final.reales}\nfitness: {mejor_final.fitness}')
	pass