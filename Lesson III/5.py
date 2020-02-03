def f():
    s=list(map(float,input().split()))
    print(s)
    m=s[0]
    for i in range(len(s)):
        if abs(s[i])<abs(m):
            m=s[i]
    return m
    
#f()
