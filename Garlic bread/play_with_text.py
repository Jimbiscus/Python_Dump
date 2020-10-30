text_file = open("garlic-bread.txt")
text = text_file.read()
text_file.close()

words = []

lines = text.split("\n")

for line in lines:
    words += line.split(" ")

# cleaning

while "" in words:
    words.remove("")

while "-" in words:
    words.remove("-")

#remove unnecessary characters
removable_character = ["(", ")", "."]

for index in range(len(words)):
    word = words[index]
    for character in removable_character:
        word = word.replace(character, "")
    words[index] = word
    
# longuest word

l_word = 0
longuest_words = []

for word in words:
    if len(word) > l_word:
        longuest_words = [word]
        l_word = len(word)
    elif len(word) == l_word:
        if word not in longuest_words:
            longuest_words.append(word)

# count word with "s"
count_s = 0

for word in words:
    if "s" in word:
        count_s += 1

# word more repeated
more_repeated = 0
words_repeated = []

for word in words:
    occurence = 0
    for other in words:
        if other.lower() == word.lower():
            occurence += 1
    if occurence > more_repeated:
        words_repeated = [word.lower()]
        more_repeated = occurence
    elif occurence == more_repeated:
        if word.lower() not in words_repeated:
            words_repeated.append(word)
    
print(longuest_words) 
print(count_s)
print(more_repeated, words_repeated)
