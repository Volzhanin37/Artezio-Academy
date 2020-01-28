def range2(start=0, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0
    l = []
    i = start
    while ((start < stop and step > 0 and i < stop ) or 
    (start > stop and step < 0 and i > stop)):  
        l.append(i)
        i += step
    return l

#Test        
print(range2(0,5,1))   #[0, 1, 2, 3, 4]
print(range2(0,5))     #[0, 1, 2, 3, 4]
print(range2(5))       #[0, 1, 2, 3, 4]
print(range2(4,0,-1))  #[4, 3, 2, 1]
print(range2(4,0))     #[]
print(range2(0,5,-1))  #[]  
print(range2(4,0,1))   #[]  
