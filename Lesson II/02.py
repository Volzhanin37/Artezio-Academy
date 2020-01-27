a,b,c = map(int, input('введите 3 числа через пробел: ').split())
n = 0
for i in range(a,b):
    if i%c == 0:
        n += 1
print(f"{n} чисел между {a} и {b} делятся на {c}")
