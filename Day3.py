#
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = str(input('You\' re at the crossroad, where do you want to go? "Left" or "Right"?\n')).upper()
if choice1 == "RIGHT":
    choice2 = str(input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')).upper()
    if choice2 == "SWIM":
      choice3 = str(input('You arrive at the island unharmed. There is a house with 3 doorsWhich Door?\nOne "Red", One "Black" and One "Green?"\n')).upper()
      if choice3 == "RED":
        print("Burned by Fire.\nGAME OVER!")
      elif choice3 == "GREEN":
        print("Bitten by Snake.\bGAME OVER!")
      elif choice3 == "BLACK":
        print("You find the treasure.\nYou Win!!!")
      else:
        print("Game Over")
    else:
      print("Attacked by Shark.\nGAME OVER!")
else:
  print("Fall into a hole\nGAME OVER!")

