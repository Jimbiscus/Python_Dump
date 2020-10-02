
def num_layers(n):
	thicc = "0.0005m"
	thicc = float(thicc[:-1]) * (2 ** n)
	return thicc

print(num_layers(5))
print(num_layers(21))
# Write your code here :-)
