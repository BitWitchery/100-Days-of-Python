# Life in Weeks

# Create a function called life_in_weeks() using maths and f-Strings that tells us how many
# weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.

# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

#First Test solution
def life_in_weeks(x):
    age = 90 - x
    weeks = age * 52
    print(f"You have {weeks} weeks left.")

x = int(input("What is your current age?"))

life_in_weeks(x)

# My Solution for Test Run in Udemy
def life_in_week(x):
    age = 90 - x
    weeks = age * 52
    print(f"You have {weeks} weeks left.")

life_in_week(30)