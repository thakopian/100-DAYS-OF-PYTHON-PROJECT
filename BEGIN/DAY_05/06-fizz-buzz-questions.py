# https://repl.it/@appbrewery/day-5-4-exercise
# https://repl.it/@thakopian/day-5-4-exercise

# fizz buzz is a kid's game
# start counting and evaluating the numbers for an acceptable criteria that gets you either fizz or buzz
# if both critera are true you say fizzbuzz

#######

# problem 1 - fizz buzz up to 100
# if number is divisble by 3 you say fizz
# if number is divisble by 5 you say buzz
# if the number is divisble by 3 and 5 you say fizzbuzz
# in that pattern number 15 would get you a fizzbuzz

# basically left over of modulo plus the number
# use if statements to continue the operation througgh the for loop range

'''
for x in range(0, 101):
    if x % 3 == 0:
        print(f' {x} is fizz')
    if x % 5 == 0:
        print(f' {x} is buzz')
'''
# now do it so you can get a fizzbuzz return
# have a conditional operator and elif statements
# conditional checks for all fizzbuzz statements
# elif checks for the fizz or buzz statements
# using an if statement will return a fizzbuzz with a fizz or buzz as well which we don't want
# all other numbers that don't match criteria are not printed
# or you can else: print(x) to see them in comparison if you want

for x in range(0, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(f' {x} is fizzbuzz')
    elif x % 3 == 0:
        print(f' {x} is fizz')
    elif x % 5 == 0:
        print(f' {x} is buzz')
