import numpy as np
from decimal import Decimal, ROUND_UP

def calcular_parametros(params: dict):
	if params['usar_precision']:
		for var in params['variables']:
			var['num_bits'] = int(Decimal(np.log((max(var['limites'])-min(var['limites']))*(10**var['precision'])+1)/np.log(2))\
				.quantize(Decimal('0.'), rounding=ROUND_UP))
	else:
		for var in params['variables']:
			var['precision'] = int(Decimal(np.log((2**var['num_bits']-1)/(max(var['limites'])-min(var['limites'])))/np.log(10))\
				.quantize(Decimal('0.'), rounding=ROUND_UP))
	params.update({
		'bits_totales': sum([var['num_bits'] for var in params['variables']])
	})
	return params