print('hello cancan')

tree = [
    '                       *',
    '                      ***',
    '                     *****',
    '                    *******',
    '                       |  ',
]

for line in tree:
    print(line)

def pingfang(number):
    for i in range(1, number + 1):
        print('%dx%d=%d' % (i, i, i * i), end=' ')

def suibian(times):
    for x in range(1, times + 1):
        for i in range(1, 18):
            for j in range(1, 18):
                if (j <= i):
                    print('%dx%d=%d' % (i, j, i * j), end=' ')
            print('\n', end='')

suibian(1)
pingfang(1000)
