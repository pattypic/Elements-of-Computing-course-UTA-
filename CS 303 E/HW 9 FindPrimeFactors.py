# File: FindPrimeFactors.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course: CS303E
#
# Date: 03/07/2023
# Description of Program:
    # 1. Find prime factors of a number
    # 2. Find the next prime number after a number
    # 3. Find the prime factors of a number
import math

def isPrime(num):
    if ( num < 2 or num % 2 == 0 ):     # Deal with evens and numbers < 2.
        return ( num == 2 )
    divisor = 3                                # See if there are any odd divisors
    while ( divisor <= math.sqrt ( num )):     # up to the square root of num.
        if ( num % divisor == 0 ) :
            return False
        else:
            divisor += 2
    return True
    
def findNextPrime(num):
    if ( num < 2 ) :
        return 2
    if ( num % 2 == 0) :               # If (num >= 2 and num is even ), the
        num -= 1                       # next prime after num is at least
    guess = num + 2                    # (num - 1) + 2 , which is odd.
    while ( not isPrime ( guess )):
        guess += 2
    return guess

def findPrimeFactors(num):
    if num == 1:
        print("1 has no prime factorization.")
    elif num < 0:
        print("Negative integer entered. Try again.")
    elif isPrime(num):
        print(f" The prime factorization of {num} is: [{num}]")
    else:
        factors = []
        d = 2
        before = num
        while num > 1:
            if num % d == 0:
                factors.append(d)
                num //= d
            else:
                d = findNextPrime(d)
        print(f" The prime factorization of {before} is: {factors}")


print("Find Prime Factors:")
num = 1
while num != 0:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    if num == 0:
        print("Goodbye")
    else:
        findPrimeFactors(num)
        print()

# Problems:
    # None