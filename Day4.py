# Jo Ken Po Game whith images
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
question = "YES"
while question == "YES":
    print("\033[31mLet's go Playng Jo Ken Po\033[m")
    game_images = [rock, paper, scissors]
    player_choise = int(input("What do you choise? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
    if player_choise > 2 or player_choise < 0:
        print("You choise a invalid number. You Lose.")
    else:
        print(f"You choise {game_images[player_choise]}")
        computer_choise = random.randint(0, 2)
        print(f"Computer choise {game_images[computer_choise]}")
        if computer_choise == player_choise:
            print("Draw Game")
        elif computer_choise == 2 and player_choise == 0:
            print("You Win!")
        elif computer_choise == 0 and player_choise == 2:
            print("You Lose")
        elif player_choise > computer_choise:
            print("You win!")
        elif computer_choise > player_choise:
            print("You Lose")
    question = input('Do you have a play again "Yes" or "No"?\n ').upper()