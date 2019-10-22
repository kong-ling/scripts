class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        print(self.value)
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self

ti = TestIterator()
print(list(ti))


nested =[[1,2], [3, 4], [5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            print(element)
            yield element

print(list(flatten))

for numb in flatten(nested):
    print(numb)
