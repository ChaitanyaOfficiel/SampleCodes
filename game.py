import random 
def game():
    print("Let's play the of rock paper and scissors")
    
    for i in range(3):
        user = input("Enter the you're choice:  ")
        guess = ['rock', 'paper','scissors']
        computer = random.choice(guess)
        if(user == computer):
            print("It's a draw")
        elif(user == 'rock'):
            if(computer == 'paper'):
                print("Computer won, You lost")
            else:
                print("You won, Computer lost")
        elif(user == 'scissor'):
            if(computer == 'rock'):
                print("Computer won, You lost")
            else:
                print("You won, Computer lost")
        elif(user == "paper"):
            if(computer =='scissor'):
                print("Computer won, You lost")
            else:
                print("You won, Computer lost")
        else:
            print("You have enter the wrong key")
    i+1;
game()


