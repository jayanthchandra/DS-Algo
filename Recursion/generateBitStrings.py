"""

Python Script to generate n bit strings 

"""

def generate_bit_strings(n):
	if n == 0:
		return []
	if n == 1:
		return ['0', '1']
	return [bit+otherbit for bit in generate_bit_strings(1) for otherbit in generate_bit_strings(n-1)]

print generate_bit_strings(2)