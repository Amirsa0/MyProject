def skyline (*args) :
    args = list(map(int,input().split()))
    higher = 0
    if not args :
        return 0
    for i in args : 
        if i > higher :
            higher = i
    return higher
        
print(skyline())        