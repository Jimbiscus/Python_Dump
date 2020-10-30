:
            list_of_fwords.append(word)


print(f"Il y a {count_words} mots qui finissent par e .")

for word in list_of_words:
    print(f" - {word}")
print(f"il y a {count_fwords} mots qui commencent par f")
for fword in list_of_fwords:
    print(f" - {fword}")
words_count = {}
longestF = []
for fword in list_of_fwords:
    print(f"{len(fword)} - {fword}" )



for word in words:
    if len(word) > 4:
        word = word.lower()
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

more =  max(words_count.values())

print(f"Les mots le plus répété apparaissent {more} fois.")
print(f"Liste des mots trouvés {more} fois:")

for key, value in words_count.items():
    if value == more:
        print(f" - {key}")



