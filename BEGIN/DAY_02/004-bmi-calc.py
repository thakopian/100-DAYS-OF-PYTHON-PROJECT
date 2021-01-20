# follow execercise - https://repl.it/@appbrewery/day-2-2-exercise#README.md

# use the BMI formula in your code with inputs

# start with inputs

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# convert inputs to floats for divisions

hNum = float(height)
wNum = float(weight)

# calcuate the float values in the formula expression

bmi = wNum/(hNum ** hNum)

# set bmi as integer which automatically rounds the float

bmi_int = int(bmi)

# print the final rounded integer value

print(bmi_int)
