# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# size and toppings inputs already established, now write the code
# set the bill variable to 0

# recursion example from class notes - https://www.udemy.com/course/100-days-of-code/learn/lecture/17965124#content

# start with conditional statement using elif not nested (nested is ok but longer)

# then add a nested if / else statement for the pepperoni depending on size
# then add a  if statement for the cheese (just one option so no alternatives here)
# your inputs must exactly match the capital cases or will end up with the wrong sum bill

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"your final bill is ${bill}")
