# Write your code here :-)
students = {"Albert" : 10, "Leopold": 30, "Baudouin": 20, "Gonzague" : 56, "Cunégonde": 76, "Ginette" : 53, "Roberte" : 99}

bestof = []

bestof = [name for name, score in students.items() if score >= 50]
print(bestof)
