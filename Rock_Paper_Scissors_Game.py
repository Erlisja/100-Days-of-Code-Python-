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
        # print(f"Computer \n {options[computer]}")
        # print(f"Player \n {options [player]}")
        print("It's a draw!")
    elif (computer == 0 and player == 1):
        # print("Computer \n" + rock)
        # print("Player \n" + paper)
        print ("You Won!")
    elif(computer == 0 and player == 2):
        # print("Computer \n" + rock)
        # print("Player \n" + scissors)
        print ("You Lost!")
    elif(computer == 1 and player == 0):
        # print("Computer \n" + paper)
        # print("Player \n" + rock)
        print ("You Lost!")
    elif(computer == 1 and player == 2):
        # print("Computer \n" + paper)
        # print("Player \n" + scissors)
        print ("You Won!")
    elif(computer == 2 and player == 0):
        # print("Computer \n" + scissors)
        # print("Player \n" + rock)
        print ("You Won!")
    elif(computer == 2 and player == 1):
        # print("Computer \n" + scissors)
        # print("Player \n" + paper)
        print ("You Lost!")
    # if player == 0 and computer == 2:
    #     print("You win!")
    # elif computer == 0 and player == 2:
    #     print("You lose")
    # elif computer > player:
    #     print("You lose")
    # elif player > computer:
    #     print("You win!")
    # elif computer == player:
    #     print("It's a draw")

    play_again = input('Do you want to play again? Type "Yes" or "No"\n').lower()
    if play_again != "yes":
        print("Game Over!")
        break
        

