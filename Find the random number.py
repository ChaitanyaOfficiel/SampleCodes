import random

secretNumber = random.randint(1, 29)
print("I am currently Thinking of a number")

for i in range(1, 4):
    print("Try to Guess  the number")
    guess = int(input("Enter the Guessing number: "))
    if guess < secretNumber:
        print("The number is you enter is too low")

    elif guess > secretNumber:
        print("The number is you enter is too high")

    else:
        break


if guess  == secretNumber:
    print("You have guessed correct number")
else:
    print("You have guessced wrong number. Better luck next time ")
    print(secretNumber)