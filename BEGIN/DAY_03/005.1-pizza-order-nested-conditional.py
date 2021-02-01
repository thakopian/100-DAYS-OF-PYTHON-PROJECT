# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# size and toppings inputs already established, now write the code
# set the bill variable to 0

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
if size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
if size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3

# if add_pepperoni == 'Y':
# bill += 2

if extra_cheese == 'Y':
    bill += 1


print(f"Your final bill is ${bill}")

# code doesn't work - bill always = 0 with this format
# turns out the code does work , just input correct caps or the order won't be taken
# modified by commenting out the separate pepperoni section and adding that to the pizza size
# pepperoni cost depends on pizza size so they should be nested here
# this entire program assume only ONE input so it is all just 'if' operators which is not optimal but works in this case though doesn't scale well
