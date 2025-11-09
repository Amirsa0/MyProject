def largest (nums):
    largest_number = 0 
    for n in nums :
        if n > largest_number : 
            largest_number = n 
    return largest_number        

my_nums = [1,2,3,8,9,13,5,6,9,10,30]    
largest_number = largest(my_nums)
print(largest_number)