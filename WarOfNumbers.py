
def war_of_numbers(lst):
    evenSum = 0
    oddSum = 0
    result = 0
    even = []
    odd = []
    for n in lst:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    for m in even:
        evenSum += m
    for k in odd:
        oddSum += k
    if evenSum > oddSum:
        print(str(evenSum) + " is greater than " + str(oddSum))
        result = evenSum - oddSum
        return result
    else:
        print(str(oddSum) + " is greater than " + str(evenSum))
        result = oddSum - evenSum
        return result

print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
