def add_indexes(lst):
    n = 0
    for i in lst:
        lst[n] = lst[n] + n
        n = n + 1
    return lst

l = [1, 4, 5, 9, 0]
print(add_indexes(l))
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print (factorial(5))
