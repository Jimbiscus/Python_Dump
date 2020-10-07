def cruzon(n):
    if ((2**n)+1) % ((2*n)+1) == 0:
        return True
    else:
        return False
print(cruzon(10))
