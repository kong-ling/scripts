import os
import sys

datas = [11, 22, 10, 30, 50, 80, 17, 100]

print('\nDefault:')
def sort_default(numbers):
    '''simple output'''
    for d in numbers:
        print(d, end=', ')
    print('\n')


def sort_bubble(numbers):
    '''bubble output'''
    temp = numbers[0]
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] >= numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                #print(numbers[j], numbers[j+1])
        sort_default(numbers)

    return numbers

sort_default(datas)

print('\nBubble:')
sort_default(sort_bubble(datas))
