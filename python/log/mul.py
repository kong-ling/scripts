for i in range(1, 10):
    for j in range(i, 10):
        print('{:3}x{:3}={:3}'.format(i, j, i*j), end=', ')
    print('\n')

print([(x, y) for x in range(10) for y in range(10)])

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

def print_params(*params):
    print(params)

print_params('Testing')
print_params(1, 2, 3)
