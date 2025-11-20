def sum_name (*args) :
    args = list(map(int,input().split()))
    res=0
    if not args :
        return 0
    else:    
        for i in args : 
           res += i
        return res

print(sum_name())       