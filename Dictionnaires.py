# d = {"a": 1, "b" : 2, "c" : 3}
# print(d["b"])
dico = {}
dico["name"] = input("Entrez le nom du heros : ")
dico["power"] = input("Entrez son niveau de puissance : ")

print(dico)
print("Votre personnage s'appelle " + dico['name'] + ". Il a une puissance de " + dico['power'])

inventory = {"potion" : 1, "scroll": 2, "sword" : 0}
# pas obligé de mettre k ou v, va toujours renvoyer 2 valeurs : clés et valeurs
for k, v in inventory.items():
    print(k + " --> " + str(v))
for k in inventory.values():
    print(k)

#  supprimer quelquechose d'un dictionnaire

# del(dico["potion"]



# v = dico.pop("potion")
# print(v)
