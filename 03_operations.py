#operations
print('#operations')
print(2+2)
##exponentiation 2^3 => 2 ** 3. RESULT ALWAYS A FLOAT IF BASE AND/OR POWER ARE FLOAT
print('##exponentiation')
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2**3)
##multiplication
print('##multiplication')
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
##division.  ALWAYS A FLOAT
print('##division')
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print(1/2)
print(2/1) # integer by integter => result float
##integer division ==  floor division. RESULTS ARE ALWAYS ROUNDED! rounding always goes to the lesser integer
print('##integer division ==  floor division')
print(6 // 3) # integer by integter => result integer
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print()
print(6 // 4)
print(6. // 4) #rounded to the nearest integer value that is less than the real (not rounded) result
print(6 / 4)
print(6. / 4)
print(-6 // 4) #he real (not rounded) result is -1.5 in both cases. However, the results are the subjects of rounding. The rounding goes toward the lesser integer value, and the lesser integer value is -2, hence: -2 and -2.0
print(6 // -4)
##modulo
print('##remainder (modulo)')
print(14 % 4) #remainder left after the integer division 12/4 = 3, remainder 2
print(12 % 4.5)
##addition
print('##addition')
print(-4 + 4)
print(-4. + 8)
##substraction
print('##substraction')
print(-4 - 4)
print(4. - 8)
##unary and binary operators
print('##unary and binary operators')
print('##unary: + and -')
print(+2)
print(-1.1)
print('##binary: addition, substraction, multiplication and division operator. EXPECTED 2 ARGUMENTS')
##operators and priorities
print('exponentiation => **')
print('unaries => + and -')
print('binaries => *, /, //, %')
print('binaries => + and -')
##operator bindings
print(9 % 6 % 2) #modulo has left-sided binding
print(2 ** 2 ** 3) #the exponentiation operator uses right-sided binding
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))