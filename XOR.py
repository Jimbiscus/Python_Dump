def XOR(a, b):
	a ^= b
	b ^= a
	a ^= b
	return [a, b]

print(XOR(10, 50))

a, b = 5, "Jimbo"
a, b = b, a

print(a)
print(b)
