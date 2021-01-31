# use a nested conditional statement with elif to create a program
# to determine who can get on a ride and the prices they should pays

age = int(input('what is your age'))

if age >= 12:
    print('hope on board buckaroo!')

    if age < 12:
        print('pay $5')
    elif age <= 18:
        print('pay $9')
    else:
        print('pay $14')
else:
    print('sorry you are not old enough to ride')
