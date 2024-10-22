##LISTS
numbers = [10, 5, 7, 2, 1]
# Type of data to store multiple objects
# Ordered and mutable collection
# The elements inside a list may have different types
# A list are always numbered starting from zero
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content adding the first element 111: ", numbers)  # Current list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content adding in possition [1] the value of possition of [4]:", numbers)  # Printing current list content.

#length of the list
print("\nList length:", len(numbers))  # Printing the list's length.

# Lists can be nested
my_list = [1, 'a', ["list", 64, [0, 1], False]]

#delete elements
del numbers[1]
print(len(numbers))
print(numbers)

print(numbers[-1]) #the last one in the list

#insert element. list.insert(pos, elmnt) BOTH PARAMS REQUIRED
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#iterate
my_list = ["white", "purple", "blue", "yellow", "green"]
for color in my_list:
    print(color)


#LAB
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print(hat_list)

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input('Insert number: '))
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print(hat_list)

# Step 3: write a line of code that prints the length of the existing list.
len(hat_list)
print(hat_list)
