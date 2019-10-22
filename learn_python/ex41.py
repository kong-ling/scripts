from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda such at this.",
             "Nice job, you died ... jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    
    print quip[randint(0, len(quips) - 1)]
    exit(1)
