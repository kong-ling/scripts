import os
import sys

src_string = 'They are students.'
specified_letters = 'aeiou'

# remove specified letters from the src string
# src: the given string
# letters: letters to be removed
def remove_specified_letters(src, letters):
    for ch in src:
        if ch in letters:
            i = src.find(ch)
            src = src[:i] + src[i+1:]
            print(src)
    return src

if __name__ == '__main__':
    print(remove_specified_letters(src_string, 'ae'))
    print(remove_specified_letters(src_string, 'ts'))
    print(remove_specified_letters(src_string, specified_letters))
