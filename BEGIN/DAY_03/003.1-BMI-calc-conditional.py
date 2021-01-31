# BIM calc with conditional statements
# https://repl.it/@thakopian/day-3-2-exercise#README.md

# create inputs

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# create bmi calculation

bmi = round(weight/(height ** height), 2)

# check formula works with a print statement

print("your BMI is ")
print(bmi)

# create conditions

if bmi < 18.5:
    print('you are underweight')
elif bmi >= 18.5:
    print('you have a normal weight')
elif bmi >= 25:
    print('you are slightly overweight')
elif bmi >= 30:
    print('you are obese')
else:
    print('you are clinically obese')
