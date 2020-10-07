def name_shuffle(txt):
    txt = txt.split()
    return txt[-1]+" "+txt[0]


print(name_shuffle("Grande Bite"))

jim = "jimo buso"
jim = jim.split()
print(jim)
print(jim[-1] +" "+jim[0])
print(name_shuffle("Donald Trump"))

string_to_reverse = "Donald Trump Junior"
string_to_list = string_to_reverse.split()
string_to_list.reverse()

print(' '.join(string_to_list))
print("Donald Trump".split()[-1]+" "+"Donald Trump".split()[0])
