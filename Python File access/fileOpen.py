
dividables = []

file = open("file_2.txt", "r")
for line in file.readlines():
    if int(line) % 7 == 0:
        dividables.append(line[:-1])
file.close()




file = open("result.txt", "w")

file.write(str(dividables))
print("Results Written")
file.close()
