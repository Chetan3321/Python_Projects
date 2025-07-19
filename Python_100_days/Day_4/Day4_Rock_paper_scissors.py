import random
game_display = ["rock","paper","Scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1"
                         "for Paper or 2 for Scissor"))
  
if user_choice >= 0 and user_choice <= 2:
     print(game_display[user_choice])
     
computer_choice = random.randint(0, 2)
print(game_display[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number. You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!") 
else:
    print("You typed an invalid number. You lose!")