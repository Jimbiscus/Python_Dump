def is_in_order(txt):
    sortedTxt = sorted(txt)
    sortedString = "".join(sortedTxt)
    if sortedString == txt:
        return True
    else:
        return False

print(is_in_order("abcddzazzefg"))
