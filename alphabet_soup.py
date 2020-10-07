def alphabet_soup(txt):
    soup = []
    txt = sorted(txt)
    for n in txt:
        soup.append(n)
    return ''.join(soup)

print(alphabet_soup("jimmelionnus"))
