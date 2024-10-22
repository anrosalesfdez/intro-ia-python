#
# 4.3.1.8 LAB: Prime numbers
#

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    #Starting from 5, check potential factors up to the square root of n. The increment of 6 helps to skip even numbers and multiples of 3.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True