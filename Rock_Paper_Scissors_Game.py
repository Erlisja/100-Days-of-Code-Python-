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
options = [rock,paper,scissors]
while True:

    print ("Welcome to Rock, Paper, Scissors game !")
    player = int (input ("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n"))
    computer = random.randint(0,2)

    if (player >=3 or player < 0) :
        print ("You typed an invalid number, you lose!")
    else :
        print("Player:")
        print(options[player])
        print("Computer:")
        print(options [computer])
    if (computer == player):
        print("It's a draw!")
    elif (computer == 0 and player == 1):
        print ("You Won!")
    elif(computer == 0 and player == 2):
        print ("You Lost!")
    elif(computer == 1 and player == 0):
        print ("You Lost!")
    elif(computer == 1 and player == 2):
        print ("You Won!")
    elif(computer == 2 and player == 0):
        print ("You Won!")
    elif(computer == 2 and player == 1):
        print ("You Lost!")

    play_again = input('Do you want to play again? Type "Yes" or "No"\n').lower()
    if play_again != "yes":
        print("Game Over!")
        break
        

