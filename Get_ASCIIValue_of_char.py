print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))

a = "a"

print(ord(a))

def counterpartCharCode(char):
    char = char.swapcase()
    char = ord(char)
    return char

print(counterpartCharCode("b"))
