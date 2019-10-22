ten_things = 'apples oranges crows telephone light sugar'


stuff = ten_things.split(' ')
print stuff

more_stuff = ['day', 'night', 'song', 'frisbee', 'corn', 'banana', 'girl', 'boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)


print 'there we go: ', stuff

print stuff[1]
print stuff[-1]

print stuff.pop()

print ' '.join(stuff)
