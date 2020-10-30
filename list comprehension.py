boy_tuple = ("Marc", "Jolan", "Allan", "Harambe")

heterosexual_list = [boy for boy in boy_tuple if boy != "Jolan"]
print(heterosexual_list)


def find_even_nums(num):
    even = [number for number in range(1, num + 1) if number % 2 == 0]
    return even


print(find_even_nums(2))

l = ["ananas","gateau","chataigne","petanque","marguerite","saperlipopette","tahin"]

m = []

m = [i for i in l if i[0] == "a"]

print(m)
