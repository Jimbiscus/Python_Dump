def abcmath(a, b, c):
    for b in range(b):
        a += a
    if a % c == 0:
        return True
    else:
        return False

print(abcmath(5, 2, 10))


def cap_to_front(s):
    upperList = []
    lowerList = []
    for i in s:
        if i.isupper() == True:
            upperList.append(i)
        else:
            lowerList.append(i)
    upperWord = "".join(upperList)
    lowerWord = "".join(lowerList)
    result = upperWord + lowerWord
    return result

print(cap_to_front("hApPy"))
print(cap_to_front("moveMENT"))
print(cap_to_front("shOrtCAKE"))
