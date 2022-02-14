import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from numpy.random import rand, randint, shuffle

class Individuo():
	def __init__(self,params: dict):
		self.nombre = params['nombre']
		self.valor = params['valor']
		self.fitness = params['fitness']
		self.p_seleccion = params['p_seleccion']
		self.v_esperado = params['v_esperado']
		self.reales = None
		pass
