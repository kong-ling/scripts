class FooBar:
    def __init__(self):
        self.somevar = 42

class FooBar1:
    def __init__(self, value=42):
        self.somevar = value


f = FooBar()
print(f.somevar)

f1 = FooBar1('this is a contructor argument')
print(f1.somevar)

class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)

b = Bird()
b.eat()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

fibs = Fibs()

for f in fibs:
    print(f)
    if f > 10000:
        print(f)
        break
