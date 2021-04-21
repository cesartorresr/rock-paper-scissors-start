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
print("Hello! Welcome to this awesome game: ROCK PAPER SCISSORS")
list_of_game = [rock, paper, scissors]
choose_to_play = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. \n"))

if choose_to_play == 0:
  print(list_of_game[0])
elif choose_to_play == 1:
  print(list_of_game[1])
elif choose_to_play == 2:
  print(list_of_game[2])
else:
  print("Please type a number between 0 to 2 \n")  
# the pc now choose to play
choose_pc = random.randint(0, 2)
if choose_pc == 0:
    print(list_of_game[0])
elif choose_pc == 1:
    print(list_of_game[1])
else:
    print(list_of_game[2])  
# conditions to know who is the winner
if choose_to_play == 0 and choose_pc ==    






