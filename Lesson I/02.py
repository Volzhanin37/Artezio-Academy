S = list(input('enter the string: '))
d={}
for i in range(len(S)):
    d[S[i]] = S.count(S[i])
print(d)
