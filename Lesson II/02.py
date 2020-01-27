def num_of_div(a,b,c):
    n = 0
    for i in range(a,b):
        if i%c == 0:
            n += 1
    return n
