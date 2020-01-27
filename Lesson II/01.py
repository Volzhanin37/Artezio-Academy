def sq_of_odd(X):
    num_of_n = 0
    for n in range(1,X+1,2):
        print(n*n, end=' ')
        num_of_n += 1
    print()     
    print(f"Нечетных чисел в интервале [0:{X}]: {num_of_n}")
