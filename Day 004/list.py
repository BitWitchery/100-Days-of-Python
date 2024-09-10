#List with States of America
states_of_america = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ","of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi","Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada","New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota","Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

# prints the whole list of states_of_america
print(states_of_america)

# want just the first name out of the list
print(states_of_america[0])

# want the last name from the list
print(states_of_america[-1])

fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

# can change items of the list -> change Cherry to Banana
fruits[0] = "Banana"
print(fruits)

# add one items to the list with append()
fruits.append("Cherry")
print(fruits)

# add more then one item to my list with extend()
fruits.extend(["Mango", "Kiwi"])
print(fruits)