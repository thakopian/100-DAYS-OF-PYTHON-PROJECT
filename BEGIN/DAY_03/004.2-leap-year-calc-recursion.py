# formula to get input into integer format
calc = int(input("Which year do you want to check? "))

# year value check with elif statements instead of nested if statements


if calc % 4 == 0 and calc % 100 != 0:
    print("leap year")
elif (calc % 100) == 0:
    print("not a leap year")
elif (calc % 400) == 0:
    print("leap year")
else:
    print("not a leap year")
