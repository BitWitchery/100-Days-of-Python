# Functions with more then one input

# my Solution to the task
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"How is it like in {location}?")

location = input("Where do you life?\n")
name = input("What's your name?\n")

greet_with(name, location)

# Positional Argument as a Solution

def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"How is it like in {location}?")

greet_with("Ben Bauer", "London")

# Keyword Arguments as an Solution

def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"How is it like in {location}?")

greet_with(name = "Tim Tailor", location = "New York")