import random

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Combine the lists
combined_list = list1 + list2 + list3
print(combined_list)
# Select a random integer from the combined list
random_integer = random.choice(combined_list)
print(random_integer)
'''
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2) #find the number of duplicates of 2

print(duplicates) 



d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)



colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = {}

print(colors[0][0])
print(len(colors))

colors_dictionary = dict(colors)

print(colors_dictionary)
'''


board = [[1,2,3],[4,5,6],[7,8,9]]

for line in board:
    print(line)
    for cell in line:
        print(cell)
        if cell == 5:
            print('cell is same!')
            index = line.index(5)
            print(index)
            line[index] = 999


print(board)


board = [[1,2,3],[4,5,6],[7,8,9]]

for line in board:
    try:
        index = line.index(5)
        line[index] = 666
    except ValueError:
        print('This possition is already taken. Try another one!')


print(board)

