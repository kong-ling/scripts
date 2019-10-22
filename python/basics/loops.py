from math import sqrt

for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Didn't find it!"


#while True:
#    word = raw_input('Please enter a word: ')
#    #process the word
#    if not word: break
#    print 'The word was ' + word

#print square values

for x in range(21):
    for y in range(21):
        if y >= x:
            if y == x:
                print
            print '%2dx%2d=%3d' % (x, y, x*y),

for x in range(21):
    print ('%30s') % ('*' * x)
