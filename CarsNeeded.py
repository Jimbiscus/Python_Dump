def name_shuffle(txt):
    l = []
    l2 = []
    for n in txt:
        if n != " ":
            l.append(n)
        else:
            l2.append(n)
    l2 = l2[1:]
    "".join(l[])
    "".join(l2[])
    return str(l2) + " " + str(l)
	
print(name_shuffle("Bobby Slave"))
