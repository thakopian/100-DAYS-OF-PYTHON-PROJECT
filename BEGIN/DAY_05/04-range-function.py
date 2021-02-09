# using for loops with the range function
# https://www.udemy.com/course/100-days-of-code/learn/lecture/18085735#content

'''
# start value a is first number
# end value b is last value but is not included in range    

for number in range (a, b):
    print(number)


'''

# print all values between 1 through 10
for number in range(1, 11):
    print(number)

'''
# add a step c for a number pattern in the range
for number in range (a, b, c):
    print(number)

'''

# print all values between 1 through 10 every 3 steps
for number in range(1, 11, 3):
    print(number)

# add all values from 1 to 100
total = 0
for x in range(1, 101):
    total += x
print(total)
