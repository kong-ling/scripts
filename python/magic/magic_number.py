x = 142857

def sum_of_number(num):
    numbers = []
    while True:
        res = num//10
        mod = num%10
        #print(res, mod)
        numbers.append(mod)
        if res > 0 :
            num = res
            pass
        else:
            break
    sum = 0
    for d in numbers:
        sum += d
    #print(sum),
    return sum

#sum_of_number(12345)
for i in range(1, 14):
    y = x*i
    #sum_of_number(y),
    print('%d x %3d = %8d(sum=%d)' % (x, i, y, sum_of_number(y)))
