from algoritmo import *
from solicitud_parametros import *
from operadores import poblacion_constructor
from printers import *

if __name__=='__main__':
	parametros = solicitud_parametros()
	while True:
		respuesta = int(input("""Que desea hacer?:\n(1)Correr Algoritmo\n(2)Modificar parámetros\n(3)Salir\n"""))
		if respuesta not in range(1,4):
			print('debe seleccionar una opción válida.')
			continue
		if respuesta == 3:
			break
		if respuesta == 2:
			parametros = solicitud_parametros()
			continue
		if respuesta == 1:
			pob0 = poblacion_constructor(parametros['n_pob'] or 50, parametros['variables'])
			if not parametros['n_gen']:
				pob_final = AGS(f1 if parametros['funcion']=='1' else f2, parametros['variables'],max=parametros['max'],poblacion=pob0)
			else:
				pob_final = AGS(f1 if parametros['funcion']=='1' else f2, parametros['variables'],max=parametros['max'],
				n=parametros['n_pob'],n_gen=parametros['n_gen'],p_cruce=parametros['p_cruce'],
				p_muta=parametros['p_muta'],poblacion=pob0)
			pob0 = pob0[0:parametros['n_pob'] or 50]
			imprimir_tabla(pob0,pob_final)
			continue