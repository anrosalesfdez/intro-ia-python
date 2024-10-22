#functions => decomposition to make them understandable
# built-in functions (print, input...)
#preinstalled modules
#directly from our code

def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())


#parameters live inside functions (this is their natural environment) DEFINITION
#arguments exist outside functions, and are carriers of values passed to corresponding parameters. INVOKATION

#function with arguments
def hello(name):    # defining a function
    print("Hello,", name)    # body of the function

name = input("Enter your name: ")

hello(name)    # calling the function

#function with parameter
def message(number):
    print("Enter a number:", number)
number = 1234 #It's legal, and possible, to have a variable named the same as a function's parameter
message(1)
print(number)

def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

#Positional parameter passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

#You can mix both fashions if you want - there is only one unbreakable rule: you have to put positional arguments before keyword arguments.

#default (predefined) values 
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction("James", "Doe")
introduction("Henry")

#result keyword (not required if no value to return)
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

#one behaviour, goes through the return
happy_new_year()
#another behaviour, it does not go into the return
happy_new_year(False)

def boring_function():
    return 123

value = None
if value is None:
    print("Sorry, you don't carry any value") #if a function doesn't return a certain value using a return expression clause, it is assumed that it implicitly returns None

#lists as parameter
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5, 4, 3]))

#lists as results
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

#LAB
def is_year_leap(year):
#
# Write your code here.
#
def is_year_leap(year):
#
# Write your code here.
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
#
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False
    
    return result

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
