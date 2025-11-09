def hello () :
    print('hello world !')

hello()

def hello_1 (name):
    '''
    this function says hello to the name , 
    to the length of name 

    '''

    for i in range(len(name)) :
        print(f'oh hello {name}')

hello_1('Amirsaleh')   

def hello_2_n_times(name,n):

    '''
    this function says hello to the name , n times.
    '''

    for i in range (n):
        print(f"hello {name}")


hello_2_n_times('Sara',5)        


def  sum_of_two_numbers (a,b):
    '''
    this fuction sum a , b
    '''
    res = a + b
    return(res)

javab = sum_of_two_numbers(4,5)
print(javab)

def chandta_toosh (s,c):
    '''
    gets a string and a character and returns the numbers thas characters repeatitions in that string
    '''

    counter = 0 
    for this_character in s :
        if this_character == c :
            counter += 1 
    return (counter)     

name = 'jadidan'
print(f"{name} has {chandta_toosh(name,'a')} ")  

