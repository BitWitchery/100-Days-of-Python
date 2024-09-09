print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how they need to pay based on their size choice.
# (S) Small Pizza = 15$ / (M) Medium Pizza = 20$ / (L) Large Pizza = 25$

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please try again.")

# todo: work out how much to add to their bill based on their pepperoni choice.
# Add pepperoni for Small Pizza +2$ / Medium or Large Pizza +3$

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on wheter if they want extra cheese.
# cheese for any size of pizza +1$
if extra_cheese == "Y":
    bill = +1

print(f"Your total bill is ${bill}.")


