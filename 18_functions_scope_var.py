# A variable existing outside a function has a scope inside the functions' bodies, excluding those of them which define a variable of the same name
# Variable de fuera a dentro sí, de dentro a afura no
def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

#global variable = extend a variable's scope in a way which includes the functions' bodies
#Using global variable(s) inside a function forces Python to refrain from creating a new variable inside the function - the one accessible from outside will be used instead.
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)

ºvar = 1
my_function()
print(var)

#function interacts with its arguments
#changing the parameter's value doesn't propagate outside the function 
#a function receives the argument's value, not the argument itself
def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)



