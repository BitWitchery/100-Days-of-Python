# Even or odd number

# My solution to the task.
num = int(input("Enter a number: "))

new_num = int(num) % 2

if new_num != 1:
    print("It's an even number.")
else:
    print("It's an odd number.")


# Course Solution
num_to_check = int(input("What is the number you want to check? "))

if num_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")