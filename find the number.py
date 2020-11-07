import random

hiddenNumber = random.randint(1,29)
print('I am Thinking of a number')

for i in range(1,5):
    print("Try to find the hidden number")
    guess = int(input("Enter your number:"))
    if guess < hiddenNumber :
        print("The number is bigger")
    elif guess > hiddenNumber :
        print("The number is lower")
    else:
        break

if guess == hiddenNumber:
    print("you have entered the correct number")
else:
    print("you have entered the wrong number")
    print(hiddenNumber)
    
