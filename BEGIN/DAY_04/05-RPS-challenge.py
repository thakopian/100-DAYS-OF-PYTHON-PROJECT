# https://repl.it/@thakopian/rock-paper-scissors-start

# how can you use inputs to make the ascii art below play rock paper scissors?
# make it randomized response to a user input
# remember the challenges we had in the last several problems and how those were solved

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

# provide choices an an input

rps_choices = [rock, paper, scissors]

your_choice = input('choose by typing rock, paper, or scissor')

rock = 0
paper = 1
scissor = 2
