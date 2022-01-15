from pickletools import bytes1


abc = '100010101'

index = [5, len(abc)]
bits = list(abc)
last_index = 0
for i in index:
	print(bits[last_index:i+last_index])
	last_index = i