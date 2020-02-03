def f4(*args, **kwargs):
    def unpack(x, a=[]):
        for i in x:
            if isinstance(i, (list, tuple)):
                unpack(i)
            else:
                a.append(i)
        return a

    unp_nums = unpack(list(args) + list(kwargs.values()))
    f4_sum = sum(unp_nums)
    f4_mult = 1
    for num in unp_nums:
        if num != 0:
            f4_mult *= num
    return f4_mult, f4_sum
# print(f4(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))
# не реализовал проверку на циклические ссылки
