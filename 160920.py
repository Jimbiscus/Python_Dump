# Ecrit ton programme ici ;-)
print("Bonjour")
rep = input("Vous allez bien ? ")

if rep == "Oui" or rep == "oui" or rep == "OUI" or rep == "oUi":
    print("Bonne journée")
elif rep == "Non" or rep == "non" or rep == "NON" or rep == "nOn":
    print("Ca va aller...")
else:
    print("Input Incorrect")

pin = input("PIN CODE ? ")
pin = int(pin)
if pin == 1111:
    print("YES !!!!!")
while pin != 1111:
    print("Pin Incorrect")
    break

