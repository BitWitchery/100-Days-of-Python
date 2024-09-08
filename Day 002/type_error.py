num_char= len(input("What's your name?"))
# will show TypeError
# print("Your name has " + num_char + " characters.")

# Type() check function
print(type(num_char))

#Correctet num_char function
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Another Version
name_of_the_user = input("Enter your name ")
length_of_name = len(name_of_the_user)

print("Number of letter in your name: " + str(length_of_name))
