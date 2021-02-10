# https://repl.it/@appbrewery/password-generator-start
# parse and review the challenge code before starting

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#####
# after the input it is your code to assign random index values from each list based on the integer request
# then combine them randomly to provide a return print statement for the password to the user
# the solution comes with researching methods in the random module to help solve the problem for choosing inputs

'''
# student solution 1 
# randomize with a sample range input for each string type
# then concat all values into a password variable
# used that variable to create the len of the password length
# create a random password with random.sample with range of password concat and overall len length
# create a string that joins the new random password values together and print that

rand_letters = random.sample(letters, nr_letters)
rand_numbers = random.sample(numbers, nr_numbers)
rand_symbols = random.sample(symbols, nr_symbols)
password = rand_letters + rand_numbers + rand_symbols

length = (len(password))

randomized_password = random.sample(password, length)
string = ''.join(randomized_password)

print(string)

'''

# student solution 2 with corrections for out of range bugs
# use join method with random choices method
# note that random choices returns a list so the join method combines that list into one non separated value
# pass all the pw letters, symbols, numbers into a concatenated password
# pass all the nr letters, symbols, numbers in a concatenated total character string
# create a new password with a random sample based on your concatenated values and join that together and print as the new password

pw_letters = ''.join(random.choices(letters, k=nr_letters))
pw_symbols = ''.join(random.choices(symbols, k=nr_symbols))
pw_numbers = ''.join(random.choices(numbers, k=nr_numbers))

password = pw_letters + pw_symbols + pw_numbers

total = nr_letters + nr_symbols + nr_numbers

new_password = ''.join(random.sample(password, k=total))
print('Your new password is: ' + new_password)
