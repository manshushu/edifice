import random

def get_word():
# A list of words that can be guessed
    words = ['python', 'java', 'computer', 'hacker', 'painter']
    word = random.choice(words)
    return word
def play_hangman():
    # setup the game
    word = get_word()
    word_letters = set(word) # letters in the word to be guessed
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set() # what the user has guessed already
    # how many attempts the user gets for guessing the word
    lives = 6

# loop until lives left is 0 or user has guessed all the letters
while len(word_letters) > 0 and lives > 0:
    # print out what user's available letters are
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

    # make list of characters showing either '_'' for not guessed letters or the actual letter in case of guessed letters 
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Current word: ', ' '.join(word_list))

    # ask user for input, making sure it is only a non-guessed valid letter
    user_letter = input('Guess a letter: ').lower()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)          
        else:
            lives -= 1  # remove one life for incorrect guess
            print('Letter is not in word.')
    
    elif user_letter in used_letters:
        print('You have already used that character. Guess another letter.')
    
    else:
        print('Invalid character. Please enter a valid letter')

# Gets here when len(word_letters) == 0 or when lives == 0
if lives == 0:
    print('Sorry, you died. The word was', word)
else:
    print('Congratulations, you guessed the word', word, '!')



play_hangman()