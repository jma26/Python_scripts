from random import randint
word_bank = ['JavaScript', 'Python', 'Java', 'TypeScript', 'Hello', 'World', 'Ludicrous', 'Tenacity', 'Ferocious', 'Programming', 'Kotlin', 'Swift']

length_of_word_bank = len(word_bank)
random_integer = randint(0, length_of_word_bank - 1)
random_word = word_bank[random_integer]

def game(word):
    letters_guessed = []
    indexes = []
    guesses_remaining = 3
    
    print('Hello! Welcome to "Guess The Word!"')
    print('You have 3 tries only!')
    output = '-' * len(word)
    print(output)
    while True:
        guess = input('What letter would you like to guess? \n')
        # Check if input is more than one letter
        if len(guess) > 1:
            print('Please try again! Only one letter at a game \n')
        # Check if input is already guessed
        elif guess in letters_guessed:
            print('Please try again! Letter already guessed \n')
        elif guess not in word:
            guesses_remaining -= 1
            letters_guessed.append(guess)
            if guesses_remaining == 0:
                # Check if remaining guesses is 0 and display answer
                print('GAME OVER! Word was {} \n'.format(word))
                return False
        else:
            output_list = list(output)
            for index, letter in enumerate(word):
                if guess in letter:
                    indexes.append(index)
            for index in indexes:
                output_list[index] = guess
            output = ''.join(output_list)
            # Check if winner
            if output == word:
                print('Winner winner chicken dinner! You guessed the word correctly!')
                return False
        # Clear out indexes at every guess
        indexes = []
        print('{} guesses remaining... \n'.format(guesses_remaining))
        print('Letters guessed ---> {} \n'.format(letters_guessed))
        print(output + ' \n')
            
            
            

game(random_word.lower())
    



