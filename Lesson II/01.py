X = int(input('Введите X: '))
num_of_n = 0
for n in range(1,X+1,2):
    print(n*n, end=' ')
    num_of_n += 1
print()     
print("Нечетных чисел в интервале [0:X]:", num_of_n)
