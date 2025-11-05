number = int(input())

if number % 3 == 0 and number % 5 == 0 : 
    print(f"افسانه ای")
elif number % 3 == 0 :
    print(f" جادویی")
elif number % 5 == 0 :
    print(f" نفرین شد")
else:
    print(" معمولی")  