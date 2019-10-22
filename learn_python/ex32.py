hairs = ['brown', 'blond', 'red']
eys = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]


for hair in hairs:
    print "%s is used" % hair
merges = [hairs, weights]
for merge in merges:
    print "%s is used" % merge



elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)


for i in elements:
    print "Element was: %d" % i
