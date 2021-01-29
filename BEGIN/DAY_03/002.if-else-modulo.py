# create a program to check if a number is odd or even
# https://repl.it/@thakopian/day-3-1-test-your-code#main.py

number = int(input("Which number do you want to check? "))

calc = number % 2

print(calc)

if calc == 0:
    print('even number')
else:
    print('odd number')
