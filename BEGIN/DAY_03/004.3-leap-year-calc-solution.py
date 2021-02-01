# from the challenge solution
# https://repl.it/@thakopian/day-3-3-exercise#README.md

# all you need to use is the modulo % and conditional statements
# follow the flow cart with the challenge link
# note that the 'and' operator and the != operator is not used for this section

year = int(input("Which year do you want to check? "))


if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("is a leap year")
        else:
            print("is not a leap year")
    else:
        print("is  a leap year")
else:
    print("is not a leap year")
