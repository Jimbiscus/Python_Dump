l = [1, 2]
n = 10

for n in range(n - 2):
    a = l[-2] + l[-1]
    l.append(a)
    print(l)
