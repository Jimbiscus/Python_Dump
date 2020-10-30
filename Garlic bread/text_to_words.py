a = "PYTHON"

b = "Python"
print(a.upper() == b.upper())
t = []

text = "Aujourd'hui on cuisine des pains à l'ail.\nEt ça va être déliceux."

lines =  text.split("\n")
print(lines)

for line in lines:
    t += line.split(" ")

print(t)
