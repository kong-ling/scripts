from sys import argv
from os.path import exists

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1:%r, arg2:%r" % (arg1, arg2)


print_two('first', '2nd')


#Ok, that *args is actually pointless, we can just do this
def print_two_again(args1, arg2):
    print "arg1:%r, arg2:%r" % (arg1, arg2)


print_two_again('first', '2nd')
