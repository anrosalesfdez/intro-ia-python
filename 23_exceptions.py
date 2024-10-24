#Exceptions
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
#the code in the except branch is activated only when an exception has been encountered inside the try block.
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
except:
    print('Something strange has happened here... Sorry!')



while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")
