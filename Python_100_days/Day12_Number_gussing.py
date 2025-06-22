from random import randint

EASY_LEVEL_TERNS = 10
HARD_LEVEL_TERNS = 7

# Function to check users' guess against actual answer
def check_answer (user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too High.")
    elif user_guess < actual_answer:
        print("Too Low.")
    else:
        print(f"You got it! The answer was {actual_answer}")
        
 
def game():
    #Function to set difficulty
    def set_difficulty():
        level = input("Choose a difficult. Type 'easy' or 'hard':")
        if level == "easy":
            return EASY_LEVEL_TERNS
        else:
            return HARD_LEVEL_TERNS
        
                 
            
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)


    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
    # Let the user guess a number
    guess = int(input("Make a guess: "))

    check_answer(guess, answer)

game()