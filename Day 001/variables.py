#Way to ask for a name and store them in a data container (variable)
name = input("What is your name?")
print(name)

#Name variable is named already
name = "Jack"
print(name)

#Asking to count how long a name is in one line WITHOUT variable
print(len(input("What is your name? ")))

#Asking to count how long a name is with storing it in a variable
name= input("What is your name? ")
length = len(name)
print(length)

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". 
# You are only allowed to use variables to solve this exercise.

#easy solution but more then 3 lines
glass1 = "milk"
glass2 = "juice"

glass3 = "empty"    #temporary variable to help to switch stuff

glass3 = glass1     #glass3 stores now milk
glass1 = glass2     #glass1 stores now juice
glass2 = glass3     #since glass3 stores milk now glass 2 stores milk

print(glass1 + " " + glass2)

#better solution
glass1 = "milk"
glass2 = "juice"

#temp is a placeholder variable

temp = glass1       #temp stores now milk
glass1 = glass2     #glass1 stores now juice
glass2 = temp       #since temp stores milk now glass 2 stores milk

print(glass1 + " " + glass2)