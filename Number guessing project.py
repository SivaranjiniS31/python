from random import randint 

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =10



def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High.")
        return turns -1
        
    elif  user_guess < actual_answer:
        print("Too Low.")
        return turns -1
         
        
    else:
        print(f"You got it! The answer was {actual_answer}")    
        
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard':") 
    if level == "easy": 
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
    

        
def game():        
#  choosing a random number between 1 and 100       
    print("Welcome to the number Guessing game!")
    print("I'm thinking of a number between 1 and 100")  
    answer = randint(1,100)    
    print(f"the correct answer is {answer}")  

    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts to guess the number.")

# let the user guess
        guess=int(input("Make guess:"))

        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of thr gusses, you lose")
            return
        elif guess != answer:
            print("Guess again")
        
game()        
