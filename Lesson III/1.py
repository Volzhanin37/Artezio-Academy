def sqr(collection):
    a = []
    for elem in collection:
        a.append(elem*elem)
    return a
# print(sqr((1, 3)))


def even_pos(collection):
    a = []
    collection = list(collection)
    for i in range(1, len(collection), 2):  # отсчитывал нумерацию позиций с 1
        a.append(collection[i])
    return a
# print(even_pos((1, 2, 3, 4)))


def even_cubes(collection):
    a = []
    collection = list(collection)
    for i in range(1, len(collection), 2):
        if collection[i] % 2 == 0:
            a.append(collection[i]**3)
    return a
# print(even_cubes((1, 2, 3, 4)))




