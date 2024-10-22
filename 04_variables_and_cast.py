#variables
print()
print('#variables')
print('no need declaration. they exist once value assigned')
print('assignment to nonexisting variable => creation of variable')
var = 1
print(var)
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print('Client name: ' + client_name + '. Account balance: ' + str(account_balance))
var = 1
print(var)
var = var + 1
print(var)
var = 100
var = 200 + 300
print(var)

#solving problems
print()
print('#solving problems')
print('Pythagorean theorem: The square of the hypotenuse is equal to the sum of the squares of the other two sides.')
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
'''
create the variables: john, mary, and adam;
assign values to the variables: The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
now create a new variable named total_apples equal to addition of the three former variables.
print the value stored in total_apples to the console;
experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
'''
john = 1
mary = 2
adam = 3
print(john, mary, adam, sep=',')
total_apples = john + mary + adam
print(total_apples)

#shortcut operators
print()
print('#shortcut operators')
x = 1
print(x)
x +=2
print(x)

#LAB
print()
print('#LAB')
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#LAB
print()
print('#LAB')
x =  0
x = float(x) #cast int(), float(), str()
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)
x =  1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)
x =  -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)