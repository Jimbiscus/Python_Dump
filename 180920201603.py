l1 = [1, 5, 6]
l2 = [2, 5, 3]

print(l1 + l2)

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 5, "d": 4}

d1.update(d2)
print(d1)  # la derniere valeur de "a" est conservée
