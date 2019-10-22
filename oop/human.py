class Human(object):
    laugh = 'hahahaha'

    def __init__(self, more_words):
        print('We are happy birds.', more_words)

    def show_laugh(self):
        print(self.laugh)

    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()

li_lei = Human('Cool')
li_lei.laugh_10th()
