import random
from game_data_higher_lower import data
import art_higher_lower
from replit import clear


# Get data from random
def get_random():
    return random.choice(data)


# Format the data to print organized
def data_print(value):
    name = (value['name'])
    description = (value['description'])
    country = (value['country'])
    return f" {name}, a {description}, from {country}"


# Checks followers agains user's guess and
# returns True if they if they got it right.
# Or False if they got it wrong
def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(art_higher_lower.logo)
    score = 0
    game_continue = True
    choice_a = get_random()
    choice_b = get_random()

    while game_continue:
        choice_a = choice_b
        choice_b = get_random()

        while choice_a == choice_b:
            choice_b = get_random()

        print(f"Compare A: {data_print(choice_a)}.")
        print(art_higher_lower.vs)
        print(f"Compare B: {data_print(choice_b)}.")

        guess = str(input("Who has more followers? Type 'A' or 'B': ").lower())
        a_follower = choice_a['follower_count']
        b_follower = choice_b['follower_count']
        is_corret = check_answer(guess, a_follower, b_follower)

        clear()
        print(art_higher_lower.logo)
        if is_corret:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
