# from day 3-5 exercise - https://repl.it/@thakopian/day-3-5-exercise#main.py

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

nameTest = name1 + name2
nameString = nameTest.lower()

v1 = nameString.count('t')
v2 = nameString.count('r')
v3 = nameString.count('u')
v4 = nameString.count('e')

v5 = nameString.count('l')
v6 = nameString.count('o')
v7 = nameString.count('v')
v8 = nameString.count('e')


t1 = v1 + v2 + v3 + v4
t2 = v5 + v6 + v7 + v8

print(t1)
print(t2)

t3 = str(t1) + str(t2)
t4 = int(t3)

print(t3)

if t4 < 10 or t4 > 90:
    print(f'your score {t3} you go together like coke and mentos')
elif t4 > 40 and t4 < 50:
    print(f'your score {t3}  you are alright together')
else:
    print(f'your score {t3} oh well')
