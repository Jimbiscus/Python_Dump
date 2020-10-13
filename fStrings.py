name = "Jimbo"
title = "gros batard"
person = {"name": "Jolan", "title" : "gros batardo"}

def to_uppercase(entry):
    return entry.upper()

print("Coucou, %s, %s." % (name,title)) # Don't use that, it's old

print("Salut, {name}. Tu es un {title}.".format(name=person["name"], title=person["title"]))

print("Salut, {name}. Tu es un {title}.".format(**person)) # this ain't bad

print(f"Salut, {name}. Tu es un {title} !") # this the bomb


print(to_uppercase(f"{name} est drole !"))

print(f"{name.upper()} est drole.")

name = "Eric"
profession = "comedian"
affiliation = "Monty Python"

message = (
    f"""Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
    """
)
print(message)
