skills = {"Puissance" : 10, "Magie" : 5, "Défense" : 3}
skills["Nom"] = input("Entrez le nom du heros : ")
for k, v in skills.items(): #pas obligé de mettre k ou v
    print(k + " : " + str(v))

