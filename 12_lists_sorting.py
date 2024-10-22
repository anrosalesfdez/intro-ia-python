##we compare the adjacent elements, and by swapping some of them, we achieve our goal.

#example 1
my_list1 = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list1) - 1):  # we need (5 - 1) comparisons
    if my_list1[i] > my_list1[i + 1]:  # compare adjacent elements
        my_list1[i], my_list1[i + 1] = my_list1[i + 1], my_list1[i]  # If we end up here, we have to swap the elements.

print(my_list1)


#example 2
my_list2 = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list2) - 1):
        if my_list2[i] > my_list2[i + 1]:
            swapped = True  # a swap occurred!
            my_list2[i], my_list2[i + 1] = my_list2[i + 1], my_list2[i]

print(my_list2)

#example 3 method sort
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#reverse
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]
