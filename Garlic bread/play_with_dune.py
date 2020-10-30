text_file = open("recette.txt")
text = text_file.read()
text_file.close()

words = []

lines = text.split("\n")

for line in lines:
    words += line.split(" ")

# cleaning

#remove unnecessary characters
removable_character = ["(", ")", ".", ",", "!", '"', "?", ":", ";", "'"]

for index in range(len(words)):
    word = words[index]
    for character in removable_character:
        word = word.replace(character, "")
    
    if word:
        if word[0] == "'":
            word = word[1:]
    if word:
        if word[-1] == "'":
            word = word[:-1]

    words[index] = word

while "" in words:
    words.remove("")

while "-" in words:
    words.remove("-")
  
# count word with "h" and "n"

list_of_words = []
list_of_fwords = []
count_words = 0
count_fwords = 0
for word in words:
    word = word.lower()

    if word[-1] == "e":
        count_words += 1
        if word not in list_of_words:
            list_of_words.append(word)
    if word[0] == "f" or word[0] == "F":
        count_fwords += 1
        if word not in list_of_fwords:
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



