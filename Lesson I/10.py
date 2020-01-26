list1 = [1, 2, 3, 4, 5]
list2 = [0, 1, 2, 3, 4]
print(list(set(list1).symmetric_difference(set(list2)))) #определяем разницу, как все элементы, кроме общих для двух множеств
