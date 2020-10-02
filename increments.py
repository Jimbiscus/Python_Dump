monster = 4
monster = monster + 1
monster += 1

monster = monster - 2
monster -= 2

monster *= 2
monster /= 6

text = "Mot "
text *= 6
print(text)

a = 10 // 3
print(a)

iban = "BE85310113967006"
bban = iban[4:]
num = bban[:-2]
num = int(num)

verif = bban[-2:]
verif = int(verif)
if num % 97:
    print("Valid")
else:
    print("error")

num = int(iban[4:-2])
verif = int(iban[-2:])

if (verif == num % 97):
    print("Ok!")
