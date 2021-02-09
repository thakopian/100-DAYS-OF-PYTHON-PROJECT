# https://repl.it/@thakopian/day-5-1-solution#main.py

# 🚨 Don't change the code below 👇

# sample hieght selection from notes
# student_heights = 180 124 165 173 189 169 146

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

# you cannot use len() or sum() for the problem solving just the provided formula and for loops

total_height = 0
for x in student_heights:
    total_height += 1
print(total_height)

average_height = round(total_height / student_heights)
print(average_height)

'''
# Problem solving with len and sum
total_height = sum(student_heights)
number_of_sutdents = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
'''
