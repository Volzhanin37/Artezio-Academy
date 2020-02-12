n = int(input())
list1 = []
for i in range(n):
    a, b = input().split()
    list1.append(a)
    list1.append(b)
for i in range(0, len(list1), 2):
    try:
        print(int(list1[i])//int(list1[i+1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
