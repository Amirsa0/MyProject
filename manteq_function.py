def is_even(n):
    '''
    returns True if the provided value is even 
    '''

    return(n % 2 == 0)

print(is_even(30))

def number_of_evens(nums):
    '''
    return how many nums is even
    '''
    count = 0
    for n in nums :
        if n % 2 == 0 :
            count += 1 
    return count    

def number_of_evens_2 (nums) :
    count = 0 
    for n in nums :
        if  is_even(n):
            count +=1
    return(count)        

print(number_of_evens_2([2,4,6]))
