listo = ["a", "b", "c"]


def mapping(listo):
    dicto = {}
    for i in listo:
        dicto[i] = i.upper()
    return dicto

print(mapping(listo))
