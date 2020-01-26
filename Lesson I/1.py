S = input('enter passport data.(Constraints: 1-1000 characters): ')
if not (0<len(S)<1000):
    print ('Out of Constraints!')
else:
    S = S.split(' ')
    for i in range (len(S)):
        if S[i].isalpha(): # проверка, что слово является именем(не содержит цифр)   
            S[i] = S[i].capitalize()
    print(' '.join(S))
