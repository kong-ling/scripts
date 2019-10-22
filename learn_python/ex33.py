numbers = []

def num_append(limit, offset):
    i = 0
    while i < limit:
        numbers.append(i)
        i += offset
        print "Numbers now: ", numbers

    return numbers


num_append(100, 6)

for num in numbers:
    print num
