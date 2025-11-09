def is_even(n):
    return(n % 2 == 0)

def get_odd_numbers (nums):
    '''
    return odd numbers in the list
    '''
    odd_nums = []
    for n in nums :
        if not is_even(n):
            odd_nums.append(n)
    return odd_nums        


my_list = [1,3,5,8,6,9,10,12,15,17,18,20]
my_odds_number = get_odd_numbers(my_list)
print(my_odds_number)