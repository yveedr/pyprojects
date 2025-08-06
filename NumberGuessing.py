import random


lowest_num = 1
highest_num = 100
guesses = 0
is_running = True
answer = random.randint(lowest_num, highest_num)


print("Number Guessing Game")
print(f"Enter a number between {lowest_num} and {highest_num}:")
print("-------------- START ----------------")
while is_running:
    guess = input(f"Enter a guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("Number is out of range")
        elif guess < answer:
            print("too low! try again")
        elif guess > answer:
            print("too high! try again")
        elif guess == answer:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
            
            
    else:
        print("please enter a valid number")