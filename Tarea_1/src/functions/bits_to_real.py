
def bits2float(bits: list, params: dict):
	last_index = 0
	for var in params['variables']:
		sub_bits = bits[last_index:last_index+var['num_bits']]
		print('el string de {} es: {}'.format(var['nombre'],sub_bits))
		last_index += var['num_bits']
		substring = sum([2**i*int(bit) for i,bit in enumerate(reversed(sub_bits))])
		print('el substring de {} es: {}'.format(var['nombre'],substring))
		real = min(var['limites'])+substring*(max(var['limites']) - min(var['limites']))/(2**var['num_bits']-1)
		real = round(real, var['precision'])
		print('El valor real de la variable {} es: {}'.format(var['nombre'],real))
	return 