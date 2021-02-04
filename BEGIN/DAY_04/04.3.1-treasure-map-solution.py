# https://repl.it/@thakopian/day-4-3-exercise#main.py

# lists, index, nested lists, inputs,

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# take the input and split it into two parts for each coordinate
# convert the string into an integer

horizontal = int(position[0])
vertical = int(position[1])

# shift by -1 to adjust for the index value in the list
# row is gained by a vertical shift by -1 in the map
# reuse row ( they're all 3x3 anyway) to shift the inex of horizontal by -1
#  after selecting the row then select the column and replace that value with an X

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = 'x'

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
