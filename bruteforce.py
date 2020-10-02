code = "1234"

brute = "0000"

while brute != code:
    brute = int(brute)
    brute += 1
    brute = str(brute)
    print(brute)
    brute = "0" * (4 - len(brute)) + brute
