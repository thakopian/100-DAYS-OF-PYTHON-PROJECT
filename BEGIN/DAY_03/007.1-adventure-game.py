# replit - https://repl.it/@thakopian/treasure-island-start#main.py
# flow chart in class notes https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#content

# create an adventure game flow chart which will be if and elif statements
# every choice is either a continue or a game over until you win which is the final step
# print the intro to the adventure game
# ask for input for directions - use word count to check for l or r, left or right


# pseudo code:

'''
input left or right - convert input to lower case and count the l or r as a valid characters
    if right
            print game over
        else
            swim or wait (same inputs conversion as above)
            if swim
                print game over
            else  (same inputs conversion as above)
                which door - red or white or yello
                if red or white 
                    print game over
                else
                    print you win

                    
'''
# start game coding:

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

start = input("go left or go right?")
direction = start.lower()

left = start.count('l')
right = start.count('r')

if left:
    action = input('swim or wait')
else:
    print('wasted!')

choice = action.lower()

swim = choice.count('s')
wait = choice.count('w')

if wait:
    door = input('pick a door')
else:
    print('wasted!')

color = door.lower()

red = color.count('r')
blue = color.count('b')
yellow = color.count('y')


if blue:
    print('wasted!')
if red:
    print('wasted!')
if yellow:
    print('A winner is you!')
else:
    print('wasted!')
