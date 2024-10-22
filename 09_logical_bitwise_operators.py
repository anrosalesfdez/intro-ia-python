##LOGICAL OPERATORS ==>  the arguments of these operators must be integers
#and => conjunction
#or => disjunction
#not => unary operator, logical negation (priority high, same as unary + and -)
var = 1
# Example 1:
print(var > 0)
print(not (var <= 0))
# Example 2:
print(var != 0)
print(not (var == 0))

##BITWISE OPERATORS ==>  the arguments of these operators must be integers
#& (ampersand) - bitwise conjunction
#| (bar) - bitwise disjunction
#~ (tilde) - bitwise negation
#^ (caret) - bitwise exclusive or (xor)
x = 4
y = 1
print(bin(x))
print(bin(y))

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

##BINARY LEFT AND RIGTH SHIFT
#value << bits
#value >> bits
var = 17
var_right = var >> 1 #17 floor-divided by 2 to the power of 1
var_left = var << 2 #17 multiplied by 2 to the power of 2
print(var, var_left, var_right)
