import random

runs = int(input("how many times you want to roll? 1,2 or 3?"))
           
def colour():
    if number < 18:
        return("small")
    else:
        return("big")

def oddeven():
    if number % 2 == 0:
        return("even")
    else:
        return("odd")
 
def redblack():
    if number<=10 or 19<=number<=28 and number % 2 != 0:
        return("red")
    else:
        return("black")

while runs != 1 and runs !=2 and runs !=3 :
    runs = int(input("wrong input try again.how many times you want to roll? 1,2 or 3?"))
for i in range(runs):
    number = int(random.uniform(1,36))
    print(number,colour(),oddeven(),redblack())
    

        





    
