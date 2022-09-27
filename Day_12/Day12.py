from random import randint
from Art_Guess_Number import logo

difficulty_easy = 10
difficulty_hard = 5

#Function to set difficulty
def difficulty():
    level = input("Choise the difficulty, type 'easy' or  'hard':")
    if level == 'easy':
        return difficulty_easy
    else:
        return difficulty_hard

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"Your game is finish the number thinked was {answer}\n"
              f"Congratulations")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 an 100.")

    # Drawing random number between 1 and 100.
    answer = randint(1, 100)
    turns = difficulty()
    guess = 0

    #Repeat the guessing functionality if they get it wrong.
    while guess != answer:
        print(f"You have a {turns} attempts.")

        #User guess a number.
        guess = int(input("Guess Game: "))

        #Track the number of turns and reduce by 1 if they get if wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Finish game.Try again")
            return
        elif guess != answer:
            print("Guess again.\n")


game()