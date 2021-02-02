# import the random module
import random
# import your own custom module
import my_th_module

# your code:

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

print(random_float/10)
print(random_integer/10)

# print(round(random_float), 2)

random_Score = random.randint(1, 100)
print(f'your actual score is {random_Score}')
