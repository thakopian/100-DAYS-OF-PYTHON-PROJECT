# BIM calc with conditional statements
# https://repl.it/@thakopian/day-3-2-exercise#README.md

# create inputs

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# create bmi calculation

bmi = round(weight/(height ** height), 2)

# check formula works with a print statement

# print(bmi)

# create conditions

if bmi < 18.5:
    print(f'your bmi is {bmi} and you are underweight')
elif bmi < 25:
    print(f'your bmi is {bmi} and you are normal weight')
elif bmi < 30:
    print(f'your bmi is {bmi} and you are overweight')
elif bmi < 35:
    print(f'your bmi is {bmi} and you are obese')
else:
    print(f'your bmi is {bmi} and you are clinically obese')
