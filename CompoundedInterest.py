def compound_interest(p, t, r, n):
    formula = p * (1 + (r/n)) ** ( n * t)
    return formula

print(compound_interest(10000, 10, 0.06, 12))
