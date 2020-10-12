def count_characters(lst):
    length = len(lst)
    strLength = len(lst[0])
    return length * strLength

print(count_characters([
  "###",
  "###",
  "###"]))
