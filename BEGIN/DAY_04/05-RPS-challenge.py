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

'''
rock = 0
paper = 1
scissor = 2
'''

# provide choices an an input to print them out later
rps_choices = [rock, paper, scissors]

# player input by number converted to integer
your_choice = int(
    input('choose by typing ROCK = 0, PAPER = 1, or SCISSOR = 2 \n> '))

print("your hand")
print(rps_choices[your_choice])

# computer choice randomly generated
comp_choice = random.randint(0, 2)

print("computer hand")
print(rps_choices[comp_choice])

'''
# test hard coded values
your_choice = 1
comp_choice = 2
'''

# conditional choice matrix

if your_choice == 1 and comp_choice == 0:
    print('you win')
elif comp_choice == 1 and your_choice == 0:
    print('you lose')
elif your_choice == 2 and comp_choice == 1:
    print('you win')
elif comp_choice == 1 and your_choice == 2:
    print('you lose')
else:
    print("it\'s a draw")

# your outcome logic is not correct, the outcomes don't match the rules
# account for numbers out of range stated for inputs so outcome doesn't go straight to draw
# because the range is so important you need to reconfigure your code to make sure from the beginning the user input is in the valid range of 0-2
