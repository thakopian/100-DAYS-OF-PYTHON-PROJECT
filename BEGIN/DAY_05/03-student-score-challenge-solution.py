# https://repl.it/@thakopian/day-5-2-exercise

# 🚨 Don't change the code below 👇

student_scores = input("Input a list of student scores ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# sample score input - student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# you normally use max() and min() function for these solutions but not with this exercise

# Write your code below this row 👇

# set high score is = 0 so that value can be added to
# for loop of x in student_scores to iterate through values
# comparison operator of x to the high score which starts at 0
# that loop will process through all the scores until only the highest value is left to compare high score which is always being added to
# therefore even if high score starts with the highest value then all values will compare to it to check the highest value in the comparison operator
# print the new high score

high_score = 0
for x in student_scores:
    if x > high_score:
        high_score = x
print(high_score)

'''
# while loop method:

n = 0
maxi = scores[n]
nxt = scores[n+1]
while maxi <= 100:
    while maxi < nxt:
        maxi = nxt
        print ("Maximum score:",maxi)
'''
