def make_dict(keys, values):
    return ({key: values[num] if num < len(values)
            else None for num, key in enumerate(keys)})

a = [1, 2, 3, 4]
b = [1, 2, 3]
c = [1, 2, 3, 4, 5]
print(make_dict(a, b))
print(make_dict(a, c))
