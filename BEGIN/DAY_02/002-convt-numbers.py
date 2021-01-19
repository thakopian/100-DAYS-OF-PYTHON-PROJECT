two_digit_number = input("Type a two digit number: ")

# strings have an index not integers so get the index first
con1 = two_digit_number[0]
con2 = two_digit_number[1]

# convert each index value to an integer value
num1 = int(con1)
num2 = int(con2)

# add the integers together and print the results
print(num1+num2)
