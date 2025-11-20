def pick_even(*args):
    args = list(map(int,input().split()))
    even_number = []
    for i in args :
        if i % 2 == 0 :
            even_number.append(i)
    return even_number        

print(pick_even())