def cycle(collection):
    while True:
        for i in collection:
            yield i

a = cycle([0, 1, 2])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
