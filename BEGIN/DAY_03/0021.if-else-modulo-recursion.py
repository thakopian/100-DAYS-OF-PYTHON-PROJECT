# create a program to check if a number is odd or even
# recursion - combine the input, integer and modulo operation into one line for one variable to pass into the if else test

number = int(input("Which number do you want to check? ")) % 2

if number == 0:
    print('even number')
else:
    print('odd number')
