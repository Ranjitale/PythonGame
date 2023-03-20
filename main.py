# Let's make a game with python which is our first game:

# Game no .1 Guessing the value of the number:
import random

a=random.randint(10,19)
print(a)

for i in range(4):
    b=int(input("Guess tha value : "))
    if a==b:
        print("Correct You won the match !") 
        break
    elif a>b:
        print("low")
        
    elif a<b:
        print("High")    
