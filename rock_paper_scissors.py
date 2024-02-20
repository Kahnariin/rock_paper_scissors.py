import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: \n").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked: " + str(computer_pick) + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Player won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("Player won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("Player won!")
        user_wins += 1
        
    elif user_input == "rock" and computer_pick == "scissors":
        print("Player won!")
        user_wins += 1
        
    elif user_input == computer_pick:
        continue
    else:
        print("Computer won!")
        computer_wins += 1

print("Player won "+ str(user_wins) + ".")
print("Computer won "+ str(computer_wins) + ".")
print("GoodBye!")