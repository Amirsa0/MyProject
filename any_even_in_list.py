def is_even (n):
    return( n % 2 == 0)


def any_even_in_list (nums) :
    '''
    return True if any of numbers is even
    '''
    has_even = False

    for n in nums : 
        if is_even(n) :
            has_even = True
    return has_even       


my_numbers = [1,3,5]
print(any_even_in_list(my_numbers))

def any_even_in_list_2 (nums):

    for n in nums :
        if is_even(n):
            return True
    return False    

print(any_even_in_list_2(my_numbers))    