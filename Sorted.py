# Write your code here :-)
Jim = [4, 6, 9, 1, 4, 2, 5, 9, 1, 1, 1]
Jim = sorted(Jim)
Jim2 = []
for n in Jim:
    if n not in Jim2:
        Jim2.append(n)

print(Jim2)
