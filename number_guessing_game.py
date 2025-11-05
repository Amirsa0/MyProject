from random import randint
number = randint(1,10)
guess_your_number = int (input("please gussing your number !?"))

if (guess_your_number == number) : 
    print('woow thats true !!!!')
else:
    print (f"wrong !!! , {number} is true")    