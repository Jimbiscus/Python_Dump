from random import randint

words = ["arbre", "poutre", "chaise", "antilope", "fromage"]
index = randint(0, len(words) -1)
tries = 0
word = words[index]
user_word = "_" * len(word)


while user_word != word:
    tries += 1
    print(user_word)
    letter = input("Entrez une lettre : ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                user_word = user_word[:i] + letter + user_word[i+1:]
else:
    tries = str(tries)
    print("Cela vous a pris " + tries + " input pour deviner le mot")

print(user_word)

### autre solution (ligne 16)
# if word[i] == char:
# tmp += char
# else:
# tmp += user_word[i]
# user_word = tmp
