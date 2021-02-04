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

vertical = int(position[0])
horizontal = int(position[1])

print(vertical, horizontal)

'''
selected_row = map[horizontal]
selected_column[vertical - 1] = "x"
'''

coordinate = board[horizontal - 1][vertical - 1] = 'x'

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# this solution keeps stopping at the 'x' assignment at the coordinates
# I am note sure how to fix this problem
