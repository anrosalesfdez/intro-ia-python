##FUNCTIONS vs. METHODS
#function doesn't belong to any data => result = function(arg)
#change the state of a selected entity => result = data.method(arg)

#Example 1
print('#Example 1')
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(0, 222) #list.insert(location, value)
print(len(numbers))
print(numbers)

#Example 2

print('#Example 2')
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

#Example 3
print('#Example 3')
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#swapping varaibles values
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

print('#swapping varaibles values')
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2): #length // 2 times (this works well for lists with both even and odd lengths, because when the list contains an odd number of elements, the middle one remains untouched)
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


#LAB - THE BEATLES
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 2:", beatles)

# step 3
for i in range(2):
    new = input('Insert other members: ')
    beatles.append(new)
print("Step 3:", beatles)

# step 4

for i in range(2):
    del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(-1, 'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))



