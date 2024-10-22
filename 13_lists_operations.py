
list_1 = [1]
list_2 = list_1 #Copies the name of the array, not its contents
#the two names (list_1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa
list_1[0] = 2
print(list_2)

#slice = make a brand new copy of a list, or parts of a list
list_1 = [1]
list_2 = list_1[:] #my_list[start:end]
                    #start is the index of the first element included in the slice;
                    #end is the index of the first element not included in the slice.
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#del
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#example
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)


#same with slice
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


#example
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

#example
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

##LAB
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
my_new_list = []
for i in range(len(my_list)):
    if i in my_new_list:
        continue
    else:
        my_new_list.append(i)
    
print("The list with unique elements only:")
print(my_new_list)


