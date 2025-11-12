donations = {
    'jadi':20 , 
    "sara":800 , 
    "amir":12 , 
    "hasan": 9 
}

def donationa_analysist (don) :
    person = ""
    total = 0 
    count = 0
    max_donation = 0
    for name , value in don.items() :
        total += value
        count += 1 
        if value > max_donation :
            person = name 
            max_donation = value

    avg = total // count        






    return avg , total , person
    

avg , total ,   max_person = donationa_analysist(donations)  

print(f"total donatios :{ total}")
print(f"average donation is {avg}")
print(f"thanks to {max_person}")
