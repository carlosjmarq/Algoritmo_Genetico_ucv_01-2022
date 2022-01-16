import numpy as np
from decimal import Decimal, ROUND_UP

def float2bits(reales: list, params: dict):
	print('\n')
	string = []
	for i,var in enumerate(params['variables']):
		substring = int(Decimal( (reales[i]-min(var['limites']))*(2**var['num_bits']-1)/(max(var['limites'])-min(var['limites'])) )\
				.quantize(Decimal('0.'), rounding=ROUND_UP))
		print('El substring de {} es: {}'.format(var['nombre'], substring))
		bits = []
		while substring not in (0,1):
			bits.append(substring%2)
			substring //= 2
		bits.append(substring)
		if len(bits) != var['num_bits']:
			for i in range(var['num_bits']-len(bits)):
				bits.append(0)
		bits = [bit for bit in reversed(bits)]
		print('El valor en bits de {} es: {}'.format(var['nombre'], bits))
		for bit in bits:
			string.append(bit)
	print('El valor del string de todas las variables es: {}\n'.format(string))
	return