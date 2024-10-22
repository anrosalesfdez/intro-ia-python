#BOOLEANS

# == and != => binary operators with left-sided binding. low priority
print(2==2)
print(2==2.)
print(1==2)
var = 0
print(var == 0)
print(var != 0)
var = 1
print(var == 1)
print(var != 1)
# >= and < => binary operators with left-sided binding. greater priority than == !=

#1 +, - (unary)
#2 **
#3 *, /, //, %
#4 +,- (binary))
#5 <m <=, >, >=
#6 ==, !=

#LAB
n = input('Inser value for n:')
print(type(n))
if int(n) < 100:
    v_result = False
else:
    v_result = True
print(v_result)
# if any of the if-elif-else branches contains just one instruction, you may code it in a more comprehensive form (you don't need to make an indented line after the keyword, but just continue the line after the colon).
n = int(input('Inser value for n:'))
print(type(n))
if n < 100: v_result = False
else: v_result = True
print(v_result)

#LAB
plant = input('Plant:')

if plant == 'Spathiphyllum':
    print('No, I want a big Spathiphyllum!')
elif plant == plant.upper:
    print('Yes - Spathiphyllum is the best plant ever!')
else:
    print('Spathiphyllum! Not ',plant, '!')


#LAB
#TAX CALCULATOR
income = float(input('Insert your income:'))
base = 85528
if income < base:
    tax = income*0.18-556.02
else:
    tax = 14839.02+0.32*(income-base)
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#LAB
#LEAP OR COMMON YEAR
year = int(input('Insert a year:' ))
if year < 1582:
    result = 'Not within the Gregorian calendar period'
elif year%4 != 0:
    result = 'Common year'
elif year%100 != 0:
    result = 'Leap year'
elif year%400 != 0:
    result = 'Common year'
else:
    result = 'Leap year'
print(result)