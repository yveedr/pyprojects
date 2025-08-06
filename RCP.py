# Rock, Scissors, Paper Game

import random

options = ("rock", "scissors", "paper")
running = True

print("ROCK, SCISSORS, PAPER GAME")
print("---------- START ---------")

while running:
    player = None
    computer =  random.choice(options)
    
    
    while player not in options:
            player = input("Enter a choice (rock, scissors, paper): ").lower()  
            
    print(f"player: {player}")
    print(f"computer: {computer}")
            
    if player == computer:
                        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
                        print("You won!")
    elif player == "scissors" and computer == "paper":
                        print("You won!")
    elif player == "paper" and computer == "rock":
                        print("You won!")
    else:
                        print("You lost!")                
    if not input("Wanna play again (y/n)?: ").lower() == "y":
            running = False
            
print("thanks for playing!")
    
   
    
            
            