l = ['abc', 'xyz', 'aba', '1221']
num = 0
for s in l:
    if len(s)>=2 and s[:1] == s[-1:]:
        num += 1
print(num)
