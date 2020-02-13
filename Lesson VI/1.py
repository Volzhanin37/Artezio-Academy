class EvenIterator(object):

    def __init__(self, l):
        self.l = l
        self.limit = len(l)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.even_index = self.counter
            self.counter += 2
            return self.l[self.even_index]
        else:
            raise StopIteration

list1 = [0, 1, 2, 3, 4]
ev_it = EvenIterator(list1)

for i in EvenIterator(list1):
    print(i)
