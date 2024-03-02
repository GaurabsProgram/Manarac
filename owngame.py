import random
import sys

def choice():
    choose = input("Hey, little stranger. Do you want to play a game? ").lower()
    return choose

def game():    
    print("Please choose the range of numbers you want to guess:  ")
    user_range = input("Enter the range:  ")
    user_range = int(user_range)
    answer = random.randint(0, user_range)
    print(answer)

    print("Choose the difficulty level (easy/medium/hard):")
    level = input("Which level do you want to play in?  :  ").lower()
    if level == "hard":
        print("You have 5 attempts.")
        attempts = 5
    elif level == "medium":
        print("You have 10 attempts.")
        attempts = 10
    elif level == "easy":
        print("You have 15 attempts.")
        attempts = 15
    else:
        print("Invalid level. Defaulting to medium and You got 10 attempts.")
        attempts = 10
        
    count = 0
    for _ in range(attempts):
        guess = int(input("Enter a number:  "))
        if guess == answer:
            count=count+1
            print(f"Congratulations! You won the game in {count} attempts.")
            sys.exit()
        elif guess > answer:
            print("A bit lower.")
            print(f"You have {count-1} out of {attempts}")
            count=count + 1
        elif guess < answer:
            print("A bit higher.")
            count=count+1
            print(f"You have {count-1} out of {attempts}")
    else:   
        print(f"Sorry, you've run out of attempts. The correct number was {answer}.")
        sys.exit()

choose = choice()

if choose == "yes":
    game()
else:
    print("Okay, maybe next time.")
