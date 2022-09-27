#Game Hangman
import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

print(logo)
print("Let's go play Hangman!")
lives = len(stages) - 1
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
chosen_letter = []

for _ in range(word_length):
    display += '_'

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print("This letter is repeated. Choice other.")
    elif guess in chosen_letter:
        print("This letter is repeated. Choice other.")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(f"{''.join(display)}")

    if guess not in chosen_word and guess not in chosen_letter:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        chosen_letter += guess
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    if '_' not in display:
        end_of_game = True
        print(f"Congratulations the word is {chosen_word}.")
        print("You Win!")
