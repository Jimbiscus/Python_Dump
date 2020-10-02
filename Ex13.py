from random import randint

number = randint(0, 10)
print(number)
if number > 9:
    print("Score maximum")
elif number > 5:
    print("Bon score")
else:
    print("Score correct")
