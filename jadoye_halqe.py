n = int(input())
x = int(input())
counter = 0

while counter != n :
    if x%2 == 1 :
        x = (x*2)-1
    elif x%2 == 0 :
        x = x/2
    counter += 1


print(f"{x:0.0f}")