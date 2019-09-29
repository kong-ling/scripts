import os
import sys

src = 'A CHEF HIDE A BED'


encrypo = {
    'A':'1',
    'B':'2',
    'C':'3',
    'D':'4',
    'E':'5',
    'F':'6',
    'G':'7',
    'H':'8',
    'I':'9',
    ' ':' ',
}
decrypo = {
    '1':'A',
    '2':'B',
    '3':'C',
    '4':'D',
    '5':'E',
    '6':'F',
    '7':'G',
    '8':'H',
    '9':'I',
    ' ':' ',
}
def convert(s):
    dst = ''
    print('%s: \n%s' % (sys._getframe().f_code.co_name, s))
    for ch in s:
        if ch in encrypo.keys():
            dst += encrypo[ch]
        else:
            dst += ('*')

    return dst

def reverse(s):
    print('%s: \n%s' % (sys._getframe().f_code.co_name, s))
    dst = ''
    for ch in s:
        if ch in decrypo.keys():
            dst += decrypo[ch]
        else:
            dst += ('*')

    return dst

dest = convert(src)

print(dest)
print(reverse(dest))
print(reverse('1234 658921'))

print(convert('DEAD BEEF CAFE Gkl'))
