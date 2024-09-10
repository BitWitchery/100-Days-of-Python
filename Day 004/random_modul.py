import random
#import module from my own files
import my_module

# Functions for integers
random_integer = random.randint(1, 10)
print(random_integer)

# print from my own modules
print(my_module.my_favorite_number)

# print a random float number between 0 to 1
random_float = random.random()
print(random_float)

# print a random float number that can be higher then 0 to 1
random_float = random.random() * 10
print(random_float)

# print random float in a range from a to be
random_floaty = random.uniform(1,10)
print(random_floaty)