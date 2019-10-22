from sys import argv
from os.path import exists

script, filename = argv

print "We're going to erase %r." % filename

print "If ou don't want that, hit CTRL-C (^C)."

print "If you do want that, hit RETURN."

raw_input('>')

print "Does the output file exist? %r" % exists(filename)

