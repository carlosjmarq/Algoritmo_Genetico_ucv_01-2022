import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from operadores import *

def imprimir_tabla(pob1: list, pob2:list):
	print(f'pob1 len es {len(pob1)}')
	print(f'pob2 len es {len(pob2)}')
	tabla = PrettyTable()
	tabla.field_names = ('Pob inicial','valor0','fitness0','','Pob final','valor1','fitness1')
	for i in range(len(pob1)):
		tabla.add_row([
			pob1[i].reales,
			pob1[i].valor,
			pob1[i].fitness,
			'',
			pob2[i].reales,
			pob2[i].valor,
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