def chain(*args):
    for arg in args:
        for i in arg:
            yield i


a = chain([1, 2, 3], [4, 5, 6])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
