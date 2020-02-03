def average(a, b, c, d, max_arg=[]):
    if not max_arg:
        max_arg.append(max(a, b, c, d))
    if max_arg[0] < max(a, b, c, d):
        max_arg[0] = max(a, b, c, d)
    return (a+b+c+d)/4, max_arg[0]

# print(average(1,2,3,5))
# print(average(1,2,3,10))
# print(average(1,2,3,15))
# print(average(1,2,3,9))
