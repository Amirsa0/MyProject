l = [0,0.45,9,-1,8]
# new_l = []

# for i in l : 
#     new_l.append(i*2)
# print(new_l)    

new_l = [n*2 for n in l ]

print(new_l)

a = 5
if a % 2 == 0 : 
    res = "zoj"
else:
    res = "fard"

print(res)

res_2 = "fard" if a % 2 != 0 else 'zoj'
print(res_2) 


new_l_2 = [n for n in l  if n%2 == 0]
print(new_l_2)

list = [1,2,8,6,9]

list1=['zoj' if n % 2 == 0 else 'fard' for n in list]

print(list1)

list2 = ['Hope' if n%3==0 else n for n in range (1,12)]
print(list2)

