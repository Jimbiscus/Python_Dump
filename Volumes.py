def setify(lst):
	lst2 = []
	for n in lst:
		if n not in lst2:
			lst2.append(n)
		return sorted(lst2)
