def print_params(params: dict):
	for var in params['variables']:
		print('Variable {}:'.format(var['nombre']))
		print('    dominio: {}'.format(str(var['limites'])))
		print('    precisión: {}'.format(10**(var['precision']*-1)))
		print('    número de bits asignados: {}'.format(var['num_bits']))
		print('\n')
	return