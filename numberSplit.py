
def number_split(n):
    l = []
    half = n//2
    halfPlusOne = half + 1
    if n % 2 == 0:
        l.append(half)
        l.append(half)
        return l
    else:
        l.append(half)
        l.append(halfPlusOne)
        return l
print(number_split(-5))
