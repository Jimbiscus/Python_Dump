from random import randint

number = [randint(0, 10), randint(0, 10)]

while number[-1] != number[-2]:
    rnd = randint (0, 10)
    number.append(rnd)

for n in number:
    print(n)
