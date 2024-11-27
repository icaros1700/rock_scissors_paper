import random

user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:  # busca si la repuesta del usuario esta en la lista
        continue

    random_numer = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_numer]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    elif user_input == "rock" and computer_pick == "rock":
        print("Draw!")
        draw += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw!")
        draw += 1
        
    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw!")
        draw += 1
    
    else:
        print("You lost!")
        computer_wins +=1


print("You won", user_wins, "Times.")
print("Computer won", computer_wins, "Times.")
print("You Draw", draw, "Times.")
print("Goodbye!")