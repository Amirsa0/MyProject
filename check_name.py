names = ['amir','ali','sara']
people = {
    'amir':{'sen':25,'ghad':185} , 
    'sara':{'sen':12 , 'ghad':165}

}

for name in names :
    if name in people : 
        # we have this person
        # lets print sen
        print (f"I have {name} and sen is {people[name]['sen']}")
    else:
        print(f"I have no data for {name}")    
