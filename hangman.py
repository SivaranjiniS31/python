import random

# Stages of the hangman
Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# List of words to choose from
word_list = ['seenu', 'sathiya', 'sivaranjini', 'sunilkumar','karthikeyan','devi','arunkumar','rahul','murugan','kayalvizhi','varshini','']

# Randomly choose a word
choosen_word = random.choice(word_list)

# Initialize lives and placeholders
lives = 6
placeholder = "_" * len(choosen_word)
correct_letters = []

# Print the initial placeholder
print(f"Word to guess: {placeholder}")

game_over = False

while not game_over:
    # Get the user's guess
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print("You already guessed that letter.")
        continue
    
    # Check if the guessed letter is in the word
    if guess in choosen_word:
        correct_letters.append(guess)
    else:
        lives -= 1
    
    # Update the display placeholder
    display = ""
    for letter in choosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(f"Current guess: {display}")
    
    # Check for win or lose
    if "_" not in display:
        game_over = True
        print("*************** YOU WIN **************")
    elif lives == 0:
        game_over = True
        print("*************** YOU LOSE **************")
    
    # Print the current stage
    print(Stages[lives])
    
               
