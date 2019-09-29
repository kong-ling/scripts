def factorial(n):
    if n == 1:
        return 1
    else:
        return n* factorial(n-1)

def power(x, n):
    if n == 0:
        return 1
    else:
        return x* power(x, n-1)


for i in range(1, 10):
    print(factorial(i))

print(power(2, 10))

def search(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper)//2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


print(search(range(100), 50, 0, 98))
