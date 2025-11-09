def print_times (name,n=1):
    '''
    print name , n times
    agar n o nadade bod n = 1 beshe
    '''
    for i in range(n):
        print(name)

print_times('Amirsale',5)
print_times('sara')

def tavan ( n , t=2) :
    '''
    n ro be tavan t miresone agaram t nadim be tavan 2 mikone
    '''
    javab = 1 
    for i in range (t) :
        javab *= n
    return javab    

print ( tavan(2,3))  


def sum_of_two (n1,n2=10):
    '''
    do adad n1 va n2 ro ba ham jam mikone va agr n2 ro nadim on ro mosavi 10
    '''    
    return n1 + n2

print(sum_of_two(1,45))
print(sum_of_two(10))
print(sum_of_two('hello',' amir'))