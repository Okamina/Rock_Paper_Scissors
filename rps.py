"""
Rock, Paper, Scissors:
1. User should choose: Rock, Paper or Scissors
2. Computer randomly select: R, P or S.
3. Compare the user's choice with the computer's choice
4. Who is the winner - condition
5. Inform user who is the winner
"""

from random import randint
from time import sleep

options = ["Rock", "Paper", "Scisssors"]

LOSS_MESSAGE = "Sorry. You lost!"
WIN_MESSAGE = "Congratulates. You won!"

def decide_winner(user_choice, computer_choice, user_score, computer_score):
  print ("Your choice is %s" % (user_choice))
  print ("Computer selecting ...")
  sleep(1)
  print ("Computer's choice is %s" % (computer_choice))
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print ("It's a tie")
    print ("user : computer %d : %d" % (user_score, computer_score))
  elif user_choice_index == 0 and computer_choice_index == 2:
    print (WIN_MESSAGE)
    user_score += 1
    print ("user : computer %d : %d" % (user_score, computer_score))
    if user_score == 3:
      play_game = False
  elif user_choice_index == 1 and computer_choice_index == 0:
    print (WIN_MESSAGE)
    user_score += 1
    print ("user : computer %d : %d" % (user_score, computer_score))
    if user_score == 3:
      play_game = False
  elif user_choice_index == 2 and computer_choice_index == 1:
    print (WIN_MESSAGE)
    user_score += 1
    print ("user : computer %d : %d" % (user_score, computer_score))
    if user_score == 3:
      play_game = False
  else:
    print (LOSS_MESSAGE)
    computer_score += 1
    print ("user : computer %d : %d" % (user_score, computer_score))
    if computer_score == 3:
      play_game = False

def play_RPS():
  print ("Rock, Paper, Scissors")
  print ("Play up to 3 points")
  play_game = True
  user_score = 0
  computer_score = 0
  while play_game == True:
    user_choice = input("Select R for Rock, P for Paper, or S for Scissors: \n")
    user_choice = user_choice.upper()
    sleep(1)
    if user_choice == "R":
      user_choice = "Rock"
    elif user_choice == "P":
      user_choice = "Paper"
    elif user_choice == "S":
      user_choice = "Scissors"
    else:
      print ("Something went wrong.")
      return
    computer_choice = options[randint(0, len(options)-1)]
    decide_winner(user_choice, computer_choice, user_score, computer_score)

  
  
play_RPS()  