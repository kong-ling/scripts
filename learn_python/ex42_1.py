from sys import exit
from random import randint

class Game(object):
    
    def __init__(self, start):
        self.quips = [
           "you died."]

        self.start = start

    def play(self):
        next = self.start

        while True:
            print('\n')
            room = getattr(self, next)

            next = room()

    def death(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)

    def central_corridor(self):
        print('The Gothon of Planet Percal')

        action = raw_input('> ')

        if action == 'shoot!':
            print('shoot')
            return 'death'
        elif action == 'dodge!':
            print('dodge!')
            return 'death'
        elif action == 'tell a joke':
            print('Lucky for you they made you learn Gothon insults in the academy')
            return 'laser_weapon_armory'
        else:
            print('DOES NOT COMPUTE!')

    def laser_weapon_armory(self):
        print('You do a dive roll into the Weapon Armory')
        code = '%d%d%d' % (randint(1, 9), randint(1, 9), randint(1, 9))
        print('code=%s' % code)
        guess = raw_input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print('BZZZEDDD!')
            guesses += 1
            guess = raw_input('[keypad]> ')

        if guess == code:
            print('the container clicks open')
            return 'the_bridge'
        else:
            print('ship from their ship and your die')
            return 'death'

    def the_bridge(self):
        print('YOu burst onto the Bridge')

        action = raw_input('> ')

        if action == 'throw the bomb':
            print('it goes off.')
            return 'death'
        elif action == 'slowly place the bomp':
            print('get off this tin can')
            return 'escape_pod'
        else:
            print('DOES NOT COMPUTE!')
            return 'the_bridge'

    def escape_pod(self):
        print('Which one do you take?')

        good_pod = randint(1, 5)
        guess = raw_input('[pod #]> ')

        if int(guess) != good_pod:
            print('crushing your body into jam jelly')
            return 'death'
        else:
            print 'you jump into pod %s and hit the eject button' % guess
            exit(0)

a_game = Game('central_corridor')
a_game.play()
