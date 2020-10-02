# word = "Marc"
mot = input("Entrer mot : ")

# letter_to_replace = "a"
letter_to_replace = input("Entrer lettre : ")
replacement_char = ""

counter = 0
new_string = "*"
for letter in list(mot):
  if letter == letter_to_replace:
    counter += 1
    print(m[:counter] + new_string + word[counter + 1:])# Ecrit ton programme ici ;-)
