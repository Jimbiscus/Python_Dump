nom = ["M", "A", "R", "C"]
print(nom[-2])
# remove = nom.remove(-2)
# ajoute = nom.append(-2, "*")
print(nom)


langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript"]
print(langs)

lang = langs.pop(3)
print("{0} was removed".format(lang))

lang = langs.pop()
print("{0} was removed".format(lang))

print(langs)

langs.remove("Ruby")
print(langs)
