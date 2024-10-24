#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Immutable lists. means that appending an element to the end of the list would require the recreation of the list from scratch

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

my_list.reverse()
print(my_list)


#You can create an empty tuple like this:
empty_tuple = ()
print(type(empty_tuple))


#tuple with only one value
one_element_tuple_1 = (1, ) #If you remove the comma, you will tell Python to create a variable, not a tuple:
one_element_tuple_2 = 1., #If you remove the comma, you will tell Python to create a variable, not a tuple:

my_tuple = (1, 10, 100, 1000)


#access tuple elements by indexing
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
print(len(my_tuple))


#Tuples are immutable
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar"  ## The TypeError exception will be raised.


#delete a tuple as a whole
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined


#create a tuple using a Python built-in function called tuple()
my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>


tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # outputs: <class 'list'>